class Driver(object):
    def __init__(self, person_id='null', car_id='null', licence_number='null', licence_date='null'):
        self.person_id = person_id
        self.car_id = car_id
        self.licence_number = licence_number
        self.licence_date = licence_date

    def to_dict(self):
        return {
            "person_id": self.person_id,
            "car_id": self.car_id,
            "licence_number": self.licence_number,
            "licence_date": self.licence_date,
        }
