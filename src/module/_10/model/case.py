from .bouton_case import BoutonCase
from ..tools.enums import TypeCase

class Case:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.type = TypeCase.VIDE

    def placer_case(self, parent, x, y):
        self.bouton = BoutonCase(parent, x, y, self.texte, lambda: self.clic())

    def setType(self, type: TypeCase):
        self.type = type

    def clic(self, type: TypeCase):
        if(self.type == type):
            self.setType(TypeCase.VIDE)
        else:
            self.setType(type)
