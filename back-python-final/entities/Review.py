# Python class for entity Review 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class Review(Base):
    __tablename__ = 'Review'
    customerCode = Column(String, ForeignKey('Customer.code'), primary_key=True, nullable=False)
    bookId = Column(Integer, ForeignKey('Book.id'), primary_key=True, nullable=False)
    reviewText = Column(String)
    reviewNote = Column(Integer)
    creation = Column(Date)
    lastUpdate = Column(Date)

    def __init__(self, customerCode='null', bookId='null', reviewText='null', reviewNote='null', creation='null', lastUpdate='null'):
        self.customerCode = customerCode
        self.bookId = bookId
        self.reviewText = reviewText
        self.reviewNote = reviewNote
        self.creation = creation
        self.lastUpdate = lastUpdate

    def to_dict(self):
        return {
            "customerCode": self.customerCode,
            "bookId": self.bookId,
            "reviewText": self.reviewText,
            "reviewNote": self.reviewNote,
            "creation": self.creation,
            "lastUpdate": self.lastUpdate,
        }
