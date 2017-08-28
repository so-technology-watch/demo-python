# Python class for resource of Employee 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import Employee_service as CommonsEntityService
from JsonSerializer.Employee_json_serializer import EmployeeJsonSerializer
from entities.Employee import Employee
from resources.commons import common_resource

employee_service = CommonsEntityService.EmployeeService()
json_serializer = EmployeeJsonSerializer()


@get('/api/v1/employee')
def get_all():
    try:
        entities = employee_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/employee/<code>')
def get_by_id(code):
    try:
        result = employee_service.find_by_id(code)      
        return common_resource.get_by_id(result, Employee, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/employee')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = employee_service.insert(entity)
        return common_resource.create(result, json_serializer, Employee)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/employee/<code>')
def update(code):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.code = code
        result = employee_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/employee')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = employee_service.save(entity)
        return common_resource.save(result, Employee, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/employee/<code>')
def delete(code):
    try:
        result = employee_service.delete_by_id(code)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/employee.count')
def count():
    try:
        result = employee_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
