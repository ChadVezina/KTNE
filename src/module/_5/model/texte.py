from tkinter import Button
from typing import Callable
from tools.constants import GridPad, BoutonCaseRect, Font

class Texte(Button):
    def __init__(self, parent, row):
        super().__init__(parent, font=Font.BODY, text=" ", padx=BoutonCaseRect.PADDING_X, pady=BoutonCaseRect.PADDING_Y, bg="white", relief="sunken")
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)

    def get_texte(self) -> str:
        return self.cget("text")

    def set_texte(self, texte):
        self["text"] = texte

    def is_exist(self):
        self["bg"] = "green"

    def is_not_exist(self):
        self["bg"] = "white"
