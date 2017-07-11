
class Driver(object):
    def __init__(self, driver_id='null', driver_name='null'):
        self.driver_id = driver_id
        self.driver_name = driver_name

    def to_dict(self):
        return {
            "driver_id": self.driver_id,
            "driver_name": self.driver_name
        }
