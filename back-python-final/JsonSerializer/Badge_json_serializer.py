# Python class for json serializer of Badge 
# Created on 2017-08-25 ( Time 18:18:32 )

import json
import datetime
from entities.Badge import Badge


class BadgeJsonSerializer(object):
    def to_json(self, entity: Badge):
        """
        Convert into a json
        :param entity: entity to convert
        :return: entity into json  
        """
        return {
            "badgeNumber": entity.badgeNumber,
            "authorizationLevel": entity.authorizationLevel,
            "endOfValidity": str(entity.endOfValidity),
        }

    def from_json(self, json_content: str):
        """
        Convert a json into an object
        :param json_content: json to convert
        :return: entity object
        """
        data = json.loads(json_content)
        entity = Badge()
        if "badgeNumber" in data:
            entity.badgeNumber = data['badgeNumber']
        else:
            entity.badgeNumber = None
        entity.authorizationLevel = data['authorizationLevel']
        entity.endOfValidity = datetime.datetime.strptime(data['endOfValidity'], "%Y-%m-%d %H:%M:%S")
        return entity
