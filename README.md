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

Modify the source's attributes at your discretion... You'll most likely want to update the name and configuration of your source. In this library a source object's `connection_configuration` attribute holds all the key:value pairs that you would enter when configuring the airbyte connector in the UI.

```python

source_obj.name = '<MODIFIED_SOURCE_NAME>'

source_obj.connection_figuration = {
     "field1": "<NEW_FIELD_1_VALUE>",
     "field2":"<NEW_FIELD_2_VALUE>"
}

```


Once you're satisfied with the configuration of your updated source connector, push it to your airbyte instance with:

```python

source_obj = client.push_source(source_obj)

```

If succesful, your source should be visible in your airbyte ui or with the `get_sources` method. Nice! The returned source_obj will be updated with your new source's `source_id` attribute and its `source_schema` attribute, which you'll need for building a connection later.


**Note: Like all classes you're free to instantiate instances of a Source class object on your own. Make sure you've familiarized yourself with the class and its attributes as well as understanding the configuration of the airbyte source you're emulating!



### Destinations

Destination's are similar to sources in this library see the following:


```python

# get a dictionary with info on your destinations
destinations_info_dict = client.get_destinations()


# return a destination class object based on a passed destinationId
destination_obj = client.get_destination(my_destination_id)

#modify the destination configuration and name
destination_obj.name = new_destination_name
destination_obj.connector_configuration = {key1:new_val1.....}


#push your destination to airbyte
destination_obj = client.push_destination(destination_obj)


```



### Connections

Connections are as the name suggests a connection between a source and a destination forming a Extraction and Loading pipeline. We can interact and build connection using this library.

To view information on connections in your workspace, you guessed it:

```python

connection_info_dict = client.get_connections()

```

To return a connection class object, yep:

```python

connection_obj = client.get_connection(connection_id)

```

To create a modified connection you can set the objects attributes like so (see squid/connectors.py for full list of attributes) like so:

```python

connection_obj.name = "NewConnection"
connection_obj.sourceId = my_source_id
connection_obj.SyncCatalog = {...}

```

This way works once you've familiarized yourself with the the configuration of connections. The easier way to build a customized connection is to use:

```python

connection_obj = client.build_connection(source_obj,destinatino_obj)

```

Which will return a connection_obj configure with the settings of your newly configured source and destination. Once you're satisfied push your connection to airbyte!

```python

connection_obj = client.push_connection(connection_obj)

```

If you were succesful, congrats! If not, message me or write an issue! If you have suggestions or ideas, lets collab!







# Why Squid

Airbyte has an octopus mascot (octavia), so a squid companion doesn't seem too far fetched. :sunglasses:


# Roadmap


- [ ] Add Tests
- [ ] Implement Error Handling in current classes/methods
- [ ] Add Classes/methods for Workspaces
- [ ] Add methods to client for jobs
- [ ] Add methods to update connection state
- [ ] Add methods to interact with the instance scheduler
- [ ] Add methods to get logs 
- [ ] Add methods to interact with the web-backend 
.
.
.
- [ ] repo -> python package 

