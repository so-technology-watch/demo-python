# Python class for resource of Synopsis 
# Created on 2017-08-25 ( Time 18:18:33 )

from bottle import get, post, put, delete, response
from services import Synopsis_service as CommonsEntityService
from JsonSerializer.Synopsis_json_serializer import SynopsisJsonSerializer
from entities.Synopsis import Synopsis
from resources.commons import common_resource

synopsis_service = CommonsEntityService.SynopsisService()
json_serializer = SynopsisJsonSerializer()


@get('/api/v1/synopsis')
def get_all():
    try:
        entities = synopsis_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/synopsis/<bookId>')
def get_by_id(bookId):
    try:
        result = synopsis_service.find_by_id(bookId)      
        return common_resource.get_by_id(result, Synopsis, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/synopsis')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = synopsis_service.insert(entity)
        return common_resource.create(result, json_serializer, Synopsis)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/synopsis/<bookId>')
def update(bookId):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.bookId = bookId
        result = synopsis_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/synopsis')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = synopsis_service.save(entity)
        return common_resource.save(result, Synopsis, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/synopsis/<bookId>')
def delete(bookId):
    try:
        result = synopsis_service.delete_by_id(bookId)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/synopsis.count')
def count():
    try:
        result = synopsis_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
