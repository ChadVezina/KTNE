from tkinter import Label
from ..tools.constantes import GridPad, Font

class Texte(Label):
    def __init__(self, parent, row):
        super().__init__(parent, font=Font.BODY, text= "", bg="white")
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)

    def set_texte(self, texte: str):
        self["text"] = texte

    def desactiver(self):
        self["text"] = ""
