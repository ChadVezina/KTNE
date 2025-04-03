from tkinter import Frame, Entry, StringVar
from constants.config import GridPad, Font

class Input(Entry):
    def __init__(
        self,
        parent: Frame,
        row: int,
        col: int = 0,
        ):
        self.sv = StringVar()
        super().__init__(
            parent,
            font = Font.BODY,
            textvariable = self.sv,
            bg = "white",
            )
        self.grid(
            row = row,
            column = col,
            padx = GridPad.PADDING_X,
            pady = GridPad.PADDING_Y,
            )

    def get_texte(self) -> str | None:
        return self.sv.get().lower().strip()

    def is_exist(self) -> None:
        self["bg"] = "green"

    def is_not_exist(self) -> None:
        self["bg"] = "white"
