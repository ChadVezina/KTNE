from .model.tableau import Tableau
from .tools.fonctions import make_menu
from constants.fenetre import Titre
from tools.module import Module


class Module_9(Module):
    def __init__(self, root, geometrie):
        super().__init__(root, geometrie)

        self.title(Titre.MODULE_9.value)

        self.tableau = Tableau()

        make_menu(self, self.nouvelle_partie, self.quitter)

        self.ouvrir_partie()

    def redessiner(self):
        for widget in self.cadre.winfo_children():
            widget.destroy()
        self.tableau.placer_tableau(self.cadre)
