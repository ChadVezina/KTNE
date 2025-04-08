from tkinter import Frame
from typing import Callable, TypeVar


T = TypeVar("T")


class Ligne(Frame):
    def __init__(self, parent, row, solution: list[T], create_commande: Callable[[Frame, int, T], None]):
        super().__init__(
            parent,
            )
        self.grid(row = row)
        for col, args in enumerate(solution):
            create_commande(self, col, args)
