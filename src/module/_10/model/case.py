from .bouton_case import BoutonCase
from ..tools.enums import TypeCase

class Case:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.type = None
        self.bouton = None
        self.init()

    def init(self):
        if self.type = = TypeCase.POINT_A or self.type = = TypeCase.POINT_B:
            return
        if self.x % 2 = = 0 or self.y % 2 = = 0:
            self.setType(TypeCase.MUR_VIDE)
        else:
            self.setType(TypeCase.VIDE)

    def placer_case(self, parent, x: int, y: int, commande):
        self.bouton = BoutonCase(parent, x, y, lambda: self.clic(commande))
        self.bouton.setType(self.type)

    def setType(self, type: TypeCase):
        if self.type = = type:
            return
        self.type = type
        if self.bouton is not None:
            self.bouton.setType(type)

    def clic(self, commande):
        commande(self.x, self.y, self.type)
