from tkinter import Label
from constants.config import GridPad, Font

class Texte(Label):
    def __init__(self, parent, row, col, texte = ""):
        super().__init__(parent, font = Font.BODY, text = texte)
        self.grid(row = row, column = col, padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)

    def set_texte(self, texte):
        self["text"] = texte

    def clear_texte(self):
        self["text"] = ""
