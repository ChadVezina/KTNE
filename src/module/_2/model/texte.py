from tkinter import Label
from tools.constants import GridPad, Font

class Texte(Label):
    def __init__(self, parent, row, texte):
        super().__init__(parent, font=Font.BODY, text=texte)
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
