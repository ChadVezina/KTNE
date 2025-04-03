from .model.tableau import Tableau
from constants.fenetre import Titre
from constants.instructions import Contenu
from model.module import Module


class Module_8(Module):
    def __init__(self, root, geometrie):
        self.tableau = Tableau()

        super().__init__(Titre.MODULE_8, Contenu.MODULE_8, root, geometrie)

    def redessiner(self):
        self.tableau.do(self.cadre, 0)
