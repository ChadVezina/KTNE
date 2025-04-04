from tkinter import Frame
from typing import Callable

from model.bouton import Bouton
from constants.config import GridPad

class Tableau(Frame):
    def __init__(self, parent: Frame, row: int, textes: list[str], options: list[str], commande_texte: Callable[[str], None], commande_option: Callable[[str], None]):
        super().__init__(parent)
        self.grid(row = row, padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)
        self.boutons: tuple[dict[str, Bouton], dict[str, Bouton]] = [{}, {}]
        self.first_split = 10
        self.second_split = 5
        self.make_options(0, textes, commande_texte, self.first_split)
        self.make_options(1, options, commande_option, self.second_split)

    def make_options(self, row: int, options: list[str], commande: Callable[[str], None], split_col: int = 2):
        composante = Frame(self)
        composante.grid(row = row, padx = GridPad.PADDING_X*2, pady = GridPad.PADDING_Y*2)
        for scan, texte in enumerate(options):
            self.boutons[row][texte] = self.make_button(composante, scan, texte, lambda texte=texte: commande(texte), split_col)
        return composante

    def make_button(self, parent: Frame, colonne: int, texte: str, commande: Callable[[], None], split_col: int):
        x = colonne // split_col
        y = colonne % split_col
        return Bouton(parent, x, y, texte, commande)

    def set_active_all(self) -> None:
        for texte in self.boutons[1].keys():
            self.boutons[1][texte].show()

    def set_active(self, liste: list[str], options: list[str]) -> None:
        for texte in self.boutons[1].keys():
            self.boutons[1][texte].hide()
        colonne = 0
        for texte in liste:
            if texte in self.boutons[1].keys():
                x = colonne // self.second_split
                y = colonne % self.second_split
                self.boutons[1][texte].show_with(x, y, texte in options)
                colonne += 1
