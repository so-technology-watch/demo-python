from json import dumps
import commons.commons_utilitaire as commons_utilitaire
from bottle import get, post, put, delete, request, response, hook
from services import driver_service as commons_driver_service
from entities.driver import Driver

driver_service = commons_driver_service.DriverService("driver")
invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


@hook('after_request')
def init_response():
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'


@get('/api/v1/drivers')
def get_all():
    try:
        response.status = 200
        drivers = driver_service.find_all()
        list = [driver.to_dict() for driver in drivers]
        return dumps(list)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@get('/api/v1/drivers/<driver_id>')
def get_by_id(driver_id):
    try:
        response.status = 200
        driver = driver_service.find_by_id(driver_id)
        return commons_utilitaire.json_response(driver, entity_not_found)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@post('/api/v1/drivers')
def create_driver():
    try:
        response.status = 200
        driver = commons_utilitaire.get_record_from_body(request, Driver)
        result = driver_service.create(driver)
        return commons_utilitaire.json_bool_response(result)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@put('/api/v1/drivers')
def update_driver():
    try:
        response.status = 200
        driver = commons_utilitaire.get_record_from_body(request, Driver)
        result = driver_service.update(driver)
        return commons_utilitaire.json_bool_response(result)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@delete('/api/v1/drivers/<driver_id>')
def delete_driver(driver_id):
    try:
        response.status = 200
        result = driver_service.delete_by_id(driver_id)
        return commons_utilitaire.json_bool_response(result)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)
