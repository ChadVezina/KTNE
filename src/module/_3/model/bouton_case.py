from model.bouton import Bouton
from constants.config import Font


class BoutonCase(Bouton):
    def __init__(self, parent, x, y, texte, commande):
        super().__init__(
            parent,
            x,
            y,
            texte,
            commande,
            Font.BODY_SYMBOLE,
            no_margin = True,
            )

