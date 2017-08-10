from bottle import get, post, put, delete, request, route, response, hook
from services import Cours_service as commons_entity_service
from jsonSerializer.CoursJsonSerializer import CoursJsonSerializer
import json

cours_service = commons_entity_service.CoursService("Cours")
json_serializer = CoursJsonSerializer()


@hook('after_request')
def init_response():
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'


@route('/<>', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/<>/<>', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/<>/<>/<>', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/<>/', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/<>/<>/', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/<>/<>/<>/', method=['GET', 'POST', 'PUT', 'DELETE'])
@route('/', method=['GET', 'POST', 'PUT', 'DELETE'])
def error_400():
    response.status = 400


@get('/api/v1/cours')
def get_all():
    try:
        entities = cours_service.find_all()
        result = [json_serializer.to_json(entity) for entity in entities]
        response.status = 200
        return json.dumps(result)
    except TypeError as e:
        print(e)
        response.status = 500
        return {"error": 500, "error_description": "{}".format(e)}
 

@get('/api/v1/cours/<idCours>')
def get_by_id(idCours):
    try:
        result = cours_service.find_by_id(idCours)
        if result['code'] == 200:
            if result['entity']:
                response.status = 200
                return json_serializer.to_json(result['entity'])
            else:
                response.status = 404
        else:
            response.status = 400
    except TypeError as e:
        print(e)
        response.status = 500
        return {"error": 500, "error_description": "{}".format(e)}


@post('/api/v1/cours')
def create():
    try:
        body = request.body
        if body:
            body_str = body.read().decode('utf-8')
            entity = json_serializer.from_json(body_str)
            result = cours_service.insert(entity)
            if result['code'] == 201:
                response.status = 201
                return json_serializer.to_json(entity)
            if result['code'] == 409:
                response.status = 409
            else:
                response.status = 500
                return {"error": 500, "error_description": "{}".format(result['message'])}
        else:
            response.status = 400
    except TypeError as e:
        print(e)
        response.status = 500
        return {"error": 500, "error_description": "{}".format(e)}


@put('/api/v1/cours/<idCours>')
def update(idCours):
    try:
        body = request.body
        if body:
            body_str = body.read().decode('utf-8')
            entity = json_serializer.from_json(body_str)
            if entity.idCours == int(idCours):
                result = cours_service.update(entity)
                if result['code'] == 200:
                    response.status = 200
                    return json_serializer.to_json(result['entity'])
                if result['code'] == 201:
                    response.status = 201
                    return json_serializer.to_json(result['entity'])
                else:
                    response.status = 500
                    return {"error": 500, "error_description": "{}".format(result['message'])}
            else:
                response.status = 400
        else:
            response.status = 400
    except TypeError as e:
        print(e)
        response.status = 500
        return {"error": 500, "error_description": "{}".format(e)}


@delete('/api/v1/cours/<idCours>')
def delete(idCours):
    try:
        result = cours_service.delete_by_id(idCours)
        if result['code'] == 204:
            if result['entity']:
                response.status = 204
            else:
                response.status = 404
        else:
            response.status = 400
    except TypeError as e:
        print(e)
        response.status = 500
        return {"errorCode": 500, "message": "Internal Server Error"}


@get('/api/v1/cours.count')
def count():
    try:
        result = cours_service.count_all()
        if type(result) == int:
            response.status = 200
            return {"count": result}
        else:
            response.status = 500
            return {"error": 500, "error_description": "{}".format(result)}
    except TypeError as e:
        print(e)
        response.status = 400
