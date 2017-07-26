from json import dumps
import commons.utility_commons as commons_utilitaire
from bottle import get, post, put, delete, request, response, hook
from services import Driver_service as commons_Driver_service
from entities.Driver import Driver

Driver_service = commons_Driver_service.DriverService("Driver")
invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


@hook('after_request')
def init_response():
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'


@get('/api/v1/Driver')
def get_all():
    try:
        response.status = 200
        drivers = Driver_service.find_all()
        list = [driver.to_dict() for driver in drivers]
        return dumps(list)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@get('/api/v1/Driver/<person_id>/<car_id>')
def get_by_id(person_id, car_id):
    try:
        response.status = 200
        driver = Driver_service.find_by_id(person_id, car_id)
        return commons_utilitaire.json_response(driver, entity_not_found)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@post('/api/v1/Driver')
def create_driver():
    try:
        response.status = 200
        driver = commons_utilitaire.get_record_from_body(request, Driver)
        result = Driver_service.insert(driver)
        return commons_utilitaire.json_bool_response(result, response)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@put('/api/v1/Driver')
def update_driver():
    try:
        response.status = 200
        driver = commons_utilitaire.get_record_from_body(request, Driver)
        result = Driver_service.update(driver)
        return commons_utilitaire.json_bool_response(result, response)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@delete('/api/v1/Driver/<person_id>/<car_id>')
def delete_driver(person_id, car_id):
    try:
        response.status = 200
        result = Driver_service.delete_by_id(person_id, car_id)
        return commons_utilitaire.json_bool_response(result, response)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)
