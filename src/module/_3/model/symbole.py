from tkinter import Button
from typing import Callable

from ..tools.constantes import Font, TextPad


class Symbole:
    def __init__(self, parent, col, texte, hint, selected, commande: Callable[[], None]):
        self.bouton = Button(
            parent,
            font=Font.BODY_SYMBOLE,
            text=texte,
            padx=TextPad.PADDING_X,
            pady=TextPad.PADDING_Y,
            relief="sunken" if selected else "flat",
            command=commande,
            )
        self.hint = Button(
            parent,
            font=Font.BODY_HINT,
            text=hint,
            padx=TextPad.PADDING_X,
            pady=TextPad.PADDING_Y,
            relief="solid" if selected else "flat",
            command=commande,
            )
        self.bouton.grid(row=0, column=col)
        self.hint.grid(row=1, column=col)
