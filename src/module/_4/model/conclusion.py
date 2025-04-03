from tkinter import Frame, Label

from .ligne import Ligne

from ..tools.constantes import GridPad, Font


class Conclusion(Frame):
    def __init__(self, parent: Frame, row: int, solutions: list[str], split_col = 1):
        super().__init__(
            parent,
            )
        self.grid(padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        self.setText(solutions, split_col)

    def setText(self, solutions: list[str], split_col = 1):
        texte = "Appuyer sur ce(s) bouton(s):"
        Label(self, font=Font.BODY, text=texte).grid(row=0)
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
                Ligne(self, row+1, sub_liste)
