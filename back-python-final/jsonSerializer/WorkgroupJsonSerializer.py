import json
import datetime
from entities.Workgroup import Workgroup


class WorkgroupJsonSerializer(object):
    def to_json(self, entity: Workgroup):
        return {
            "id": entity.id,
            "name": entity.name,
            "description": entity.description,
            "creationDate": str(entity.creationDate),
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Workgroup()
        entity.id = data['id']
        entity.name = data['name']
        entity.description = data['description']
        entity.creationDate = datetime.datetime.strptime(data['creationDate'], "%Y-%m-%d %H:%M:%S")
        return entity
