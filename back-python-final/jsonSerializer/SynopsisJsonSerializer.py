import json
import datetime
from entities.Synopsis import Synopsis


class SynopsisJsonSerializer(object):
    def to_json(self, entity: Synopsis):
        return {
            "bookId": entity.bookId,
            "synopsis": entity.synopsis,
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Synopsis()
        entity.bookId = data['bookId']
        entity.synopsis = data['synopsis']
        return entity
