import base64
import json
import requests


def encode_password_string(password_string):
    encoded_password_string = base64.b64encode(password_string.encode())
    return encoded_password_string.decode()


def get_workspaces(headers):
    workspace_url = "http://localhost:8000/api/v1/workspaces/list"

    return json.loads(requests.post(url=workspace_url,headers=headers).text)


def get_sources(workspace_id,headers):
    source_url = "http://localhost:8000/api/v1/sources/list"
    data = {"workspaceId": workspace_id}

    return json.loads(requests.post(url=source_url,headers=headers,data=json.dumps(data)).text)

def create_source(source_configuration,headers):
    create_source_url = "http://localhost:8000/api/v1/sources/create"


    create_response = requests.post(
        url=create_source_url,
        headers=headers,
        data=json.dumps(source_configuration))

    return json.loads(create_response.text)


def get_destinations(workspace_id,headers):
    destination_url = "http://localhost:8000/api/v1/destinations/list"
    data = {"workspaceId": workspace_id}
    return json.loads(requests.post(url=destination_url,headers=headers,data=json.dumps(data)).text)


def create_destination(destination_configuration,headers):
    create_destination_url = "http://localhost:8000/api/v1/destinations/create"
    
    return json.loads(
        requests.post(url=create_destination_url,headers=headers,data=json.dumps(destination_configuration)).text
    )

def get_connections(workspace_id,headers):
    url = "http://localhost:8000/api/v1/connections/list"
    data = {
    "workspaceId": workspace_id
    }

    return json.loads(requests.post(url=url,headers=headers,data=json.dumps(data)).text)


def get_source_schema(source_id,headers):
    get_schema_url ="http://localhost:8000/api/v1/sources/discover_schema"
    data = {
        "sourceId":source_id
    }

    return json.loads(requests.post(url=get_schema_url,headers=headers,data=json.dumps(data)).text)



def build_connector(connection_config,headers):
    connector_url = "http://localhost:8000/api/v1/connections/create"
    return json.loads(requests.post(
        url=connector_url,
        headers=headers,
        data = json.dumps(connection_config)
        ).text)


def foo():
    pass



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


    def make_authorization_string(self):
        base_password_string = f"{self.user}:{self.password}"
        self.authorization_string = encode_password_string(base_password_string)


    def load_headers(self):
        self.make_authorization_string()
        headers = {
            "Accept":"application/json",
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.authorization_string}"
            }
        return headers



    def get_sources(self):
        source_url = f"{self.url}/api/v1/sources/list"

        data = {
            "workspaceId": self.active_workspace_id
            }

        return json.loads(requests.post(url=source_url,headers=self.headers,data=json.dumps(data)).text)



    def get_source(self,source_id=None):
        sources = self.get_sources()
        print(type(sources))
        for source in sources['sources']:
            if source['sourceId'] != source_id:
                continue

            source_definition_id = source['sourceDefinitionId']
            source_id = source['sourceId']
            name = source['name']
            connection_configuration = source['connectionConfiguration']

            break

        return Source(
            name=name,
            workspace_id=self.active_workspace_id,
            connection_configuration=connection_configuration,
            source_definition_id=source_definition_id
            )

    

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
        source.source_id = response['sourceId']
        source.source_template_name = response['sourceName']


        return source







class Source():
    def __init__(self,name=None,workspace_id=None,connection_configuration=None,source_definition_id=None,source_id=None) -> None:
        

        self.name = name
        self.workspace_id = workspace_id
        self.connection_configuration = connection_configuration
        self.source_definition_id = source_definition_id
        self.source_id = None
        self.source_template_name = None

    def get_template_config(self):
        return self.connection_configuration





class Connection():
    

    def __init__(self) -> None:
        pass


    def define_connection_config(self):
        pass


    def create_connector(self):
        pass















# %%%


import base64



f = "airbyte:password"


encoded = base64.b64encode(f.encode())
print(encoded.decode())
# %%
