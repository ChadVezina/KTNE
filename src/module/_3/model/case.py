from tkinter import Frame
from model.bouton import Bouton
from model.texte import Texte
from constants.config import HintCaseRect, Font

class Case:
    def __init__(self, numero, texte, hint, afficher_solution):
        self.numero = numero
        self.texte = texte
        self.hint = hint
        self.afficher_solution = afficher_solution
        self.bouton = None
        self.is_active = False

    def placer_case(self, parent, x, y):
        self.is_active = False
        self.composante = Frame(parent)
        self.composante.grid(row = x, column = y)
        self.bouton = Bouton(self.composante, 0, 0, self.texte, lambda: self.clic(), Font.BODY_SYMBOLE, no_margin = True)
        self.label = Texte(self.composante, 1, 0, self.hint, Font.BODY_HINT, HintCaseRect.WIDTH, HintCaseRect.WRAP_LENGTH, True)

    def clic(self):
        if self.is_active:
            self.desactiver()
        else:
            self.activer()
        self.afficher_solution()

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
