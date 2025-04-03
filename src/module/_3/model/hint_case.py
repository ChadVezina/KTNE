from tkinter import Label

from tools.constants import BoutonCaseRect, Font


class HintCase(Label):
    def __init__(self, parent, x, y, texte):
        self.x = x
        self.y = y
        multi = 2
        taille = 9
        width = (BoutonCaseRect.WIDTH+BoutonCaseRect.PADDING_X*2)*multi
        super().__init__(
            parent,
            font=Font.BODY_HINT,
            text=texte,
            width=width,
            wraplength=width*taille,
            )
        self.grid(row=x, column=y)

