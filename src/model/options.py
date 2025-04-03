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
        self.boutons_active: dict[int, bool] = {}
        for scan, option in options.items():
            self.boutons[scan] = Bouton(self, 0, scan, option)
            self.boutons_active[scan] = False
        for scan in options.keys():
            self.add_command(scan, commande)

    def add_command(self, scan: int, commande: Callable[[int], None]) -> None:
        self.boutons[scan]["command"] = lambda: commande(scan)

    def get_active_options(self) -> list[int]:
        liste = [scan for scan in self.boutons_active if self.boutons_active[scan]]
        return sorted(liste, key = lambda scan: scan)

    def is_active(self, scan: int) -> int:
        return self.boutons_active[scan]

    def activer(self, scan: int) -> None:
        self.boutons[scan].activer()
        self.boutons_active[scan] = True

    def desactiver(self, scan: int) -> None:
        self.boutons[scan].desactiver()
        self.boutons_active[scan] = False
