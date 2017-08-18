# Python class for entity Book 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class Book(Base):
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    publisherId = Column(Integer, ForeignKey('Publisher.code', ondelete='RESTRICT'), nullable=False)
    authorId = Column(Integer, ForeignKey('Author.id', ondelete='RESTRICT'), nullable=False)
    isbn = Column(String, nullable=False)
    title = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    discount = Column(Integer)
    availability = Column(Integer)
    bestSeller = Column(Integer)

    def __init__(self, id='null', publisherId='null', authorId='null', isbn='null', title='null', price='null', quantity='null', discount='null', availability='null', bestSeller='null'):
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
