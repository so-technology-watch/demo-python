# Python class for entity Customer 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class Customer(Base):
    __tablename__ = 'Customer'
    __table_args__ = {'autoload': True}

    def __init__(self, code='null', countryCode='null', firstName='null', lastName='null', login='null', password='null', age='null', city='null', zipCode='null', phone='null', reviewer='null'):
        """
        Init the table
        """
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
        """
        :return: the class as a dictionary
        """
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
