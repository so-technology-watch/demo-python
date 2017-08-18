# Python class for entity Country 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class Country(Base):
    __tablename__ = 'Country'
    code = Column(String, primary_key=True, nullable=False, unique=True)
    name = Column(String)

    def __init__(self, code='null', name='null'):
        self.code = code
        self.name = name

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
        }
