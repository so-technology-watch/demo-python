import json
import datetime
from entities.Review import Review


class ReviewJsonSerializer(object):
    def to_json(self, entity: Review):
        return {
            "customerCode": entity.customerCode,
            "bookId": entity.bookId,
            "reviewText": entity.reviewText,
            "reviewNote": entity.reviewNote,
            "creation": str(entity.creation),
            "lastUpdate": str(entity.lastUpdate),
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Review()
        entity.customerCode = data['customerCode']
        entity.bookId = data['bookId']
        entity.reviewText = data['reviewText']
        entity.reviewNote = data['reviewNote']
        entity.creation = datetime.datetime.strptime(data['creation'], "%Y-%m-%d %H:%M:%S")
        entity.lastUpdate = datetime.datetime.strptime(data['lastUpdate'], "%Y-%m-%d %H:%M:%S")
        return entity
