# Python class for entity Badge 
# Created on 2017-08-25 ( Time 18:18:32 )

from commons.get_connection import Base


class Badge(Base):
    __tablename__ = 'Badge'
    __table_args__ = {'autoload': True}

    def __init__(self, badgeNumber='null', authorizationLevel='null', endOfValidity='null'):
        """
        Init the table
        """
        self.badgeNumber = badgeNumber
        self.authorizationLevel = authorizationLevel
        self.endOfValidity = endOfValidity

    def to_dict(self):
        """
        :return: the class as a dictionary
        """
        return {
            "badgeNumber": self.badgeNumber,
            "authorizationLevel": self.authorizationLevel,
            "endOfValidity": self.endOfValidity,
        }
