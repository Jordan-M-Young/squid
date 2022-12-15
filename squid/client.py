import base64
import requests
import json
from connectors import Source, Destination, Connection


class Client():
    def __init__(self,url="http://localhost:8000",user="airbyte",password="password") -> None:
        
        self.url = url
        self.user = user
        self.password = password


        self.headers = self.load_headers()
        self.set_default_workspace()



    def get_workspaces(self):
        workspace_url = f"{self.url}/api/v1/workspaces/list"

        return json.loads(requests.post(url=workspace_url,headers=self.headers).text)


    def set_default_workspace(self):
        workspaces = self.get_workspaces()
        default_workspace = workspaces['workspaces'][0]['workspaceId']
        self.set_active_workspace(default_workspace)

    
    def set_active_workspace(self,workspace_id):
        self.active_workspace_id = workspace_id


    def encode_password_string(self,password_string):
        encoded_password_string = base64.b64encode(password_string.encode())
        return encoded_password_string.decode()

    def make_authorization_string(self):
        base_password_string = f"{self.user}:{self.password}"
        self.authorization_string = self.encode_password_string(base_password_string)


    def load_headers(self):
        self.make_authorization_string()
        headers = {
            "Accept":"application/json",
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.authorization_string}"
            }
        return headers


    def get_destinations(self):
        destination_url = f"{self.url}/api/v1/destinations/list"
        data = {
            "workspaceId": self.workspace_id
            }
        return json.loads(requests.post(url=destination_url,headers=self.headers,data=json.dumps(data)).text)


    def get_destination(self,destination_id=None):
        destinations = self.get_destinations()
        print(type(destinations))
        for destination in destinations['sources']:
            if destination['sourceId'] != destination_id:
                continue

            break

        return Destination(
            name=destination['name'],
            workspace_id=self.active_workspace_id,
            connection_configuration=destination['connectionConfiguration'],
            destination_definition_id=destination['destinationDefinitionId']
            )


    def push_destination(self,destination):

        create_destination_url = f"{self.url}/api/v1/destinations/create"
    
        destination_configuration = {
            "destinationDefinitionId":destination.destination_definition_id,
            "connectionConfiguration":destination.connection_configuration,
            "workspaceId":destination.workspace_id,
            "name": destination.name
        }


        response = json.loads(
            requests.post(url=create_destination_url,headers=self.headers,data=json.dumps(destination_configuration)).text
        )

        response = json.loads(response.text)
        destination_id = response['destinationId']
        destination.destination_id = destination_id
        destination.destination_template_name = response['destinationName']

        return destination

    def get_sources(self):
        source_url = f"{self.url}/api/v1/sources/list"

        data = {
            "workspaceId": self.active_workspace_id
            }

        return json.loads(requests.post(url=source_url,headers=self.headers,data=json.dumps(data)).text)



    def get_source(self,source_id=None):
        sources = self.get_sources()

        for source in sources['sources']:
            if source['sourceId'] != source_id:
                continue

            break

        return Source(
            name=source['name'],
            workspace_id=self.active_workspace_id,
            connection_configuration=source['connectionConfiguration'],
            source_definition_id=source['sourceDefinitionId']
            )

    def get_source_schema(self,source_id):
        get_schema_url = f"{self.url}/api/v1/sources/discover_schema"

        data = {
            "sourceId":source_id
        }

        return json.loads(requests.post(url=get_schema_url,headers=self.headers,data=json.dumps(data)).text)


    def push_source(self,source):
        create_source_url = f"{self.url}/api/v1/sources/create"

        source_configuration = {
            "sourceDefinitionId":source.source_definition_id,
            "connectionConfiguration":source.connection_configuration,
            "workspaceId":source.workspace_id,
            "name": source.name
        }



        create_response = requests.post(
            url=create_source_url,
            headers=self.headers,
            data=json.dumps(source_configuration))


        response = json.loads(create_response.text)
        source_id = response['sourceId']
        source.source_id = source_id
        source.source_template_name = response['sourceName']
        source.schema = self.get_source_schema(source_id)



        return source

    
    def get_connections(self):
        url = f"{self.url}/api/v1/connections/list"
        data = {
        "workspaceId": self.workspace_id
        }

        return json.loads(requests.post(url=url,headers=self.headers,data=json.dumps(data)).text)



    def get_connection(self,connection_id):

        connections = self.get_connections()

        for connection in connections["connections"]:
            if connection["connectionId"] != connection_id:
                continue

            break

        
        return Connection(
            connection_config=connection
        )