from tkinter import Frame, Entry, StringVar
from typing import Callable
from constants.config import GridPad, Font

class Input(Entry):
    def __init__(
        self,
        parent: Frame,
        row: int,
        col: int = 0,
        commande: Callable[[], None] = None,
        font = Font.BODY,
        no_margin: bool = False,
        ):
        self.sv = StringVar()
        super().__init__(
            parent,
            font = font,
            textvariable = self.sv,
            bg = "white",
            )
        self.grid(
            row = row,
            column = col,
            padx = 0 if no_margin else GridPad.PADDING_X,
            pady = 0 if no_margin else GridPad.PADDING_Y,
            )
        if commande is not None:
            self.bind("<KeyRelease>", lambda e: commande())

    def get_texte(self) -> str | None:
        return self.sv.get().lower().strip()

    def is_exist(self) -> None:
        self["bg"] = "green"

    def is_not_exist(self) -> None:
        self["bg"] = "white"
