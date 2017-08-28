# Python class for resource of Publisher 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import Publisher_service as CommonsEntityService
from JsonSerializer.Publisher_json_serializer import PublisherJsonSerializer
from entities.Publisher import Publisher
from resources.commons import common_resource

publisher_service = CommonsEntityService.PublisherService()
json_serializer = PublisherJsonSerializer()


@get('/api/v1/publisher')
def get_all():
    try:
        entities = publisher_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/publisher/<code>')
def get_by_id(code):
    try:
        result = publisher_service.find_by_id(code)      
        return common_resource.get_by_id(result, Publisher, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/publisher')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = publisher_service.insert(entity)
        return common_resource.create(result, json_serializer, Publisher)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/publisher/<code>')
def update(code):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.code = code
        result = publisher_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/publisher')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = publisher_service.save(entity)
        return common_resource.save(result, Publisher, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/publisher/<code>')
def delete(code):
    try:
        result = publisher_service.delete_by_id(code)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/publisher.count')
def count():
    try:
        result = publisher_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
