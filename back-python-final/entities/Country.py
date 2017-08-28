# Python class for entity Country 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class Country(Base):
    __tablename__ = 'Country'
    __table_args__ = {'autoload': True}

    def __init__(self, code='null', name='null'):
        """
        Init the table
        """
        self.code = code
        self.name = name

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "code": self.code,
            "name": self.name,
        }
