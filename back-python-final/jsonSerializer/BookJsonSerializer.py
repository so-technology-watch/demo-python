import json
import datetime
from entities.Book import Book


class BookJsonSerializer(object):
    def to_json(self, entity: Book):
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
        data = json.loads(json_content)
        entity = Book()
        entity.id = data['id']
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
