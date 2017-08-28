# Python class for json serializer of Review 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.Review import Review


class ReviewJsonSerializer(object):
    def to_json(self, entity: Review):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "customerCode": entity.customerCode,
            "bookId": entity.bookId,
            "reviewText": entity.reviewText,
            "reviewNote": entity.reviewNote,
            "creation": str(entity.creation),
            "lastUpdate": str(entity.lastUpdate),
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Review()
        if "customerCode" and "bookId" in data:
            entity.customerCode = data['customerCode']
            entity.bookId = data['bookId']
        else:
            entity.customerCode = None
            entity.bookId = None
        entity.reviewText = data['reviewText']
        entity.reviewNote = data['reviewNote']
        entity.creation = datetime.datetime.strptime(data['creation'], "%Y-%m-%d %H:%M:%S")
        entity.lastUpdate = datetime.datetime.strptime(data['lastUpdate'], "%Y-%m-%d %H:%M:%S")
        return entity
