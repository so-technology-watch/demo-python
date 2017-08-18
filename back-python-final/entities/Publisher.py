# Python class for entity Publisher 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class Publisher(Base):
    __tablename__ = 'Publisher'
    code = Column(Integer, primary_key=True, nullable=False, unique=True)
    countryCode = Column(String, ForeignKey('Country.code', ondelete='RESTRICT'), nullable=False)
    name = Column(String)
    email = Column(String)
    contact = Column(String)
    city = Column(String)
    zipCode = Column(Integer)
    phone = Column(String)

    def __init__(self, code='null', countryCode='null', name='null', email='null', contact='null', city='null', zipCode='null', phone='null'):
        self.code = code
        self.countryCode = countryCode
        self.name = name
        self.email = email
        self.contact = contact
        self.city = city
        self.zipCode = zipCode
        self.phone = phone

    def to_dict(self):
        return {
            "code": self.code,
            "countryCode": self.countryCode,
            "name": self.name,
            "email": self.email,
            "contact": self.contact,
            "city": self.city,
            "zipCode": self.zipCode,
            "phone": self.phone,
        }
