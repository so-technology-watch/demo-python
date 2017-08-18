# Python class for entity BookOrderItem 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class BookOrderItem(Base):
    __tablename__ = 'BookOrderItem'
    bookOrderId = Column(Integer, ForeignKey('BookOrder.id'), primary_key=True, nullable=False)
    bookId = Column(Integer, ForeignKey('Book.id'), primary_key=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

    def __init__(self, bookOrderId='null', bookId='null', quantity='null', price='null'):
        self.bookOrderId = bookOrderId
        self.bookId = bookId
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
            "bookOrderId": self.bookOrderId,
            "bookId": self.bookId,
            "quantity": self.quantity,
            "price": self.price,
        }
