from tkinter import Frame

from .symbole import Symbole


class Ligne(Frame):
    def __init__(self, parent, row, solution: list[tuple[str, str, bool]]):
        super().__init__(
            parent,
            )
        self.grid(row=row)
        for col, (texte, hint, selected) in enumerate(solution):
            Symbole(self, col, texte, hint, selected)
