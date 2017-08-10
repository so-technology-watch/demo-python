import json
import datetime
from entities.Cours import Cours


class CoursJsonSerializer(object):
    def to_json(self, entity: Cours):
        return {
            "idCours": entity.idCours,
            "libelle": entity.libelle,
            "nbHeures": entity.nbHeures,
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Cours()
        entity.idCours = data['idCours']
        entity.libelle = data['libelle']
        entity.nbHeures = data['nbHeures']
        return entity
