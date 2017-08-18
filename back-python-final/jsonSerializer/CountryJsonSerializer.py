import json
import datetime
from entities.Country import Country


class CountryJsonSerializer(object):
    def to_json(self, entity: Country):
        return {
            "code": entity.code,
            "name": entity.name,
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Country()
        entity.code = data['code']
        entity.name = data['name']
        return entity
