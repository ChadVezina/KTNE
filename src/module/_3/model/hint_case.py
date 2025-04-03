from tkinter import Label

from constants.config import HintCaseRect, Font


class HintCase(Label):
    def __init__(self, parent, x, y, texte):
        self.x = x
        self.y = y
        super().__init__(
            parent,
            font=Font.BODY_HINT,
            text=texte,
            width=HintCaseRect.WIDTH,
            wraplength=HintCaseRect.WRAP_LENGTH,
            )
        self.grid(row=x, column=y)

