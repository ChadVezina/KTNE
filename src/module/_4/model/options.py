from tkinter import Frame, Button
from typing import Callable
from ..tools.constantes import GridPad, Font

class Options(Frame):
    def __init__(self, parent: Frame, row: int, options: dict[int, str]):
        super().__init__(parent)
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        self.make_options(options)

    def make_options(self, options: dict[int, str]):
        self.boutons: dict[int, Button] = {}
        self.boutons_active: dict[int, bool] = {}
        for option in options.items():
            self.boutons[option[0]] = self.make_button(option[0], option[1])
            self.boutons_active[option[0]] = False

    def make_button(self, colonne: int, texte: str):
        bouton = Button(self, font=Font.BODY, text=texte, bg="white")
        bouton.grid(row=0, column=colonne, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        return bouton

    def add_command(self, scan: int, commande: Callable):
        self.boutons[scan].config(command=commande)

    def get_active_options(self):
        liste = [scan for scan in self.boutons_active if self.boutons_active[scan]]
        return sorted(liste, key=lambda scan: scan)

    def is_active(self, scan: int):
        return self.boutons_active[scan]

    def activer(self, scan: int):
        self.boutons[scan]["bg"] = "pink"
        self.boutons_active[scan] = True

    def desactiver(self, scan: int):
        self.boutons[scan]["bg"] = "white"
        self.boutons_active[scan] = False
