# Python class for resource of BookOrderItem 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import BookOrderItem_service as CommonsEntityService
from JsonSerializer.BookOrderItem_json_serializer import BookOrderItemJsonSerializer
from entities.BookOrderItem import BookOrderItem
from resources.commons import common_resource

bookorderitem_service = CommonsEntityService.BookOrderItemService()
json_serializer = BookOrderItemJsonSerializer()


@get('/api/v1/bookorderitem')
def get_all():
    try:
        entities = bookorderitem_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/bookorderitem/<bookOrderId>/<bookId>')
def get_by_id(bookOrderId, bookId):
    try:
        result = bookorderitem_service.find_by_id(bookOrderId, bookId)      
        return common_resource.get_by_id(result, BookOrderItem, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/bookorderitem')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = bookorderitem_service.insert(entity)
        return common_resource.create(result, json_serializer, BookOrderItem)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/bookorderitem/<bookOrderId>/<bookId>')
def update(bookOrderId, bookId):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.bookOrderId = bookOrderId
        entity.bookId = bookId
        result = bookorderitem_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/bookorderitem')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = bookorderitem_service.save(entity)
        return common_resource.save(result, BookOrderItem, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/bookorderitem/<bookOrderId>/<bookId>')
def delete(bookOrderId, bookId):
    try:
        result = bookorderitem_service.delete_by_id(bookOrderId, bookId)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/bookorderitem.count')
def count():
    try:
        result = bookorderitem_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
