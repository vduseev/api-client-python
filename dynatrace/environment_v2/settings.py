from typing import Optional, Dict, Any

from dynatrace.dynatrace_object import DynatraceObject
from dynatrace.http_client import HttpClient
from dynatrace.pagination import PaginatedList


class SettingService:
    ENDPOINT = "/api/v2/settings/objects"

    def __init__(self, http_client: HttpClient):
        self.__http_client = http_client
    
    def list_objects(self,schema_id: Optional[str] = None,
             scope: Optional[str] = None,external_ids: Optional[str] = None,
             fields: Optional[str] = None,
             filter:Optional[str] = None, sort:Optional[str] = None, page_size:Optional[str] = None) -> PaginatedList["DynatraceObject"]:
        """Lists settings

        :return: a list of settings with details
        """
        params = {
            "schemaIds": schema_id,
            "scope": scope,
            "fields": fields,
            "externalIds": external_ids,
            "filter": filter,
            "sort": sort,
            "pageSize": page_size,
        }
        return PaginatedList(Settings, self.__http_client, target_url=self.ENDPOINT, list_item="items", target_params=params)
    
    def create_object(self,external_id,object_id,schema_id,schema_version,scope, value,validate_only):
        """Creates a new settings object

        :param external_id: External identifier for the object being created
        :param object_id: The ID of the settings object that should be replaced. Only applicable if an external identifier
        :param object_id: the ID of the object
        :param schema_id: The schema on which the object is based
        :param schema_version: The version of the schema on which the object is based.
        :param scope The scope that the object targets. For more details, please see Dynatrace Documentation.
        :param value The value of the setting.
        :return: a Settings object
        """        
        params = {
            "validate_only": validate_only,
        }
        body =[ {
            "externalId" : external_id,
            "objectId": object_id,
            "schemaId": schema_id,
            "schemaVersion": schema_version,
            "scope": scope,
            "value" : value

        }]
   
        response = self.__http_client.make_request(self.ENDPOINT,params=body, method="POST",query_params=params).json()
        return response
    
    
    def get_object(self, object_id: str):
        """Gets parameters of specified settings object

        :param object_id: the ID of the object
        :return: a Settings object
        """
        response = self.__http_client.make_request(f"{self.ENDPOINT}/{object_id}").json()
        return Settings(raw_element=response)

    def update_object(self, object_id: str,  value):
        """Updates an existing settings object
        
        :param object_id: the ID of the object

        """
        return self.__http_client.make_request(path=f"{self.ENDPOINT}/{object_id}", params=value, method="PUT")

    def delete_object(self, object_id: str):
        """Deletes the specified object

        :param object_id: the ID of the object
        :return: HTTP response
        """
        return self.__http_client.make_request(path=f"{self.ENDPOINT}/{object_id}", method="DELETE")

class Settings(DynatraceObject):
    def _create_from_raw_data(self, raw_element: Dict[str, Any]):
        # Mandatory
        self.objectId: str = raw_element["objectId"]
        self.value: str = raw_element["value"]