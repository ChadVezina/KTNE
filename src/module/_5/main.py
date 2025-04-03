from .model.next_link import NextLink
from constants.fenetre import Titre
from constants.instructions import Contenu
from src.model.module import Module


class Module_5(Module):
    def __init__(self, root, geometrie):
        self.next_link = NextLink()

        super().__init__(Titre.MODULE_5, Contenu.MODULE_5, root, geometrie)

    def redessiner(self):
        self.next_link.do(self.cadre, 0)
