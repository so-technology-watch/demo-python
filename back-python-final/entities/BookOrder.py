# Python class for entity BookOrder 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class BookOrder(Base):
    __tablename__ = 'BookOrder'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    shopCode = Column(String, ForeignKey('Shop.code', ondelete='RESTRICT'), nullable=False)
    customerCode = Column(String, ForeignKey('Customer.code', ondelete='RESTRICT'), nullable=False)
    employeeCode = Column(String, ForeignKey('Employee.code', ondelete='RESTRICT'), nullable=False)
    date = Column(Date)
    state = Column(Integer)

    def __init__(self, id='null', shopCode='null', customerCode='null', employeeCode='null', date='null', state='null'):
        self.id = id
        self.shopCode = shopCode
        self.customerCode = customerCode
        self.employeeCode = employeeCode
        self.date = date
        self.state = state

    def to_dict(self):
        return {
            "id": self.id,
            "shopCode": self.shopCode,
            "customerCode": self.customerCode,
            "employeeCode": self.employeeCode,
            "date": self.date,
            "state": self.state,
        }
