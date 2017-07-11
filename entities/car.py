
class Car(object):
    def __init__(self, car_id='null', car_name='null', driver_id='null'):
        self.car_id = car_id
        self.car_name = car_name
        self.driver_id = driver_id

    def to_dict(self):
        return {
            "car_id": self.car_id,
            "car_name": self.car_name,
            "driver_id": self.driver_id
        }
