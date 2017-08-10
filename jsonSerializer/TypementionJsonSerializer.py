import json
import datetime
from entities.Typemention import Typemention


class TypementionJsonSerializer(object):
    def to_json(self, entity: Typemention):
        return {
            "idMention": entity.idMention,
            "labelMention": entity.labelMention,
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Typemention()
        entity.idMention = data['idMention']
        entity.labelMention = data['labelMention']
        return entity
