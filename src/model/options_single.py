from tkinter import Frame
from typing import Callable
from model.bouton import Bouton
from constants.config import GridPad

class Options(Frame):
    def __init__(self, parent: Frame, row: int, options: dict[int, str], commande: Callable[[int], None]):
        super().__init__(parent)
        self.grid(row = row, padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)
        self.make_options(options, commande)

    def make_options(self, options: dict[int, str], commande: Callable[[int], None]) -> None:
        self.boutons: dict[int, Bouton] = {}
        self.bouton_active: int = -1
        for scan, option in options.items():
            self.boutons[scan] = Bouton(self, 0, scan, option, lambda scan = scan: commande(scan))

    def add_command(self, scan: int, commande: Callable[[int], None]) -> None:
        self.boutons[scan]["command"] = lambda scan = scan: commande(scan)

    def get_active_option(self) -> int:
        return self.bouton_active

    def is_active(self, scan: int) -> bool:
        return self.bouton_active == scan

    def activer(self, scan: int) -> None:
        if self.bouton_active != -1:
            self.desactiver(self.bouton_active)
        self.boutons[scan].activer()
        self.bouton_active = scan

    def desactiver(self, scan: int) -> None:
        self.boutons[scan].desactiver()
        self.bouton_active = -1
