import json
import datetime
from entities.Shop import Shop


class ShopJsonSerializer(object):
    def to_json(self, entity: Shop):
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
        data = json.loads(json_content)
        entity = Shop()
        entity.code = data['code']
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
