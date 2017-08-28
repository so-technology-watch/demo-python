# Python class for entity Employee 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class Employee(Base):
    __tablename__ = 'Employee'
    __table_args__ = {'autoload': True}

    def __init__(self, code='null', shopCode='null', firstName='null', lastName='null', manager='null', badgeNumber='null', email='null'):
        """
        Init the table
        """
        self.code = code
        self.shopCode = shopCode
        self.firstName = firstName
        self.lastName = lastName
        self.manager = manager
        self.badgeNumber = badgeNumber
        self.email = email

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "code": self.code,
            "shopCode": self.shopCode,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "manager": self.manager,
            "badgeNumber": self.badgeNumber,
            "email": self.email,
        }
