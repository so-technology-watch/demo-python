# Python class for resource of Book 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import Book_service as CommonsEntityService
from JsonSerializer.Book_json_serializer import BookJsonSerializer
from entities.Book import Book
from resources.commons import common_resource

book_service = CommonsEntityService.BookService()
json_serializer = BookJsonSerializer()


@get('/api/v1/book')
def get_all():
    try:
        entities = book_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/book/<id>')
def get_by_id(id):
    try:
        result = book_service.find_by_id(id)      
        return common_resource.get_by_id(result, Book, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/book')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = book_service.insert(entity)
        return common_resource.create(result, json_serializer, Book)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/book/<id>')
def update(id):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.id = id
        result = book_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/book')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = book_service.save(entity)
        return common_resource.save(result, Book, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/book/<id>')
def delete(id):
    try:
        result = book_service.delete_by_id(id)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/book.count')
def count():
    try:
        result = book_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
