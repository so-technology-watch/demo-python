# Python class for entity Cours 
# Created on 2017-08-10 ( Time 11:31:48 )

from sqlalchemy import *
from commons.get_connexion import Base


class Cours(Base):
    __tablename__ = 'Cours'

    idCours = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    libelle = Column(String)
    nbHeures = Column(Integer)

    def __init__(self, idCours='null', libelle='null', nbHeures='null'):
        self.idCours = idCours
        self.libelle = libelle
        self.nbHeures = nbHeures

    def to_dict(self):
        return {
            "idCours": self.idCours,
            "libelle": self.libelle,
            "nbHeures": self.nbHeures,
        }
