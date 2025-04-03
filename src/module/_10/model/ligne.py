from tkinter import Frame, Label

from ..tools.constantes import Font, TextPad


class Ligne(Frame):
    def __init__(self, parent, row, solution: list[str]):
        super().__init__(
            parent,
            )
        self.grid(row=row)
        for col, texte in enumerate(solution):
            Label(
                self,
                font=Font.BODY,
                text=texte,
                padx=TextPad.PADDING_X,
                pady=TextPad.PADDING_Y,
            ).grid(row=row, column=col)
