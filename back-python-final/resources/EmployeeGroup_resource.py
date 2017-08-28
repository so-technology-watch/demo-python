# Python class for resource of EmployeeGroup 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import EmployeeGroup_service as CommonsEntityService
from JsonSerializer.EmployeeGroup_json_serializer import EmployeeGroupJsonSerializer
from entities.EmployeeGroup import EmployeeGroup
from resources.commons import common_resource

employeegroup_service = CommonsEntityService.EmployeeGroupService()
json_serializer = EmployeeGroupJsonSerializer()


@get('/api/v1/employeegroup')
def get_all():
    try:
        entities = employeegroup_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/employeegroup/<employeeCode>/<groupId>')
def get_by_id(employeeCode, groupId):
    try:
        result = employeegroup_service.find_by_id(employeeCode, groupId)      
        return common_resource.get_by_id(result, EmployeeGroup, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/employeegroup')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = employeegroup_service.insert(entity)
        return common_resource.create(result, json_serializer, EmployeeGroup)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/employeegroup/<employeeCode>/<groupId>')
def update(employeeCode, groupId):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.employeeCode = employeeCode
        entity.groupId = groupId
        result = employeegroup_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/employeegroup')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = employeegroup_service.save(entity)
        return common_resource.save(result, EmployeeGroup, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/employeegroup/<employeeCode>/<groupId>')
def delete(employeeCode, groupId):
    try:
        result = employeegroup_service.delete_by_id(employeeCode, groupId)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/employeegroup.count')
def count():
    try:
        result = employeegroup_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
