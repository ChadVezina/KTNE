from tkinter import Frame
from typing import Callable

from model.bouton import Bouton
from constants.config import GridPad

class Options(Frame):
    def __init__(self, parent: Frame, row: int, commande: Callable[[int], None], n_options: int = 6):
        super().__init__(parent)
        self.grid(row = row, padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)
        self.n_options = n_options
        self.make_options(commande)

    def make_options(self, commande: Callable[[int], None]):
        self.boutons: dict[int, Bouton] = {}
        self.bouton_active: int = -1
        for scan in range(self.n_options):
            self.boutons[scan] = self.make_button(scan)
        for scan in range(self.n_options):
            self.add_command(scan, commande)

    def make_button(self, colonne: int):
        x = colonne // 2
        y = colonne % 2
        return Bouton(self, x, y, relief="raised")

    def add_command(self, scan: int, commande: Callable[[int], None]):
        self.boutons[scan]["command"] = lambda scan=scan: commande(scan)

    def get_option(self, scan: int) -> str:
        return self.boutons[scan].get_texte()

    def set_option(self, scan: int, texte: str):
        self.boutons[scan].set_texte(texte)

    def get_options(self):
        options: list[str] = []
        for scan in range(self.n_options):
            options.append(self.get_option(scan))
        return options

    def get_active_option(self):
        return self.bouton_active

    def is_active(self, scan: int):
        return self.bouton_active == scan

    def is_exist(self, scan: int):
        self.boutons[scan].is_exist()

    def is_not_exist(self, scan: int):
        self.boutons[scan].is_not_exist()

    def set_active_option(self, scan: int, active: bool):
        self.boutons[scan].set_active(active)

    def activer(self, scan: int):
        if(self.bouton_active != -1 and not self.is_active(scan)):
            self.desactiver(self.bouton_active)
        self.boutons[scan].activer()
        self.bouton_active = scan

    def desactiver(self, scan: int):
        if(self.is_active(scan)):
            self.boutons[scan].desactiver()
            self.bouton_active = -1

    def set_pointer_option(self, scan: int):
        self.boutons[scan]["bg"] = "purple"
