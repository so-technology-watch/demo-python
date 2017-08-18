# Python class for entity Employee 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class Employee(Base):
    __tablename__ = 'Employee'
    code = Column(String, primary_key=True, nullable=False, unique=True)
    shopCode = Column(String, ForeignKey('Shop.code', ondelete='RESTRICT'), nullable=False)
    firstName = Column(String)
    lastName = Column(String, nullable=False)
    manager = Column(Integer)
    badgeNumber = Column(Integer, ForeignKey('Badge.badgeNumber', ondelete='RESTRICT'))
    email = Column(String)

    def __init__(self, code='null', shopCode='null', firstName='null', lastName='null', manager='null', badgeNumber='null', email='null'):
        self.code = code
        self.shopCode = shopCode
        self.firstName = firstName
        self.lastName = lastName
        self.manager = manager
        self.badgeNumber = badgeNumber
        self.email = email

    def to_dict(self):
        return {
            "code": self.code,
            "shopCode": self.shopCode,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "manager": self.manager,
            "badgeNumber": self.badgeNumber,
            "email": self.email,
        }
