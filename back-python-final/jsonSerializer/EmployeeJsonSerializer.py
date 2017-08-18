import json
import datetime
from entities.Employee import Employee


class EmployeeJsonSerializer(object):
    def to_json(self, entity: Employee):
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
        data = json.loads(json_content)
        entity = Employee()
        entity.code = data['code']
        entity.shopCode = data['shopCode']
        entity.firstName = data['firstName']
        entity.lastName = data['lastName']
        entity.manager = data['manager']
        entity.badgeNumber = data['badgeNumber']
        entity.email = data['email']
        return entity
