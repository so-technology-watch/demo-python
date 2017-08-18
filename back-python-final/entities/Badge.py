# Python class for entity Badge 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class Badge(Base):
    __tablename__ = 'Badge'
    badgeNumber = Column(Integer, primary_key=True, nullable=False, unique=True)
    authorizationLevel = Column(Integer, nullable=False)
    endOfValidity = Column(Date)

    def __init__(self, badgeNumber='null', authorizationLevel='null', endOfValidity='null'):
        self.badgeNumber = badgeNumber
        self.authorizationLevel = authorizationLevel
        self.endOfValidity = endOfValidity

    def to_dict(self):
        return {
            "badgeNumber": self.badgeNumber,
            "authorizationLevel": self.authorizationLevel,
            "endOfValidity": self.endOfValidity,
        }
