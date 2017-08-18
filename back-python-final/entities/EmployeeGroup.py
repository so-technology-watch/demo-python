# Python class for entity EmployeeGroup 
# Created on 2017-08-18 ( Time 16:29:15 )

from sqlalchemy import *
from commons.get_connexion import Base


class EmployeeGroup(Base):
    __tablename__ = 'EmployeeGroup'
    employeeCode = Column(String, ForeignKey('Employee.code'), primary_key=True, nullable=False)
    groupId = Column(Integer, ForeignKey('Workgroup.id'), primary_key=True, nullable=False)

    def __init__(self, employeeCode='null', groupId='null'):
        self.employeeCode = employeeCode
        self.groupId = groupId

    def to_dict(self):
        return {
            "employeeCode": self.employeeCode,
            "groupId": self.groupId,
        }
