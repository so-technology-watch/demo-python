# Python class for entity Customer 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class Customer(Base):
    __tablename__ = 'Customer'
    code = Column(String, primary_key=True, nullable=False, unique=True)
    countryCode = Column(String, ForeignKey('Country.code', ondelete='RESTRICT'), nullable=False)
    firstName = Column(String)
    lastName = Column(String)
    login = Column(String, nullable=False)
    password = Column(String)
    age = Column(Integer)
    city = Column(String)
    zipCode = Column(Integer)
    phone = Column(String)
    reviewer = Column(Integer)

    def __init__(self, code='null', countryCode='null', firstName='null', lastName='null', login='null', password='null', age='null', city='null', zipCode='null', phone='null', reviewer='null'):
        self.code = code
        self.countryCode = countryCode
        self.firstName = firstName
        self.lastName = lastName
        self.login = login
        self.password = password
        self.age = age
        self.city = city
        self.zipCode = zipCode
        self.phone = phone
        self.reviewer = reviewer

    def to_dict(self):
        return {
            "code": self.code,
            "countryCode": self.countryCode,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "login": self.login,
            "password": self.password,
            "age": self.age,
            "city": self.city,
            "zipCode": self.zipCode,
            "phone": self.phone,
            "reviewer": self.reviewer,
        }
