class Destination():
    def __init__(self,name=None,workspace_id=None,connection_configuration=None,destination_definition_id=None,destination_id=None,destination_template_name=None) -> None:

        self.name = name
        self.workspace_id = workspace_id
        self.connection_configuration = connection_configuration
        self.destination_definition_id = destination_definition_id
        self.destination_id = destination_id
        self.destination_template_name = destination_template_name



    def copy(self):
        return Destination(
            name=self.name,
            workspace_id=self.workspace_id,
            connection_configuration=self.connection_configuration,
            source_definition_id=self.destination_definition_id
            )

class Source():
    def __init__(self,name=None,workspace_id=None,connection_configuration=None,source_definition_id=None,source_id=None,source_template_name=None,schema=None) -> None:
        

        self.name = name
        self.workspace_id = workspace_id
        self.connection_configuration = connection_configuration
        self.source_definition_id = source_definition_id
        self.source_id = source_id
        self.source_template_name = source_template_name
        self.schema = schema


    def copy(self):
        return Source(
            name=self.name,
            workspace_id=self.workspace_id,
            connection_configuration=self.connection_configuration,
            source_definition_id=self.source_definition_id
            )


    def get_schema(self):
        return self.schema


class Connection():
    

    def __init__(self,name=None,catalog=None,name_space_definition="source",
                name_space_format="${SOURCE_NAMESPACE}",prefix="",source_id=None,destination_id=None,
                operations_ids=[],sync_catalog=None,schedule=None,schedule_data=None,
                status="active",source_catalog_id=None,geography="auto",notify_schema_changes=True,
                non_breaking_changes_preference="ignore") -> None:


        self.name = name
        self.catalog = catalog
        self.name_space_definition = name_space_definition
        self.name_space_format = name_space_format
        self.prefix = prefix
        self.source_id = source_id
        self.destination_id = destination_id
        self.operations_id = None
        self.sync_catalog = sync_catalog
        self.schedule = schedule
        self.operations_ids = operations_ids
        self.schedule_data = schedule_data
        self.status = status
        self.source_catalog_id = source_catalog_id
        self.geography = geography
        self.notify_schema_changes = notify_schema_changes
        self.non_breaking_changes_preference = non_breaking_changes_preference

    def define_connection_config(self):
        pass


    def create_connector(self):
        pass

