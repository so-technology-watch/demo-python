# Python class for entity Eleve 
# Created on 2017-08-10 ( Time 11:31:49 )

from sqlalchemy import *
from commons.get_connexion import Base


class Eleve(Base):
    __tablename__ = 'Eleve'

    idEleve = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    nom = Column(String, nullable=False)
    prenom = Column(String)
    email = Column(String, nullable=False)
    password = Column(String)
    codePostal = Column(String)
    genre = Column(Integer, ForeignKey('Typesexe.idSexe', ondelete="RESTRICT"), nullable=False)
    dateInscription = Column(Date)

    def __init__(self, idEleve='null', nom='null', prenom='null', email='null', password='null', codePostal='null', genre='null', dateInscription='null'):
        self.idEleve = idEleve
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.password = password
        self.codePostal = codePostal
        self.genre = genre
        self.dateInscription = dateInscription

    def to_dict(self):
        return {
            "idEleve": self.idEleve,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "password": self.password,
            "codePostal": self.codePostal,
            "genre": self.genre,
            "dateInscription": self.dateInscription,
        }
