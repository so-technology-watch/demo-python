# Python class for resource of Review 
# Created on 2017-08-25 ( Time 18:18:32 )

from bottle import get, post, put, delete, response
from services import Review_service as CommonsEntityService
from JsonSerializer.Review_json_serializer import ReviewJsonSerializer
from entities.Review import Review
from resources.commons import common_resource

review_service = CommonsEntityService.ReviewService()
json_serializer = ReviewJsonSerializer()


@get('/api/v1/review')
def get_all():
    try:
        entities = review_service.find_all()
        return common_resource.get_all(json_serializer, entities)
    except TypeError as e:
        return common_resource.error_500(e)
 

@get('/api/v1/review/<customerCode>/<bookId>')
def get_by_id(customerCode, bookId):
    try:
        result = review_service.find_by_id(customerCode, bookId)      
        return common_resource.get_by_id(result, Review, json_serializer)
    except TypeError as e:
        return common_resource.error_500(e)


@post('/api/v1/review')
def create():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = review_service.insert(entity)
        return common_resource.create(result, json_serializer, Review)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/review/<customerCode>/<bookId>')
def update(customerCode, bookId):
    try:
        entity = common_resource.body_from_json(json_serializer)
        entity.customerCode = customerCode
        entity.bookId = bookId
        result = review_service.update(entity)
        return common_resource.update(result)
    except TypeError as e:
        return common_resource.error_500(e)


@put('/api/v1/review')
def save():
    try:
        entity = common_resource.body_from_json(json_serializer)
        result = review_service.save(entity)
        return common_resource.save(result, Review, json_serializer, entity)
    except TypeError as e:
        return common_resource.error_500(e)


@delete('/api/v1/review/<customerCode>/<bookId>')
def delete(customerCode, bookId):
    try:
        result = review_service.delete_by_id(customerCode, bookId)
        return common_resource.delete(result)
    except TypeError as e:
        return common_resource.error_500(e)


@get('/api/v1/review.count')
def count():
    try:
        result = review_service.count_all()
        return common_resource.count(result)
    except TypeError as e:
        print(e)
        response.status = 400
