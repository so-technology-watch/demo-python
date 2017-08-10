# Python class for entity Typemention 
# Created on 2017-08-10 ( Time 11:31:49 )

from sqlalchemy import *
from commons.get_connexion import Base


class Typemention(Base):
    __tablename__ = 'Typemention'

    idMention = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    labelMention = Column(String, nullable=False)

    def __init__(self, idMention='null', labelMention='null'):
        self.idMention = idMention
        self.labelMention = labelMention

    def to_dict(self):
        return {
            "idMention": self.idMention,
            "labelMention": self.labelMention,
        }
