# Python class for resource of Country 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import Country_service as CommonsEntityService
from JsonSerializer.Country_json_serializer import CountryJsonSerializer
from entities.Country import Country
from resources.commons import common_resource

country_service = CommonsEntityService.CountryService()
json_serializer = CountryJsonSerializer()


@get('/api/v1/country')
def get_all():
    try:
        entities = country_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/country/<code>')
def get_by_id(code):
    try:
        result = country_service.find_by_id(code)      
        return common_resource.get_by_id(result, Country, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/country')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = country_service.insert(entity)
        return common_resource.create(result, json_serializer, Country)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/country/<code>')
def update(code):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.code = code
        result = country_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/country')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = country_service.save(entity)
        return common_resource.save(result, Country, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/country/<code>')
def delete(code):
    try:
        result = country_service.delete_by_id(code)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/country.count')
def count():
    try:
        result = country_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
