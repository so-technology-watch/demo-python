class Car(object):
    def __init__(self, id='null', manufacturer_id='null', model='null', year='null', color='null'):
        self.id = id
        self.manufacturer_id = manufacturer_id
        self.model = model
        self.year = year
        self.color = color

    def to_dict(self):
        return {
            "id": self.id,
            "manufacturer_id": self.manufacturer_id,
            "model": self.model,
            "year": self.year,
            "color": self.color,
        }
