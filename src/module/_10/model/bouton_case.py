from model.bouton import Bouton
from ..tools.enums import TypeCase


class BoutonCase(Bouton):
    def __init__(self, parent, x: int, y: int, commande):
        self.condition = x % 2 == 0
        super().__init__(parent, x, y, commande=commande, border=0, no_padding=True, no_margin=True, no_color=True)

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
                if self.condition:
                    self["text"] = "━"
                else:
                    self["text"] = "┃"
            case TypeCase.MUR_VIDE:
                self["text"] = ""
            case TypeCase.VIDE:
                self["text"] = "▪"
            case _:
                return

