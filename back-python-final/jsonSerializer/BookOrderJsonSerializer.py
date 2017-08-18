import json
import datetime
from entities.BookOrder import BookOrder


class BookOrderJsonSerializer(object):
    def to_json(self, entity: BookOrder):
        return {
            "id": entity.id,
            "shopCode": entity.shopCode,
            "customerCode": entity.customerCode,
            "employeeCode": entity.employeeCode,
            "date": str(entity.date),
            "state": entity.state,
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = BookOrder()
        entity.id = data['id']
        entity.shopCode = data['shopCode']
        entity.customerCode = data['customerCode']
        entity.employeeCode = data['employeeCode']
        entity.date = datetime.datetime.strptime(data['date'], "%Y-%m-%d %H:%M:%S")
        entity.state = data['state']
        return entity
