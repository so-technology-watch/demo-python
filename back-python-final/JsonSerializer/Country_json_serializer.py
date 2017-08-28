# Python class for json serializer of Country 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.Country import Country


class CountryJsonSerializer(object):
    def to_json(self, entity: Country):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "code": entity.code,
            "name": entity.name,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Country()
        if "code" in data:
            entity.code = data['code']
        else:
            entity.code = None
        entity.name = data['name']
        return entity
