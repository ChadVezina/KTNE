from .model.tableau import Tableau
from constants.fenetre import Titre
from constants.instructions import Contenu
from model.module import Module


class Module_9(Module):
    def __init__(self, root, geometrie):
        self.tableau = Tableau()

        super().__init__(Titre.MODULE_9, Contenu.MODULE_9, root, geometrie)

    def redessiner(self):
        self.tableau.do(self.cadre, 0)
