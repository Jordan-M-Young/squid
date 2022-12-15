import requests
import json

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