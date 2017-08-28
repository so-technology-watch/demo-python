# Python class for resource of BookOrder 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import BookOrder_service as CommonsEntityService
from JsonSerializer.BookOrder_json_serializer import BookOrderJsonSerializer
from entities.BookOrder import BookOrder
from resources.commons import common_resource

bookorder_service = CommonsEntityService.BookOrderService()
json_serializer = BookOrderJsonSerializer()


@get('/api/v1/bookorder')
def get_all():
    try:
        entities = bookorder_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/bookorder/<id>')
def get_by_id(id):
    try:
        result = bookorder_service.find_by_id(id)      
        return common_resource.get_by_id(result, BookOrder, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/bookorder')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = bookorder_service.insert(entity)
        return common_resource.create(result, json_serializer, BookOrder)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/bookorder/<id>')
def update(id):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.id = id
        result = bookorder_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/bookorder')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = bookorder_service.save(entity)
        return common_resource.save(result, BookOrder, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/bookorder/<id>')
def delete(id):
    try:
        result = bookorder_service.delete_by_id(id)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/bookorder.count')
def count():
    try:
        result = bookorder_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
