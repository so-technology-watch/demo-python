# Python class for resource of Badge 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import Badge_service as CommonsEntityService
from JsonSerializer.Badge_json_serializer import BadgeJsonSerializer
from entities.Badge import Badge
from resources.commons import common_resource

badge_service = CommonsEntityService.BadgeService()
json_serializer = BadgeJsonSerializer()


@get('/api/v1/badge')
def get_all():
    try:
        entities = badge_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/badge/<badgeNumber>')
def get_by_id(badgeNumber):
    try:
        result = badge_service.find_by_id(badgeNumber)      
        return common_resource.get_by_id(result, Badge, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/badge')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = badge_service.insert(entity)
        return common_resource.create(result, json_serializer, Badge)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/badge/<badgeNumber>')
def update(badgeNumber):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.badgeNumber = badgeNumber
        result = badge_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/badge')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = badge_service.save(entity)
        return common_resource.save(result, Badge, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/badge/<badgeNumber>')
def delete(badgeNumber):
    try:
        result = badge_service.delete_by_id(badgeNumber)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/badge.count')
def count():
    try:
        result = badge_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
