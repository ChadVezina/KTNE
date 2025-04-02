from .model.next_link import NextLink
from .tools.fonctions import make_menu
from constants.fenetre import Titre
from tools.module import Module


class Module_7(Module):
    def __init__(self, root, geometrie):
        super().__init__(root, geometrie)

        self.title(Titre.MODULE_7.value)

        self.next_link = NextLink()

        make_menu(self, self.nouvelle_partie, self.quitter)

        self.ouvrir_partie()

    def redessiner(self):
        self.next_link.undo()
        self.next_link.do(self.cadre, 0)
