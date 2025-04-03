from tkinter import Frame, Button
from typing import Callable

from ..tools.constantes import GridPad, BoutonCaseRect, Font

class Options(Frame):
    def __init__(self, parent: Frame, row: int, commande: Callable[[int], None]):
        super().__init__(parent)
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        self.boutons: dict[int, Button] = {}
        self.result: int = -1
        self.make_options(commande)

    def make_options(self, commande: Callable[[int], None]):
        for scan in range(6):
            self.boutons[scan] = self.make_button(scan)
        for scan in range(6):
            self.add_command(scan, commande)

    def make_button(self, colonne: int):
        x = colonne // 2
        y = colonne % 2
        bouton = Button(self, font=Font.BODY, text=" ", padx=BoutonCaseRect.PADDING_X, pady=BoutonCaseRect.PADDING_Y, bg="white", relief="raised")
        bouton.grid(row=x, column=y, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        return bouton

    def add_command(self, scan: int, commande: Callable[[int], None]):
        self.boutons[scan]["command"] = lambda scan=scan: commande(scan)

    def get_option(self, scan: int) -> str:
        return self.boutons[scan].cget("text")

    def set_option(self, scan: int, texte: str):
        self.boutons[scan]["text"] = texte

    def get_options(self):
        options: list[str] = []
        for scan in range(6):
            options.append(self.get_option(scan))
        return options

    def get_active_option(self):
        return self.result

    def is_active(self, scan: int):
        return self.result == scan

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
        if(self.result != -1 and not self.is_active(scan)):
            self.desactiver(self.result)
        self.boutons[scan]["bg"] = "pink"
        self.result = scan

    def desactiver(self, scan: int):
        if(self.is_active(scan)):
            self.boutons[scan]["bg"] = "white"
            self.result = -1
