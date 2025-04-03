from tkinter import Frame, Label

from .ligne import Ligne
from .root import Root

from ..tools.constantes import GridPad, Font


class Conclusion(Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            )
        self.grid(padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        self.root: Root | None = None

    def do(self):
        if(self.root is not None):
            self.root.destroy()
        self.root = Root(self, 0)

    def prepare(self):
        self.do()
        Label(self.root, font=Font.BODY, text="Chargement...").grid()

    def setText(self, solutions: list[str] = None, split_col = 1):
        self.do()
        if solutions is None:
            Label(self.root, font=Font.BODY, text="Solution indéterminée...").grid()
            return
        liste = enumerate(solutions)
        for row, solution in liste:
            sub_liste: list[str] = []
            sub_liste.append(solution)
            for _ in range(split_col-1):
                try:
                    next_solution = liste.__next__()[1]
                    sub_liste.append("->")
                    sub_liste.append(next_solution)
                except StopIteration:
                    break
            if len(sub_liste) != 0:
                if row < len(solutions) - split_col:
                    sub_liste.append("->")
                Ligne(self.root, row, sub_liste)
