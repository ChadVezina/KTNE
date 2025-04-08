from tkinter import Frame
from typing import Callable
from .options import Options
from .tableau import Tableau
from model.bouton import Bouton

class Etape(Frame):
    def __init__(self, parent: Frame, row: int, textes: list[str], options: list[str], commande: Callable[[], None]):
        super().__init__(parent)
        self.grid(row = row)
        self.commande = commande
        self.bouton_active = -1
        self.texte = Bouton(self, 0, relief="sunken")
        self.options = Options(self, 1, self.clic_option)
        self.tableau = Tableau(self, 2, textes, options, self.clic_tableau_texte, self.clic_tableau_option)
        self.clic_option(0)

    def clic_option(self, scan: int):
        if self.bouton_active != scan:
            self.prev_option()
            self.bouton_active = scan
            self.options.set_active_option(scan, True)

    def prev_option(self):
        if self.bouton_active != -1:
            self.options.set_active_option(self.bouton_active, False)

    def clic_tableau_texte(self, texte: str):
        self.texte.set_texte(texte)
        self.commande()

    def clic_tableau_option(self, texte: str):
        if self.bouton_active != -1:
            self.options.set_option(self.bouton_active, texte)
            self.commande()
            length = len(self.options.boutons)
            if self.bouton_active == length - 1:
                self.clic_option(0)
            else:
                self.clic_option(self.bouton_active + 1)
