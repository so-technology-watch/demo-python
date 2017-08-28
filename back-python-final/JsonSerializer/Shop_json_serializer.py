# Python class for json serializer of Shop 
# Created on 2017-08-25 ( Time 18:18:33 )

import json
import datetime
from entities.Shop import Shop


class ShopJsonSerializer(object):
    def to_json(self, entity: Shop):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "code": entity.code,
            "name": entity.name,
            "address1": entity.address1,
            "address2": entity.address2,
            "zipCode": entity.zipCode,
            "city": entity.city,
            "countryCode": entity.countryCode,
            "phone": entity.phone,
            "email": entity.email,
            "executive": entity.executive,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Shop()
        if "code" in data:
            entity.code = data['code']
        else:
            entity.code = None
        entity.name = data['name']
        entity.address1 = data['address1']
        entity.address2 = data['address2']
        entity.zipCode = data['zipCode']
        entity.city = data['city']
        entity.countryCode = data['countryCode']
        entity.phone = data['phone']
        entity.email = data['email']
        entity.executive = data['executive']
        return entity
