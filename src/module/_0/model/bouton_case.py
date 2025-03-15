"""
Bouton représentant une case. Le fait de cliquer sur le bouton remplace
les inputs de coordonnées au TP3.
"""

from tkinter import Button

from ..tools.constantes import BoutonCaseRect, Font


class BoutonCase(Button):
    def __init__(self, parent, rangee_x, colonne_y):
        self.rangee_x = rangee_x
        self.colonne_y = colonne_y
        super().__init__(parent, font=Font.BODY, text=' ', padx=BoutonCaseRect.PADDING_X, pady=BoutonCaseRect.PADDING_Y, width=BoutonCaseRect.WIDTH, height=BoutonCaseRect.HEIGHT)

    def activer(self, commande):
        self["state"] = "normal"
        self.bind('<Button-1>', commande)

    def desactiver(self):
        self["state"] = "disabled"
        self.unbind("<Button-1>")
