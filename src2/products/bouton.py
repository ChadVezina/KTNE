from tkinter import Frame, Button
from typing import Callable, Literal;
from constants.config import GridPad, BoutonCaseRect, Font

class Bouton(Button):
    def __init__(
        self,
        parent: Frame,
        row: int = 0,
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
        visible: bool = True,
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
        self.row = row
        self.col = col
        self.padx = 0 if no_margin else GridPad.PADDING_X
        self.pady = 0 if no_margin else GridPad.PADDING_Y
        if visible:
            self.grid(
                row = row,
                column = col,
                padx = self.padx,
                pady = self.pady,
                )

    def add_command(self, commande: Callable[[], None]) -> None:
        self["command"] = lambda: commande()

    def hide(self) -> None:
        if self.winfo_ismapped():
            self.grid_remove()

    def show(self) -> None:
        self.hide()
        self.grid(row = self.row, column = self.col, padx = self.padx, pady = self.pady)

    def place(self, row: int = -1, col: int = -1) -> None:
        if row != -1:
            self.row = row
        if col != -1:
            self.col = col
        self.show()
