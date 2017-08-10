# Python class for entity Note 
# Created on 2017-08-10 ( Time 11:31:49 )

from sqlalchemy import *
from commons.get_connexion import Base


class Note(Base):
    __tablename__ = 'Note'

    idCours = Column(Integer, ForeignKey('Cours.idCours', ondelete="RESTRICT"), primary_key=True, nullable=False)
    idEleve = Column(Integer, ForeignKey('Eleve.idEleve', ondelete="RESTRICT"), primary_key=True, nullable=False)
    noteObtenue = Column(Integer, nullable=False)
    dateExamen = Column(Date, nullable=False)
    codeMention = Column(Integer, ForeignKey('Typemention.idMention', ondelete="RESTRICT"))

    def __init__(self, idCours='null', idEleve='null', noteObtenue='null', dateExamen='null', codeMention='null'):
        self.idCours = idCours
        self.idEleve = idEleve
        self.noteObtenue = noteObtenue
        self.dateExamen = dateExamen
        self.codeMention = codeMention

    def to_dict(self):
        return {
            "idCours": self.idCours,
            "idEleve": self.idEleve,
            "noteObtenue": self.noteObtenue,
            "dateExamen": self.dateExamen,
            "codeMention": self.codeMention,
        }
