# Python class for json serializer of Customer 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.Customer import Customer


class CustomerJsonSerializer(object):
    def to_json(self, entity: Customer):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "code": entity.code,
            "countryCode": entity.countryCode,
            "firstName": entity.firstName,
            "lastName": entity.lastName,
            "login": entity.login,
            "password": entity.password,
            "age": entity.age,
            "city": entity.city,
            "zipCode": entity.zipCode,
            "phone": entity.phone,
            "reviewer": entity.reviewer,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Customer()
        if "code" in data:
            entity.code = data['code']
        else:
            entity.code = None
        entity.countryCode = data['countryCode']
        entity.firstName = data['firstName']
        entity.lastName = data['lastName']
        entity.login = data['login']
        entity.password = data['password']
        entity.age = data['age']
        entity.city = data['city']
        entity.zipCode = data['zipCode']
        entity.phone = data['phone']
        entity.reviewer = data['reviewer']
        return entity
