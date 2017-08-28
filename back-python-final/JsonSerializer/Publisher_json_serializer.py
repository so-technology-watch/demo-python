# Python class for json serializer of Publisher 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.Publisher import Publisher


class PublisherJsonSerializer(object):
    def to_json(self, entity: Publisher):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "code": entity.code,
            "countryCode": entity.countryCode,
            "name": entity.name,
            "email": entity.email,
            "contact": entity.contact,
            "city": entity.city,
            "zipCode": entity.zipCode,
            "phone": entity.phone,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Publisher()
        if "code" in data:
            entity.code = data['code']
        else:
            entity.code = None
        entity.countryCode = data['countryCode']
        entity.name = data['name']
        entity.email = data['email']
        entity.contact = data['contact']
        entity.city = data['city']
        entity.zipCode = data['zipCode']
        entity.phone = data['phone']
        return entity
