import json
import datetime
from entities.Author import Author


class AuthorJsonSerializer(object):
    def to_json(self, entity: Author):
        return {
            "id": entity.id,
            "firstName": entity.firstName,
            "lastName": entity.lastName,
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Author()
        entity.id = data['id']
        entity.firstName = data['firstName']
        entity.lastName = data['lastName']
        return entity
