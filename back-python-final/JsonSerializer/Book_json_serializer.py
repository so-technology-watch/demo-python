# Python class for json serializer of Book 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.Book import Book


class BookJsonSerializer(object):
    def to_json(self, entity: Book):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "id": entity.id,
            "publisherId": entity.publisherId,
            "authorId": entity.authorId,
            "isbn": entity.isbn,
            "title": entity.title,
            "price": entity.price,
            "quantity": entity.quantity,
            "discount": entity.discount,
            "availability": entity.availability,
            "bestSeller": entity.bestSeller,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Book()
        if "id" in data:
            entity.id = data['id']
        else:
            entity.id = None
        entity.publisherId = data['publisherId']
        entity.authorId = data['authorId']
        entity.isbn = data['isbn']
        entity.title = data['title']
        entity.price = data['price']
        entity.quantity = data['quantity']
        entity.discount = data['discount']
        entity.availability = data['availability']
        entity.bestSeller = data['bestSeller']
        return entity
