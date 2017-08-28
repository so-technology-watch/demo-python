# Python class for resource of Customer 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import Customer_service as CommonsEntityService
from JsonSerializer.Customer_json_serializer import CustomerJsonSerializer
from entities.Customer import Customer
from resources.commons import common_resource

customer_service = CommonsEntityService.CustomerService()
json_serializer = CustomerJsonSerializer()


@get('/api/v1/customer')
def get_all():
    try:
        entities = customer_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/customer/<code>')
def get_by_id(code):
    try:
        result = customer_service.find_by_id(code)      
        return common_resource.get_by_id(result, Customer, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/customer')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = customer_service.insert(entity)
        return common_resource.create(result, json_serializer, Customer)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/customer/<code>')
def update(code):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.code = code
        result = customer_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/customer')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = customer_service.save(entity)
        return common_resource.save(result, Customer, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/customer/<code>')
def delete(code):
    try:
        result = customer_service.delete_by_id(code)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/customer.count')
def count():
    try:
        result = customer_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
