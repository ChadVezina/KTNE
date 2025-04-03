from typing import Callable
from .bouton_case import BoutonCase
from ..tools.enums import TypeConnexion, TypeFil
from model.texte import Texte

class Case:
    def __init__(self, numero, commande):
        self.numero = numero
        self.commande = commande
        self.action: Callable[[TypeConnexion], bool] | None = None
        self.type: TypeFil | None = None
        self.connexion: TypeConnexion | None = None
        self.is_active = False
        self.is_connexion = False

    def placer_case(self, parent):
        self.destroy()
        self.label = Texte(parent, self.numero, 0, f"Fil {self.numero + 1}")
        self.solution = Texte(parent, self.numero, 1)
        self.bouton_rouge = BoutonCase(parent, self.numero, 2, "rouge", lambda: self.clic(TypeFil.ROUGE))
        self.bouton_bleu = BoutonCase(parent, self.numero, 3, "bleu", lambda: self.clic(TypeFil.BLEU))
        self.bouton_noir = BoutonCase(parent, self.numero, 4, "noir", lambda: self.clic(TypeFil.NOIR))
        self.bouton_a = BoutonCase(parent, self.numero, 5, "A", lambda: self.clic_connexion(TypeConnexion.A))
        self.bouton_b = BoutonCase(parent, self.numero, 6, "B", lambda: self.clic_connexion(TypeConnexion.B))
        self.bouton_c = BoutonCase(parent, self.numero, 7, "C", lambda: self.clic_connexion(TypeConnexion.C))

    def destroy(self):
        self.is_active = False
        self.is_connexion = False
        self.type = None
        self.connexion = None
        self.action = None

    def add_solution(self, action: Callable[[TypeConnexion], bool]):
        if self.action == action:
            return
        self.action = action
        self.update_solution()

    def update_solution(self):
        if self.action and self.connexion:
            if self.action(self.connexion):
                self.set_solution("Couper")
            else:
                self.set_solution("Ne pas couper")

    def set_solution(self, texte):
        self.solution.set_texte(texte)

    def clear_solution(self):
        self.solution.clear_texte()
        self.action = None

    def clic(self, type: TypeFil):
        if self.is_active:
            condition = self.type == type
            self.desactiver()
            if condition:
                self.commande(self.numero)
                return
        self.activer(type)
        self.commande(self.numero)

    def activer(self, type: TypeFil):
        match type:
            case TypeFil.ROUGE:
                self.bouton_rouge.activer()
            case TypeFil.BLEU:
                self.bouton_bleu.activer()
            case TypeFil.NOIR:
                self.bouton_noir.activer()
        self.type = type
        self.is_active = True

    def desactiver(self):
        match self.type:
            case TypeFil.ROUGE:
                self.bouton_rouge.desactiver()
            case TypeFil.BLEU:
                self.bouton_bleu.desactiver()
            case TypeFil.NOIR:
                self.bouton_noir.desactiver()
        self.type = None
        self.is_active = False
        self.solution.clear_texte()

    def clic_connexion(self, type: TypeConnexion):
        if self.is_connexion:
            condition = self.connexion == type
            self.desactiver_connexion()
            if condition:
                self.update_solution()
                return
        self.activer_connexion(type)
        self.update_solution()

    def activer_connexion(self, type: TypeConnexion):
        match type:
            case TypeConnexion.A:
                self.bouton_a.activer()
            case TypeConnexion.B:
                self.bouton_b.activer()
            case TypeConnexion.C:
                self.bouton_c.activer()
        self.connexion = type
        self.is_connexion = True

    def desactiver_connexion(self):
        match self.connexion:
            case TypeConnexion.A:
                self.bouton_a.desactiver()
            case TypeConnexion.B:
                self.bouton_b.desactiver()
            case TypeConnexion.C:
                self.bouton_c.desactiver()
        self.connexion = None
        self.is_connexion = False
        self.solution.clear_texte()
