from tkinter import Frame
from typing import Callable
from model.bouton import Bouton
from constants.config import GridPad, BoutonCaseRect, Font

class Options(Frame):
    def __init__(self, parent: Frame, row: int, options: dict[int, str]):
        super().__init__(parent)
        self.grid(row = row, padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)
        self.make_options(options)

    def make_options(self, options: dict[int, str]):
        self.boutons: dict[int, Bouton] = {}
        self.bouton_active: int = -1
        for scan, option in options.items():
            self.boutons[scan] = Bouton(self, col=scan, texte=option, wraplength=BoutonCaseRect.WRAP_LENGTH, no_padding=True)

    def add_command(self, scan: int, commande: Callable[[int], None]):
        self.boutons[scan].add_command(lambda scan = scan: commande(scan))

    def get_active_option(self):
        return self.bouton_active

    def is_active(self, scan: int):
        return self.bouton_active == scan

    def activer(self, scan: int):
        if self.bouton_active != -1:
            self.desactiver(self.bouton_active)
        self.boutons[scan].activer()
        self.bouton_active = scan

    def desactiver(self, scan: int):
        self.boutons[scan].desactiver()
        self.bouton_active = -1
