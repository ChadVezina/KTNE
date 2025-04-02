from .model.tableau import Tableau
from .tools.fonctions import make_menu
from constants.fenetre import Titre
from tools.module import Module


class Module_8(Module):
    def __init__(self, root, geometrie):
        super().__init__(root, geometrie)

        self.title(Titre.MODULE_8.value)

        self.tableau = Tableau()

        make_menu(self, self.nouvelle_partie, self.quitter)

        self.ouvrir_partie()

    def redessiner(self):
        self.tableau.do(self.cadre, 0)
