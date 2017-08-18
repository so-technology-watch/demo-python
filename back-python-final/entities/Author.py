# Python class for entity Author 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class Author(Base):
    __tablename__ = 'Author'
    id = Column(Integer, primary_key=True, unique=True)
    firstName = Column(String)
    lastName = Column(String)

    def __init__(self, id='null', firstName='null', lastName='null'):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName

    def to_dict(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
        }
