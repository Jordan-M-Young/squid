# squid
Library wrapper for airbyte api, for easy programmatic access to your local or cloud based airbyte instance(s)

## Prerequisites

- `requests`

## Installation

This isn't a package yet, so clone this directory:

```shell
git clone git@github.com:Jordan-M-Young/squid.git
```
into the part of your project directory where modules are stored.


## Connecting to Airbyte

This part assumes you have an airbyte instance running, either locally or in ~ the cloud ~.
If you don't have one running check [here](https://docs.airbyte.com/category/deploy-airbyte-open-source) to get started.


```python
from squid.client import Client

# initialize airbyte client
client = Client(
  url = "http://localhost:8000",
  user = "airbyte",
  password = "password"
)

#the above use the default val for each arg
# client = Client() would also work for the default scenario
```


## Setting a workspace

Airbyte segments sources, destinations, connectors, etc into groups called workspaces. If you're just starting out you probably only have 1 on your instance. If this is the case then your client will automatically set this workspace to be your active workspace, no work needed! 


If you still need to select which workspace you want to work with, first take a look at your workspaces:

```python

workspaces = client.get_workspaces()

```

This will return a dictionary containing relevant information about all of the workspaces available on your instance. Find the 'id' of the workspace you want and the run the following in your script.

```python

workspace_id = "<MY_WORKSPACE_ID>"
client.set_active_workspace(work_space_id)

```

Retrieve your workspace_id at any time by

```python

client.active_workspace_id

```


## Interacting with Connectors

Once you've set your workspace you're ready to interact with connectors! 

### Sources

To view which source type connectors exist within your airbyte instance run the following in your notebook/script.

```python

sources_information_dict = client.get_sources()

```

This will return a dictionary containing all relevant information for each source in your workspace.

To get information on a single source:

```python

source_id = "<MY_SOURCE_ID>"

source_obj = client.get_source(source_id)

```

Which will return a Source class object, with attributes values reflecting the information observed in the dictionary returned from `client.get_sources()`.

*SourceId != SourceDefinitionId, you want the former not the latter.

# Why Squid

Airbyte has an octopus mascot (octavia), so a squid companion doesn't seem too far fetched. :sunglasses:


# Roadmap

- Testing + Error handling. Currently the code expects that airbyte is configured properly, which might not be true!

- Add more functionality around workspaces, jobs, etc. Currently all the functionality is based around pulling exsiting sources/destinations from an instance, modifying them in some way. Combining them into a new connection and pushing the connection. This obviously isn't the only thing you might want to do with your airbyte instance. Help is appreciated!!

 - Once squid's functionality represents what can be accomplished with airbyte's api, then we'll turn this into a python package.
