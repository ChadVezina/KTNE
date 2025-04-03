from tkinter import Label

from ..tools.constantes import Font, TextPad


class Symbole:
    def __init__(self, parent, col, texte, hint, selected):
        self.bouton = Label(
            parent,
            font=Font.BODY,
            text=texte,
            padx=TextPad.PADDING_X,
            pady=TextPad.PADDING_Y,
            relief="sunken" if selected else "flat",
            )
        self.hint = Label(
            parent,
            font=Font.BODY3,
            text=hint,
            padx=TextPad.PADDING_X,
            pady=TextPad.PADDING_Y,
            relief="solid" if selected else "flat",
            )
        self.bouton.grid(row=0, column=col)
        self.hint.grid(row=1, column=col)
