# Python class for entity Workgroup 
# Created on 2017-08-18 ( Time 16:29:16 )

from sqlalchemy import *
from commons.get_connexion import Base


class Workgroup(Base):
    __tablename__ = 'Workgroup'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    creationDate = Column(Date, nullable=False)

    def __init__(self, id='null', name='null', description='null', creationDate='null'):
        self.id = id
        self.name = name
        self.description = description
        self.creationDate = creationDate

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "creationDate": self.creationDate,
        }
