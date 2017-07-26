import commons.utility_commons as commons_utilitaire
from bottle import get, post, put, delete, request, response, hook
from services import Car_service as commons_Car_service
from entities.Car import Car
from json import dumps

car_service = commons_Car_service.CarService("Car")
invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


@hook('after_request')
def init_response():
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'


@get('/api/v1/Car')
def get_all():
    try:
        response.status = 200
        cars = car_service.find_all()
        list = [car.to_dict() for car in cars]
        return dumps(list)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@get('/api/v1/Car/<id>')
def get_by_id(id):
    try:
        response.status = 200
        car = car_service.find_by_id(id)
        return commons_utilitaire.json_response(car, entity_not_found)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@post('/api/v1/Car')
def create_car():
    try:
        response.status = 200
        car = commons_utilitaire.get_record_from_body(request, Car)
        result = car_service.insert(car)
        return commons_utilitaire.json_error(result, response)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(500, "Can't create this", response)


@put('/api/v1/Car')
def update_car():
    try:
        response.status = 200
        entity = commons_utilitaire.get_record_from_body(request, Car)
        result = car_service.update(entity)
        return commons_utilitaire.json_bool_response(result)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(500, "Something went wrong : an argument doesn't exist", response)


@delete('/api/v1/Car/<id>')
def delete_car(id):
    try:
        response.status = 200
        result = car_service.delete_by_id(id)
        return commons_utilitaire.json_bool_response(result)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(500, "Can't delete this : link to another entity", response)
