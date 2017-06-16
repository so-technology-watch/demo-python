import persistence.car_persistence as commons_car_service
import commons.commons_utilitaire as commons_utilitaire
from bottle import get, post, put, delete, request, response, hook, run
from json import dumps
from entities.car import Car

car_service = commons_car_service.CarPersistence(Car)
invalid_parameters = "Invalid parameters"


@get('/api/v1/cars')
def get_all():
    response.status = 200
    cars = car_service.find_all()
    if cars is None:
        response.status = 404
    return dumps(cars, default=commons_utilitaire.jdefault)


@get('/api/v1/cars/<car_id>')
def get_by_id(car_id):
    response.status = 200
    car = car_service.find_by_id(car_id)
    if car is None:
        response.status = 404
    return dumps(car, default=commons_utilitaire.jdefault)


@post('/api/v1/cars')
def create_car():
    try:
        car = commons_utilitaire.get_record_from_body(request, Car)
        response.status = 201
        return dumps(commons_car_service.create(car), default=commons_utilitaire.jdefault)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@put('/api/v1/cars')
def update_car():
    try:
        response.status = 200
        car = commons_utilitaire.get_record_from_body(request, Car)
        result = commons_car_service.update(car)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)
    if not result:
        return commons_utilitaire.error_handler(404, "identifiant not find", response)


@delete('/api/v1/cars/<car_id>')
def delete_car(car_id):
    try:
        response.status = 200
        result = commons_car_service.delete_by_id(car_id)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)
    if not result:
        return commons_utilitaire.error_handler(404, "identifiant not find", response)