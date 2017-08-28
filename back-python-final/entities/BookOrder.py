# Python class for entity BookOrder 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class BookOrder(Base):
    __tablename__ = 'BookOrder'
    __table_args__ = {'autoload': True}

    def __init__(self, id='null', shopCode='null', customerCode='null', employeeCode='null', date='null', state='null'):
        """
        Init the table
        """
        self.id = id
        self.shopCode = shopCode
        self.customerCode = customerCode
        self.employeeCode = employeeCode
        self.date = date
        self.state = state

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id": self.id,
            "shopCode": self.shopCode,
            "customerCode": self.customerCode,
            "employeeCode": self.employeeCode,
            "date": self.date,
            "state": self.state,
        }
