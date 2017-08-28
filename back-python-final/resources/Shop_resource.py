# Python class for resource of Shop 
# Created on 2017-08-25 ( Time 18:18:33 )

from bottle import get, post, put, delete, response
from services import Shop_service as CommonsEntityService
from JsonSerializer.Shop_json_serializer import ShopJsonSerializer
from entities.Shop import Shop
from resources.commons import common_resource

shop_service = CommonsEntityService.ShopService()
json_serializer = ShopJsonSerializer()


@get('/api/v1/shop')
def get_all():
    try:
        entities = shop_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/shop/<code>')
def get_by_id(code):
    try:
        result = shop_service.find_by_id(code)      
        return common_resource.get_by_id(result, Shop, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/shop')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = shop_service.insert(entity)
        return common_resource.create(result, json_serializer, Shop)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/shop/<code>')
def update(code):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.code = code
        result = shop_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/shop')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = shop_service.save(entity)
        return common_resource.save(result, Shop, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/shop/<code>')
def delete(code):
    try:
        result = shop_service.delete_by_id(code)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/shop.count')
def count():
    try:
        result = shop_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
