# Python class for json serializer of Synopsis 
# Created on 2017-08-25 ( Time 18:18:33 )

import json
import datetime
from entities.Synopsis import Synopsis


class SynopsisJsonSerializer(object):
    def to_json(self, entity: Synopsis):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "bookId": entity.bookId,
            "synopsis": entity.synopsis,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Synopsis()
        if "bookId" in data:
            entity.bookId = data['bookId']
        else:
            entity.bookId = None
        entity.synopsis = data['synopsis']
        return entity
