# Python class for entity Synopsis 
# Created on 2017-08-18 ( Time 16:29:16 )

from sqlalchemy import *
from commons.get_connexion import Base


class Synopsis(Base):
    __tablename__ = 'Synopsis'
    bookId = Column(Integer, primary_key=True, nullable=False, unique=True)
    synopsis = Column(String)

    def __init__(self, bookId='null', synopsis='null'):
        self.bookId = bookId
        self.synopsis = synopsis

    def to_dict(self):
        return {
            "bookId": self.bookId,
            "synopsis": self.synopsis,
        }
