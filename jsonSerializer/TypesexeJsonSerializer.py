import json
import datetime
from entities.Typesexe import Typesexe


class TypesexeJsonSerializer(object):
    def to_json(self, entity: Typesexe):
        return {
            "idSexe": entity.idSexe,
            "labelSexe": entity.labelSexe,
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Typesexe()
        entity.idSexe = data['idSexe']
        entity.labelSexe = data['labelSexe']
        return entity
