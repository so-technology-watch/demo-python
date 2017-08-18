import json
import datetime
from entities.Customer import Customer


class CustomerJsonSerializer(object):
    def to_json(self, entity: Customer):
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
        data = json.loads(json_content)
        entity = Customer()
        entity.code = data['code']
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
