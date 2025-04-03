from tkinter import Frame, Button, _Relief, _ButtonCommand
from typing import Callable
from constants.config import GridPad, BoutonCaseRect, Font

class Bouton(Button):
    def __init__(
        self,
        parent: Frame,
        row: int,
        col: int = 0,
        texte: str = "",
        commande: Callable[[], None] = None,
        relief: _Relief = "sunken",
        ):
        super().__init__(
            parent,
            font = Font.BODY,
            text = texte,
            padx = BoutonCaseRect.PADDING_X,
            pady = BoutonCaseRect.PADDING_Y,
            command = commande,
            bg = "white",
            relief = relief,
            )
        self.grid(
            row = row,
            column = col,
            padx = GridPad.PADDING_X,
            pady = GridPad.PADDING_Y,
            )

    def add_command(self, commande: _ButtonCommand) -> None:
        self["command"] = commande

    def get_texte(self) -> str:
        return self.cget("text")

    def set_texte(self, texte: str) -> None:
        self["text"] = texte

    def is_exist(self) -> None:
        self["bg"] = "green"

    def is_not_exist(self) -> None:
        self["bg"] = "white"

    def set_active(self, active: bool) -> None:
        if active:
            self.config(relief = "sunken")
        else:
            self.config(relief = "raised")

    def activer(self) -> None:
        self["bg"] = "pink"

    def desactiver(self) -> None:
        self["bg"] = "white"
