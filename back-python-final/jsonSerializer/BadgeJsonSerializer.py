import json
import datetime
from entities.Badge import Badge


class BadgeJsonSerializer(object):
    def to_json(self, entity: Badge):
        return {
            "badgeNumber": entity.badgeNumber,
            "authorizationLevel": entity.authorizationLevel,
            "endOfValidity": str(entity.endOfValidity),
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Badge()
        entity.badgeNumber = data['badgeNumber']
        entity.authorizationLevel = data['authorizationLevel']
        entity.endOfValidity = datetime.datetime.strptime(data['endOfValidity'], "%Y-%m-%d %H:%M:%S")
        return entity
