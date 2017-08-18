# Python class for entity Shop 
# Created on 2017-08-18 ( Time 16:29:16 )

from sqlalchemy import *
from commons.get_connexion import Base


class Shop(Base):
    __tablename__ = 'Shop'
    code = Column(String, primary_key=True, nullable=False, unique=True)
    name = Column(String)
    address1 = Column(String)
    address2 = Column(String)
    zipCode = Column(Integer)
    city = Column(String)
    countryCode = Column(String, ForeignKey('Country.code', ondelete='RESTRICT'), nullable=False)
    phone = Column(String)
    email = Column(String)
    executive = Column(String, ForeignKey('Employee.code', ondelete='RESTRICT'))

    def __init__(self, code='null', name='null', address1='null', address2='null', zipCode='null', city='null', countryCode='null', phone='null', email='null', executive='null'):
        self.code = code
        self.name = name
        self.address1 = address1
        self.address2 = address2
        self.zipCode = zipCode
        self.city = city
        self.countryCode = countryCode
        self.phone = phone
        self.email = email
        self.executive = executive

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "address1": self.address1,
            "address2": self.address2,
            "zipCode": self.zipCode,
            "city": self.city,
            "countryCode": self.countryCode,
            "phone": self.phone,
            "email": self.email,
            "executive": self.executive,
        }
