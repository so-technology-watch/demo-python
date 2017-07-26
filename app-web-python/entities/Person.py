class Person(object):
    def __init__(self, id='null', firstname='null', lastname='null', birthdate='null'):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "birthdate": self.birthdate,
        }
