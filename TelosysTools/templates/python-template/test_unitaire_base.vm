from sqlalchemy import *
from commons.get_connexion import Base


class TestDao(Base):
    __tablename__ = 'TestDao'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __init__(self, id='null', name='null'):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }