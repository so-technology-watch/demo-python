# Python class for entity Review 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class Review(Base):
    __tablename__ = 'Review'
    __table_args__ = {'autoload': True}

    def __init__(self, customerCode='null', bookId='null', reviewText='null', reviewNote='null', creation='null', lastUpdate='null'):
        """
        Init the table
        """
        self.customerCode = customerCode
        self.bookId = bookId
        self.reviewText = reviewText
        self.reviewNote = reviewNote
        self.creation = creation
        self.lastUpdate = lastUpdate

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "customerCode": self.customerCode,
            "bookId": self.bookId,
            "reviewText": self.reviewText,
            "reviewNote": self.reviewNote,
            "creation": self.creation,
            "lastUpdate": self.lastUpdate,
        }
