# Python class for json serializer of EmployeeGroup 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.EmployeeGroup import EmployeeGroup


class EmployeeGroupJsonSerializer(object):
    def to_json(self, entity: EmployeeGroup):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "employeeCode": entity.employeeCode,
            "groupId": entity.groupId,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = EmployeeGroup()
        if "employeeCode" and "groupId" in data:
            entity.employeeCode = data['employeeCode']
            entity.groupId = data['groupId']
        else:
            entity.employeeCode = None
            entity.groupId = None
        return entity
