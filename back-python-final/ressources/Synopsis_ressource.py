from bottle import get, post, put, delete, request, route, response, hook
from services import Synopsis_service as commons_entity_service
from jsonSerializer.SynopsisJsonSerializer import SynopsisJsonSerializer
from entities.Synopsis import Synopsis
import json

synopsis_service = commons_entity_service.SynopsisService("Synopsis")
json_serializer = SynopsisJsonSerializer()


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


@get('/api/v1/synopsis')
def get_all():
    try:
        entities = synopsis_service.find_all()
        result = [json_serializer.to_json(entity) for entity in entities]
        response.status = 200
        return json.dumps(result)
    except TypeError as e:
        print(e)
        response.status = 500
        return {"error": 500, "error_description": "{}".format(e)}
 

@get('/api/v1/synopsis/<bookId>')
def get_by_id(bookId):
    try:
        result = synopsis_service.find_by_id(bookId)
        if result:
            if type(result) == Synopsis:
                response.status = 200
                return json_serializer.to_json(result)
            else:
                response.status = 500
                return {"error": 500, "error_description": "{}".format(result)}
        else:
            response.status = 404
    except TypeError as e:
        print(e)
        response.status = 500
        return {"error": 500, "error_description": "{}".format(e)}


@post('/api/v1/synopsis')
def create():
    try:
        body = request.body
        if body:
            body_str = body.read().decode('utf-8')
            entity = json_serializer.from_json(body_str)
            result = synopsis_service.insert(entity)
            if result:
                if type(result) == Synopsis:
                    response.status = 201
                    return json_serializer.to_json(result)
                else:
                    response.status = 500
                    return {"error": 500, "error_description": "{}".format(result)}
            else:
                response.status = 409
        else:
            response.status = 400
    except TypeError as e:
        print(e)
        response.status = 500
        return {"error": 500, "error_description": "{}".format(e)}


@put('/api/v1/synopsis/<bookId>')
def update(bookId):
    try:
        body = request.body
        body_str = body.read().decode('utf-8')
        entity = json_serializer.from_json(body_str)
        if entity.bookId == int(bookId):
            result = synopsis_service.update(entity)
            if result:
                if type(result) == int and result > 0:
                    response.status = 200
                else:
                    response.status = 500
                    return {"error": 500, "error_description": "{}".format(result)}
            else:
                response.status = 404
        else:
            response.status = 400
    except TypeError as e:
        print(e)
        response.status = 500
        return {"error": 500, "error_description": "{}".format(e)}


@put('/api/v1/synopsis/')
def save():
    try:
        body = request.body
        body_str = body.read().decode('utf-8')
        entity = json_serializer.from_json(body_str)
        result = synopsis_service.save(entity)
        if type(result) == Synopsis:
            response.status = 201
            return json_serializer.to_json(result)
        if type(result) == int and result > 0:
            response.status = 200
            return json_serializer.to_json(entity)
        else:
            response.status = 500
            return {"error": 500, "error_description": "{}".format(result)}
    except TypeError as e:
        print(e)
        response.status = 500
        return {"error": 500, "error_description": "{}".format(e)}


@delete('/api/v1/synopsis/<bookId>')
def delete(bookId):
    try:
        result = synopsis_service.delete_by_id(bookId)
        if result:
            if type(result) == int and result > 0:
                response.status = 204
            else:
                response.status = 500
                return {"errorCode": 500, "error_description": "{}".format(result)}
        else:
            response.status = 404
    except TypeError as e:
        print(e)
        response.status = 500
        return {"errorCode": 500, "error_description": "{}".format(e)}


@get('/api/v1/synopsis.count')
def count():
    try:
        result = synopsis_service.count_all()
        if type(result) == int:
            response.status = 200
            return {"count": result}
        else:
            response.status = 500
            return {"error": 500, "error_description": "{}".format(result)}
    except TypeError as e:
        print(e)
        response.status = 400
