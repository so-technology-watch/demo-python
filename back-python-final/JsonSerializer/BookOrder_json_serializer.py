# Python class for json serializer of BookOrder 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.BookOrder import BookOrder


class BookOrderJsonSerializer(object):
    def to_json(self, entity: BookOrder):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "id": entity.id,
            "shopCode": entity.shopCode,
            "customerCode": entity.customerCode,
            "employeeCode": entity.employeeCode,
            "date": str(entity.date),
            "state": entity.state,
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = BookOrder()
        if "id" in data:
            entity.id = data['id']
        else:
            entity.id = None
        entity.shopCode = data['shopCode']
        entity.customerCode = data['customerCode']
        entity.employeeCode = data['employeeCode']
        entity.date = datetime.datetime.strptime(data['date'], "%Y-%m-%d %H:%M:%S")
        entity.state = data['state']
        return entity
