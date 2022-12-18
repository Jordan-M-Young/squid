# squid
Library that wraps airbyte api, for easy programmatic access to your local or cloud based airbyte instance(s)

#Prerequisites

Just the requests library for now.

# Installation

This isn't a package yet, so clone this directory:

```shell
git clone git@github.com:Jordan-M-Young/squid.git
```
into the part of your project directory where modules are stored.


# Connecting to Airbyte

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


# Roadmap

Add more functionality around workspaces, jobs, etc. Currently all the functionality is based around pulling exsiting sources/destinations from an instance, modifying them in some way. Combining them into a new connection and pushing the connection. This obviously isn't the only thing you might want to do with your airbyte instance. Help is appreciated!!

Once squid's functionality represents what can be accomplished with airbyte's api, then we'll turn this into a python package.
