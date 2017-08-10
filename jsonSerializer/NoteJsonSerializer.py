import json
import datetime
from entities.Note import Note


class NoteJsonSerializer(object):
    def to_json(self, entity: Note):
        return {
            "idCours": entity.idCours,
            "idEleve": entity.idEleve,
            "noteObtenue": entity.noteObtenue,
            "dateExamen": str(entity.dateExamen),
            "codeMention": entity.codeMention,
        }

    def from_json(self, json_content: str):
        data = json.loads(json_content)
        entity = Note()
        entity.idCours = data['idCours']
        entity.idEleve = data['idEleve']
        entity.noteObtenue = data['noteObtenue']
        entity.dateExamen = datetime.datetime.strptime(data['dateExamen'], "%Y-%m-%d %H:%M:%S")
        entity.codeMention = data['codeMention']
        return entity
