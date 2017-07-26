import commons.utility_commons as commons_utilitaire
from bottle import get, post, put, delete, request, response, hook, error
from services import Manufacturer_service as commons_Manufacturer_service
from entities.Manufacturer import Manufacturer
from json import dumps

Manufacturer_service = commons_Manufacturer_service.ManufacturerService("Manufacturer")
invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


@hook('after_request')
def init_response():
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'


@error(500)
def error500():
    return commons_utilitaire.error_handler(500, invalid_parameters, response)


@get('/api/v1/Manufacturer')
def get_all():
    try:
        response.status = 200
        entity = Manufacturer_service.find_all()
        list = [_entity.to_dict() for _entity in entity]
        return dumps(list)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@get('/api/v1/Manufacturer/<id>')
def get_by_id(id):
    try:
        response.status = 200
        entity = Manufacturer_service.find_by_id(id)
        return commons_utilitaire.json_response(entity, entity_not_found)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@post('/api/v1/Manufacturer')
def create_entity():
    try:
        response.status = 200
        entity = commons_utilitaire.get_record_from_body(request, Manufacturer)
        result = Manufacturer_service.insert(entity)
        return commons_utilitaire.json_bool_response(result, response)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@put('/api/v1/Manufacturer')
def update_entity():
    try:
        response.status = 200
        entity = commons_utilitaire.get_record_from_body(request, Manufacturer)
        result = Manufacturer_service.update(entity)
        return commons_utilitaire.json_bool_response(result, response)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@delete('/api/v1/Manufacturer/<id>')
def delete_entity(id):
    try:
        response.status = 200
        result = Manufacturer_service.delete_by_id(id)
        return commons_utilitaire.json_bool_response(result, response)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)
