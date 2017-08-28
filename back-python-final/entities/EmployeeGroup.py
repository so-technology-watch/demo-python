# Python class for entity EmployeeGroup 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class EmployeeGroup(Base):
    __tablename__ = 'EmployeeGroup'
    __table_args__ = {'autoload': True}

    def __init__(self, employeeCode='null', groupId='null'):
        """
        Init the table
        """
        self.employeeCode = employeeCode
        self.groupId = groupId

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "employeeCode": self.employeeCode,
            "groupId": self.groupId,
        }
