from tkinter import Frame, Label
from typing import Callable

from .symbole import Symbole

from model.ligne import Ligne
from model.root import Root
from constants.config import GridPad, Font


class Conclusion(Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            )
        self.grid(padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)
        self.root: Root | None = None

    def do(self):
        if(self.root is not None):
            self.root.destroy()
        self.root = Root(self, 0)

    def setText(self, solutions: list[list[tuple[str, str, bool, Callable[[], None]]]] = None, unique: bool = False):
        self.do()
        if solutions is None:
            Label(self.root, font = Font.BODY_SYMBOLE, text = "Solution indéterminée...").grid()
            return
        texte = "Solution unique:" if unique else "Solutions possibles:"
        Label(self.root, font = Font.BODY_SYMBOLE, text = texte).grid(row = 0)
        for row, solution in enumerate(solutions):
            Ligne(self.root, row+1, solution, lambda parent, col, args: Symbole(parent, col, *args))
