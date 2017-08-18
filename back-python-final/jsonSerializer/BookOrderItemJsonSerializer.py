import json
import datetime
from entities.BookOrderItem import BookOrderItem


class BookOrderItemJsonSerializer(object):
    def to_json(self, entity: BookOrderItem):
        return {
            "bookOrderId": entity.bookOrderId,
            "bookId": entity.bookId,
            "quantity": entity.quantity,
            "price": entity.price,
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = BookOrderItem()
        entity.bookOrderId = data['bookOrderId']
        entity.bookId = data['bookId']
        entity.quantity = data['quantity']
        entity.price = data['price']
        return entity
