# Python class for json serializer of BookOrderItem 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.BookOrderItem import BookOrderItem


class BookOrderItemJsonSerializer(object):
    def to_json(self, entity: BookOrderItem):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "bookOrderId": entity.bookOrderId,
            "bookId": entity.bookId,
            "quantity": entity.quantity,
            "price": entity.price,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = BookOrderItem()
        if "bookOrderId" and "bookId" in data:
            entity.bookOrderId = data['bookOrderId']
            entity.bookId = data['bookId']
        else:
            entity.bookOrderId = None
            entity.bookId = None
        entity.quantity = data['quantity']
        entity.price = data['price']
        return entity
