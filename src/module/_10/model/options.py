from textwrap import wrap
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
        self.bouton_active: int = -1
        for option in options.items():
            self.boutons[option[0]] = self.make_button(option[0], option[1])

    def make_button(self, colonne: int, texte: str):
        bouton = Button(self, font=Font.BODY, text=texte, bg="white", wraplength=100)
        bouton.grid(row=0, column=colonne, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        return bouton

    def add_command(self, scan: int, commande: Callable[[int], None]):
        self.boutons[scan]["command"] = lambda: commande(scan)

    def get_active_option(self):
        return self.bouton_active

    def is_active(self, scan: int):
        return self.bouton_active == scan

    def activer(self, scan: int):
        if self.bouton_active != -1:
            self.desactiver(self.bouton_active)
        self.boutons[scan]["bg"] = "pink"
        self.bouton_active = scan

    def desactiver(self, scan: int):
        self.boutons[scan]["bg"] = "white"
        self.bouton_active = -1
