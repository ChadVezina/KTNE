from tkinter import Frame, Button
from typing import Callable

from constants.config import GridPad, BoutonCaseRect, Font

class Options(Frame):
    def __init__(self, parent: Frame, row: int, commande: Callable[[int], None], n_options: int = 6):
        super().__init__(parent)
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        self.n_options = n_options
        self.make_options(commande)

    def make_options(self, commande: Callable[[int], None]):
        self.boutons: dict[int, Button] = {}
        self.bouton_active: int = -1
        for scan in range(self.n_options):
            self.boutons[scan] = self.make_button(scan)
        for scan in range(self.n_options):
            self.add_command(scan, commande)

    def make_button(self, colonne: int):
        x = colonne // 2
        y = colonne % 2
        bouton = Button(self, font=Font.BODY, text=" ", padx=BoutonCaseRect.PADDING_X, pady=BoutonCaseRect.PADDING_Y, bg="white", relief="raised")
        bouton.grid(row=x, column=y, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        return bouton

    def add_command(self, scan: int, commande: Callable[[int], None]):
        self.boutons[scan]["command"] = lambda: commande(scan)

    def get_option(self, scan: int) -> str:
        return self.boutons[scan].cget("text")

    def set_option(self, scan: int, texte: str):
        self.boutons[scan]["text"] = texte

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
        self.boutons[scan]["bg"] = "green"

    def is_not_exist(self, scan: int):
        self.boutons[scan]["bg"] = "white"

    def set_active_option(self, scan: int, active: bool):
        if active:
            self.boutons[scan].config(relief="sunken")
        else:
            self.boutons[scan].config(relief="raised")

    def activer(self, scan: int):
        if(self.bouton_active != -1 and not self.is_active(scan)):
            self.desactiver(self.bouton_active)
        self.boutons[scan]["bg"] = "pink"
        self.bouton_active = scan

    def desactiver(self, scan: int):
        if(self.is_active(scan)):
            self.boutons[scan]["bg"] = "white"
            self.bouton_active = -1
