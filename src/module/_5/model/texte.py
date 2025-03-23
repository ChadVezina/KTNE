from tkinter import Entry, StringVar
from typing import Callable
from ..tools.constantes import GridPad, Font

class Texte(Entry):
    def __init__(self, parent, row, commande: Callable[[], None]):
        self.sv = StringVar()
        super().__init__(parent, font=Font.BODY, textvariable=self.sv, bg="white")
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        self.bind("<KeyRelease>", lambda e: commande())

    def get_texte(self):
        return self.sv.get().strip()

    def is_exist(self):
        self["bg"] = "green"

    def is_not_exist(self):
        self["bg"] = "white"
