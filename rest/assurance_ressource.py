import persistence.assurance_persistence as commons_assurance_service
import commons.commons_utilitaire as commons_utilitaire
from bottle import get, post, put, delete, request, response, hook
from json import dumps
from entities.assurance import Assurance

assurance_service = commons_assurance_service.AssurancePersistence(Assurance)
invalid_parameters = "Invalid parameters"


@get('/api/v1/assurances')
def get_all():
    response.status = 200
    assurances = assurance_service.find_all()
    if assurances is None:
        response.status = 404
    return dumps(assurances, default=commons_utilitaire.jdefault)


@get('/api/v1/assurances/<assurance_id>')
def get_by_id(assurance_id):
    response.status = 200
    assurance = assurance_service.find_by_id(assurance_id)
    if assurance is None:
        response.status = 404
    return dumps(assurance, default=commons_utilitaire.jdefault)


@post('/api/v1/assurances')
def create_assurance():
    try:
        assurance = commons_utilitaire.get_record_from_body(request, Assurance)
        response.status = 201
        return dumps(commons_assurance_service.create(assurance), default=commons_utilitaire.jdefault)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)


@put('/api/v1/assurances')
def update_assurance():
    try:
        response.status = 200
        assurance = commons_utilitaire.get_record_from_body(request, Assurance)
        result = commons_assurance_service.update(assurance)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)
    if not result:
        return commons_utilitaire.error_handler(404, "identifiant not find", response)


@delete('/api/v1/assurances/<assurance_id>')
def delete_assurance(assurance_id):
    try:
        response.status = 200
        result = commons_assurance_service.delete_by_id(assurance_id)
    except TypeError:
        return commons_utilitaire.error_handler(400, invalid_parameters, response)
    if not result:
        return commons_utilitaire.error_handler(404, "identifiant not find", response)