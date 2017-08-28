# Python class for entity Workgroup 
# Created on 2017-08-25 ( Time 18:18:33 )

from commons.get_connection import Base


class Workgroup(Base):
    __tablename__ = 'Workgroup'
    __table_args__ = {'autoload': True}

    def __init__(self, id='null', name='null', description='null', creationDate='null'):
        """
        Init the table
        """
        self.id = id
        self.name = name
        self.description = description
        self.creationDate = creationDate

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "creationDate": self.creationDate,
        }
