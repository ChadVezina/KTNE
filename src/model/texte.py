from tkinter import Frame, Label
from constants.config import GridPad, Font

class Texte(Label):
    def __init__(
        self,
        parent: Frame,
        row: int = 0,
        col: int = 0,
        texte: str = "",
        font = Font.BODY,
        width: str | float = None,
        wraplength: str | float = None,
        no_margin: bool = False,
        ):
        super().__init__(
            parent,
            font = font,
            text = texte,
            width = width,
            wraplength = wraplength,
            )
        self.grid(
            row = row,
            column = col,
            padx = 0 if no_margin else GridPad.PADDING_X,
            pady = 0 if no_margin else GridPad.PADDING_Y,
            )

    def get_texte(self) -> str:
        return self.cget("text")

    def set_texte(self, texte: str) -> None:
        self["text"] = texte

    def clear_texte(self) -> None:
        self["text"] = ""

    def activer(self) -> None:
        self["bg"] = "pink"

    def desactiver(self) -> None:
        self["bg"] = "white"
