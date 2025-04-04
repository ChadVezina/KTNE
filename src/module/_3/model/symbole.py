from typing import Callable

from model.bouton import Bouton
from constants.config import Font


class Symbole:
    def __init__(self, parent, col, texte, hint, selected, commande: Callable[[], None]):
        self.bouton = Bouton(
            parent,
            0,
            col,
            texte,
            commande,
            Font.BODY_SYMBOLE,
            "sunken" if selected else "flat",
            no_color=True,
            )
        self.hint = Bouton(
            parent,
            1,
            col,
            hint,
            commande,
            Font.BODY_HINT,
            "solid" if selected else "flat",
            no_color=True,
            )
