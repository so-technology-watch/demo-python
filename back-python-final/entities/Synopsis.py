# Python class for entity Synopsis 
# Created on 2017-08-25 ( Time 18:18:33 )

from commons.get_connection import Base


class Synopsis(Base):
    __tablename__ = 'Synopsis'
    __table_args__ = {'autoload': True}

    def __init__(self, bookId='null', synopsis='null'):
        """
        Init the table
        """
        self.bookId = bookId
        self.synopsis = synopsis

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "bookId": self.bookId,
            "synopsis": self.synopsis,
        }
