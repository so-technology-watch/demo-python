# Python class for json serializer of Author 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.Author import Author


class AuthorJsonSerializer(object):
    def to_json(self, entity: Author):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "id": entity.id,
            "firstName": entity.firstName,
            "lastName": entity.lastName,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Author()
        if "id" in data:
            entity.id = data['id']
        else:
            entity.id = None
        entity.firstName = data['firstName']
        entity.lastName = data['lastName']
        return entity
