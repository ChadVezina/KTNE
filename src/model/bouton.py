from tkinter import Button
from constants.config import GridPad, BoutonCaseRect, Font

class Bouton(Button):
    def __init__(self, parent, row, col=0, texte=""):
        super().__init__(parent, font=Font.BODY, text=texte, padx=BoutonCaseRect.PADDING_X, pady=BoutonCaseRect.PADDING_Y, bg="white", relief="sunken")
        self.grid(row=row, column=col, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)

    def get_texte(self) -> str:
        return self.cget("text")

    def set_texte(self, texte):
        self["text"] = texte

    def is_exist(self):
        self["bg"] = "green"

    def is_not_exist(self):
        self["bg"] = "white"

    def set_active(self, active: bool):
        if active:
            self.config(relief="sunken")
        else:
            self.config(relief="raised")

    def activer(self):
        self["bg"] = "pink"

    def desactiver(self):
        self["bg"] = "white"
