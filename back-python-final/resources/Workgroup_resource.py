# Python class for resource of Workgroup 
# Created on 2017-08-25 ( Time 18:18:33 )

from bottle import get, post, put, delete, response
from services import Workgroup_service as CommonsEntityService
from JsonSerializer.Workgroup_json_serializer import WorkgroupJsonSerializer
from entities.Workgroup import Workgroup
from resources.commons import common_resource

workgroup_service = CommonsEntityService.WorkgroupService()
json_serializer = WorkgroupJsonSerializer()


@get('/api/v1/workgroup')
def get_all():
    try:
        entities = workgroup_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/workgroup/<id>')
def get_by_id(id):
    try:
        result = workgroup_service.find_by_id(id)      
        return common_resource.get_by_id(result, Workgroup, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/workgroup')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = workgroup_service.insert(entity)
        return common_resource.create(result, json_serializer, Workgroup)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/workgroup/<id>')
def update(id):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.id = id
        result = workgroup_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/workgroup')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = workgroup_service.save(entity)
        return common_resource.save(result, Workgroup, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/workgroup/<id>')
def delete(id):
    try:
        result = workgroup_service.delete_by_id(id)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/workgroup.count')
def count():
    try:
        result = workgroup_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
