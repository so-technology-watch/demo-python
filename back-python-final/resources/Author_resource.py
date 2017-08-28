# Python class for resource of Author 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import Author_service as CommonsEntityService
from JsonSerializer.Author_json_serializer import AuthorJsonSerializer
from entities.Author import Author
from resources.commons import common_resource

author_service = CommonsEntityService.AuthorService()
json_serializer = AuthorJsonSerializer()


@get('/api/v1/author')
def get_all():
    try:
        entities = author_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/author/<id>')
def get_by_id(id):
    try:
        result = author_service.find_by_id(id)      
        return common_resource.get_by_id(result, Author, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/author')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = author_service.insert(entity)
        return common_resource.create(result, json_serializer, Author)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/author/<id>')
def update(id):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.id = id
        result = author_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/author')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = author_service.save(entity)
        return common_resource.save(result, Author, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/author/<id>')
def delete(id):
    try:
        result = author_service.delete_by_id(id)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/author.count')
def count():
    try:
        result = author_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
