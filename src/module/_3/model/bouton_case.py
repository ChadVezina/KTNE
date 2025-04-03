from tkinter import Button

from constants.config import BoutonCaseRect, Font


class BoutonCase(Button):
    def __init__(self, parent, x, y, texte, commande):
        self.x = x
        self.y = y
        super().__init__(
            parent,
            font=Font.BODY_SYMBOLE,
            text=texte,
            padx=BoutonCaseRect.PADDING_X,
            pady=BoutonCaseRect.PADDING_Y,
            width=BoutonCaseRect.WIDTH,
            height=BoutonCaseRect.HEIGHT,
            command=commande,
            bg="white",
            )
        self.grid(row=x, column=y)

    def activer(self):
        self["bg"] = "pink"

    def desactiver(self):
        self["bg"] = "white"

