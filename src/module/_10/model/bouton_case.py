from tkinter import Button

from constants.config import BoutonCaseRect, Font
from ..tools.enums import TypeCase


class BoutonCase(Button):
    def __init__(self, parent, x: int, y: int, commande):
        self.x = x
        self.y = y
        super().__init__(
            parent,
            font = Font.BODY,
            text = "",
            padx = 0,
            pady = 0,
            width = 0,
            height = 0,
            command = commande,
            bg = "white",
            border = 0,
            )
        self.grid(row = x, column = y)

    def setType(self, type: TypeCase):
        match type:
            case TypeCase.POINT_A:
                self["text"] = "◐"
            case TypeCase.POINT_B:
                self["text"] = "◑"
            case TypeCase.DEPART:
                self["text"] = "▢"
            case TypeCase.ARRIVEE:
                self["text"] = "▲"
            case TypeCase.MUR:
                if self.x % 2 == 0:
                    self["text"] = "━"
                else:
                    self["text"] = "┃"
            case TypeCase.MUR_VIDE:
                self["text"] = ""
            case TypeCase.VIDE:
                self["text"] = "▪"
            case _:
                pass

