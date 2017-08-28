# Python class for json serializer of Workgroup 
# Created on 2017-08-25 ( Time 18:18:33 )

import json
import datetime
from entities.Workgroup import Workgroup


class WorkgroupJsonSerializer(object):
    def to_json(self, entity: Workgroup):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "id": entity.id,
            "name": entity.name,
            "description": entity.description,
            "creationDate": str(entity.creationDate),
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Workgroup()
        if "id" in data:
            entity.id = data['id']
        else:
            entity.id = None
        entity.name = data['name']
        entity.description = data['description']
        entity.creationDate = datetime.datetime.strptime(data['creationDate'], "%Y-%m-%d %H:%M:%S")
        return entity
