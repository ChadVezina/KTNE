from tkinter import Button

from ..tools.constantes import BoutonCaseRect, Font
from ..tools.enums import TypeCase


class BoutonCase(Button):
    def __init__(self, parent, x, y, texte, commande):
        self.x = x
        self.y = y
        super().__init__(
            parent,
            font=Font.BODY,
            text=".",
            padx=BoutonCaseRect.PADDING_X,
            pady=BoutonCaseRect.PADDING_Y,
            width=BoutonCaseRect.WIDTH,
            height=BoutonCaseRect.HEIGHT,
            command=commande,
            bg="white",
            )
        self.grid(row=x, column=y)

    def setType(self, type: TypeCase):
        match type:
            case TypeCase.VIDE:
                self["text"] = "white"
            case TypeCase.OBSTACLE:
                self["text"] = "black"
            case TypeCase.DEPART:
                self["text"] = "red"
            case TypeCase.ARRIVEE:
                self["text"] = "green"
            case _:
                pass

