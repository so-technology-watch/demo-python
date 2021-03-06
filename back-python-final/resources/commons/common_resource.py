# Python class for commons resources 
# Created on 2017-08-25 ( Time 18:18:33 )

from bottle import route, response, hook, request
import json


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


def error_500(e):
    print(e)
    response.status = 500
    return {"error": 500, "error_description": "{}".format(e)}


def get_all(json_serializer, entities):
    result = [json_serializer.to_json(entity) for entity in entities]
    response.status = 200
    response.body = json.dumps(result)
    return response.body


def get_by_id(result, entity_class, json_serializer):
    if result:
        if type(result) == entity_class:
            response.status = 200
            return json_serializer.to_json(result)
        else:
            return error_500(result)
    else:
        response.status = 404


def create(result, json_serializer, entity_class):
    if result:
        if type(result) == entity_class:
            response.status = 201
            return json_serializer.to_json(result)
        else:
            return error_500(result)
    else:
        response.status = 409


def update(result):
    if result:
        if type(result) == int and result > 0:
            response.status = 200
        else:
            response.status = 500
            return {"error": 500, "error_description": "{}".format(result)}
    else:
        response.status = 404


def save(result, entity_class, json_serializer, entity):
    if type(result['entity']) == entity_class and result['isNew']:
        response.status = 201
        return json_serializer.to_json(result['entity'])
    elif type(result['entity']) == entity_class and not result['isNew']:
        response.status = 200
        return json_serializer.to_json(entity)
    else:
        response.status = 500
        return {"error": 500, "error_description": "{}".format(result['entity'])}


def delete(result):
    if result:
        if type(result) == int and result > 0:
            response.status = 204
        else:
            error_500(result)
    else:
        response.status = 404


def count(result):
    if type(result) == int:
        response.status = 200
        return {"count": result}
    else:
        error_500(result)


def body_from_json(json_serializer):
    body = request.body
    if body:
        body_str = body.read().decode('utf-8')
        return json_serializer.from_json(body_str)
    else:
        response.status = 400

