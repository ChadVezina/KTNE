from .bouton_case import BoutonCase

class Case:
    def __init__(self, numero, texte):
        self.numero = numero
        self.texte = texte
        self.bouton = None
        self.is_active = False

    def placer_case(self, parent, x, y):
        self.is_active = False
        self.bouton = BoutonCase(parent, x, y, self.texte, lambda: self.clic())

    def clic(self):
        if self.is_active:
            self.desactiver()
        else:
            self.activer()

    def activer(self):
        self.is_active = True
        self.bouton.activer()

    def desactiver(self):
        self.is_active = False
        self.bouton.desactiver()

    def colonnes_valides(self, colonnes):
        if not self.is_active:
            return None
        colonne_ids: list[int] = []
        for id, colonne in enumerate(colonnes):
            if self.texte in colonne:
                colonne_ids.append(id)
        return colonne_ids