from tkinter import Frame
from typing import Callable

from .symbole import Symbole


class Ligne(Frame):
    def __init__(self, parent, row, solution: list[tuple[str, str, bool, Callable[[], None]]]):
        super().__init__(
            parent,
            )
        self.grid(row=row)
        for col, (texte, hint, selected, commande) in enumerate(solution):
            Symbole(self, col, texte, hint, selected, commande)
