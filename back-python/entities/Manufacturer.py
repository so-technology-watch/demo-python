class Manufacturer(object):
    def __init__(self, id='null', name='null'):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
