from tkinter import Frame, Button
from typing import Callable

from ..tools.constantes import GridPad, BoutonCaseRect, Font

class Tableau(Frame):
    def __init__(self, parent: Frame, row: int, textes: list[str], options: list[str], commande_texte: Callable[[str], None], commande_option: Callable[[str], None]):
        super().__init__(parent)
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        self.make_options(0, textes, commande_texte, 10)
        self.make_options(1, options, commande_option, 10)

    def make_options(self, row: int, options: list[str], commande: Callable[[str], None], split_col: int = 2):
        composante = Frame(self)
        composante.grid(row=row, padx=GridPad.PADDING_X*2, pady=GridPad.PADDING_Y*2)
        for scan, texte in enumerate(options):
            bouton = self.make_button(composante, scan, texte, split_col)
            bouton["command"] = lambda texte=texte: commande(texte)
        return composante

    def make_button(self, parent: Frame, colonne: int, texte: str, split_col: int):
        x = colonne // split_col
        y = colonne % split_col
        bouton = Button(parent, font=Font.BODY, text=texte, padx=BoutonCaseRect.PADDING_X, pady=BoutonCaseRect.PADDING_Y, bg="white")
        bouton.grid(row=x, column=y, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        return bouton
