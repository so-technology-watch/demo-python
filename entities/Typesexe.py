# Python class for entity Typesexe 
# Created on 2017-08-10 ( Time 11:31:49 )

from sqlalchemy import *
from commons.get_connexion import Base


class Typesexe(Base):
    __tablename__ = 'Typesexe'

    idSexe = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    labelSexe = Column(String, nullable=False)

    def __init__(self, idSexe='null', labelSexe='null'):
        self.idSexe = idSexe
        self.labelSexe = labelSexe

    def to_dict(self):
        return {
            "idSexe": self.idSexe,
            "labelSexe": self.labelSexe,
        }
