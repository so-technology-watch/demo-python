# Python class for entity Book 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class Book(Base):
    __tablename__ = 'Book'
    __table_args__ = {'autoload': True}

    def __init__(self, id='null', publisherId='null', authorId='null', isbn='null', title='null', price='null', quantity='null', discount='null', availability='null', bestSeller='null'):
        """
        Init the table
        """
        self.id = id
        self.publisherId = publisherId
        self.authorId = authorId
        self.isbn = isbn
        self.title = title
        self.price = price
        self.quantity = quantity
        self.discount = discount
        self.availability = availability
        self.bestSeller = bestSeller

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id": self.id,
            "publisherId": self.publisherId,
            "authorId": self.authorId,
            "isbn": self.isbn,
            "title": self.title,
            "price": self.price,
            "quantity": self.quantity,
            "discount": self.discount,
            "availability": self.availability,
            "bestSeller": self.bestSeller,
        }
