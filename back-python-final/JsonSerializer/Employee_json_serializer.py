# Python class for json serializer of Employee 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.Employee import Employee


class EmployeeJsonSerializer(object):
    def to_json(self, entity: Employee):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "code": entity.code,
            "shopCode": entity.shopCode,
            "firstName": entity.firstName,
            "lastName": entity.lastName,
            "manager": entity.manager,
            "badgeNumber": entity.badgeNumber,
            "email": entity.email,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Employee()
        if "code" in data:
            entity.code = data['code']
        else:
            entity.code = None
        entity.shopCode = data['shopCode']
        entity.firstName = data['firstName']
        entity.lastName = data['lastName']
        entity.manager = data['manager']
        entity.badgeNumber = data['badgeNumber']
        entity.email = data['email']
        return entity
