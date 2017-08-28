# Python class for entity Author 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class Author(Base):
    __tablename__ = 'Author'
    __table_args__ = {'autoload': True}

    def __init__(self, id='null', firstName='null', lastName='null'):
        """
        Init the table
        """
        self.id = id
        self.firstName = firstName
        self.lastName = lastName

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
        }
