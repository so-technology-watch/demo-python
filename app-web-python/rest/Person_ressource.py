import commons.utility_commons as commons_utilitaire
from bottle import get, post, put, delete, request, response, hook, view, template
from services import Person_service as commons_Person_service
from entities.Person import Person
from json import dumps

Person_service = commons_Person_service.PersonService("Person")
invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


@hook('after_request')
def init_response():
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'


@get('/api/v1/Person')
def get_all():
    try:
        response.status = 200
        cars = Person_service.find_all()
        list = [car.to_dict() for car in cars]
        return dumps(list)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@get('/api/v1/Person/<id>')
def get_by_id(id):
    try:
        response.status = 200
        car = Person_service.find_by_id(id)
        return commons_utilitaire.json_response(car, entity_not_found)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@post('/api/v1/Person')
def create_car():
    try:
        response.status = 200
        car = commons_utilitaire.get_record_from_body(request, Person)
        result = Person_service.insert(car)
        return commons_utilitaire.json_bool_response(result, response)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@put('/api/v1/Person')
def update_car():
    try:
        response.status = 200
        car = commons_utilitaire.get_record_from_body(request, Person)
        result = Person_service.update(car)
        return commons_utilitaire.json_bool_response(result, response)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@delete('/api/v1/Person/<id>')
def delete_car(id):
    try:
        response.status = 200
        result = Person_service.delete_by_id(id)
        return commons_utilitaire.json_bool_response(result, response)
    except TypeError as e:
        print(e)
        return commons_utilitaire.error_handler(400, invalid_parameters, response)
