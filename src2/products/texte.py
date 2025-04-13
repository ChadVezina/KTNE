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
        visible: bool = True,
        ):
        super().__init__(
            parent,
            font = font,
            text = texte,
            width = width,
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
