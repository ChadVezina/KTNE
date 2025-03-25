from tkinter import Label

from ..tools.constantes import GridPad, Font


class Conclusion(Label):
    def __init__(self, parent, texte):
        super().__init__(
            parent,
            font=Font.BODY,
            text=texte,
            )
        self.grid(padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)

    def setText(self, texte):
        self["text"] = texte

