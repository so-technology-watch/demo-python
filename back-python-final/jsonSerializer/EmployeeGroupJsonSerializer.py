import json
import datetime
from entities.EmployeeGroup import EmployeeGroup


class EmployeeGroupJsonSerializer(object):
    def to_json(self, entity: EmployeeGroup):
        return {
            "employeeCode": entity.employeeCode,
            "groupId": entity.groupId,
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = EmployeeGroup()
        entity.employeeCode = data['employeeCode']
        entity.groupId = data['groupId']
        return entity
