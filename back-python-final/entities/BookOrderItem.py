# Python class for entity BookOrderItem 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class BookOrderItem(Base):
    __tablename__ = 'BookOrderItem'
    __table_args__ = {'autoload': True}

    def __init__(self, bookOrderId='null', bookId='null', quantity='null', price='null'):
        """
        Init the table
        """
        self.bookOrderId = bookOrderId
        self.bookId = bookId
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "bookOrderId": self.bookOrderId,
            "bookId": self.bookId,
            "quantity": self.quantity,
            "price": self.price,
        }
