class Assurance(object):
    def __init__(self, assurance_id, car_id, type, montant, date_debut, date_fin):
        self.assurance_id = assurance_id
        self.car_id = car_id
        self.type = type
        self.montant = montant
        self.date_debut = date_debut
        self.date_fin = date_fin
