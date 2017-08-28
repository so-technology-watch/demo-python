# Python class for entity Publisher 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class Publisher(Base):
    __tablename__ = 'Publisher'
    __table_args__ = {'autoload': True}

    def __init__(self, code='null', countryCode='null', name='null', email='null', contact='null', city='null', zipCode='null', phone='null'):
        """
        Init the table
        """
        self.code = code
        self.countryCode = countryCode
        self.name = name
        self.email = email
        self.contact = contact
        self.city = city
        self.zipCode = zipCode
        self.phone = phone

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
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
