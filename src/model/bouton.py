from tkinter import Frame, Button
from typing import Callable, Literal;
from constants.config import GridPad, BoutonCaseRect, Font

class Bouton(Button):
    def __init__(
        self,
        parent: Frame,
        row: int,
        col: int = 0,
        texte: str = "",
        commande: Callable[[], None] = None,
        font = Font.BODY,
        relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = "raised",
        border: str | float = None,
        wraplength: str | float = None,
        no_margin: bool = False,
        no_padding: bool = False,
        no_color: bool = False,
        ):
        super().__init__(
            parent,
            font = font,
            text = texte,
            padx = 0 if no_padding else BoutonCaseRect.PADDING_X,
            pady = 0 if no_padding else BoutonCaseRect.PADDING_Y,
            command = commande,
            bg = None if no_color else "white",
            relief = relief,
            border = border,
            wraplength = wraplength,
            )
        self.grid(
            row = row,
            column = col,
            padx = 0 if no_margin else GridPad.PADDING_X,
            pady = 0 if no_margin else GridPad.PADDING_Y,
            )

    def add_command(self, commande: Callable[[], None]) -> None:
        self["command"] = lambda: commande()

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
