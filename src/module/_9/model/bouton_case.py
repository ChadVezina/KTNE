from model.bouton import Bouton


class BoutonCase(Bouton):
    def __init__(self, parent, x, y, texte, commande):
        super().__init__(
            parent,
            x,
            y,
            texte,
            commande = commande,
            no_margin=True,
            )

