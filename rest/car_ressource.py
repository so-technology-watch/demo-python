import commons.commons_utilitaire as commons_utilitaire
from bottle import get, post, put, delete, request, response, hook, view, template
from services import car_service as commons_car_service
from entities.car import Car
from json import dumps
import bottle

car_service = commons_car_service.CarService("car")
invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


@hook('after_request')
def init_response():
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'


@get('/api/v1/cars')
def get_all():
    try:
        response.status = 200
        cars = car_service.find_all()
        list = [car.to_dict() for car in cars]
        return dumps(list)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@get('/api/v1/cars/<car_id>')
def get_by_id(car_id):
    try:
        response.status = 200
        car = car_service.find_by_id(car_id)
        return commons_utilitaire.json_response(car, entity_not_found)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@post('/api/v1/cars')
def create_car():
    try:
        response.status = 200
        car = commons_utilitaire.get_record_from_body(request, Car)
        result = car_service.create(car)
        return commons_utilitaire.json_bool_response(result)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@put('/api/v1/cars')
def update_car():
    try:
        response.status = 200
        car = commons_utilitaire.get_record_from_body(request, Car)
        result = car_service.update(car)
        return commons_utilitaire.json_bool_response(result)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@delete('/api/v1/cars/<car_id>')
def delete_car(car_id):
    try:
        response.status = 200
        result = car_service.delete_by_id(car_id)
        return commons_utilitaire.json_bool_response(result)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)
