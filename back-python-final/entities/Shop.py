# Python class for entity Shop 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class Shop(Base):
    __tablename__ = 'Shop'
    __table_args__ = {'autoload': True}

    def __init__(self, code='null', name='null', address1='null', address2='null', zipCode='null', city='null', countryCode='null', phone='null', email='null', executive='null'):
        """
        Init the table
        """
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
        """
        :return: the class as a dictionary
        """
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
