import json
import datetime
from entities.Publisher import Publisher


class PublisherJsonSerializer(object):
    def to_json(self, entity: Publisher):
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
        data = json.loads(json_content)
        entity = Publisher()
        entity.code = data['code']
        entity.countryCode = data['countryCode']
        entity.name = data['name']
        entity.email = data['email']
        entity.contact = data['contact']
        entity.city = data['city']
        entity.zipCode = data['zipCode']
        entity.phone = data['phone']
        return entity
