import json
import datetime
from entities.Eleve import Eleve


class EleveJsonSerializer(object):
    def to_json(self, entity: Eleve):
        return {
            "idEleve": entity.idEleve,
            "nom": entity.nom,
            "prenom": entity.prenom,
            "email": entity.email,
            "password": entity.password,
            "codePostal": entity.codePostal,
            "genre": entity.genre,
            "dateInscription": str(entity.dateInscription),
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Eleve()
        entity.idEleve = data['idEleve']
        entity.nom = data['nom']
        entity.prenom = data['prenom']
        entity.email = data['email']
        entity.password = data['password']
        entity.codePostal = data['codePostal']
        entity.genre = data['genre']
        entity.dateInscription = datetime.datetime.strptime(data['dateInscription'], "%Y-%m-%d %H:%M:%S")
        return entity
