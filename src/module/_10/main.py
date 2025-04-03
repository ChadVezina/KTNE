from .model.next_link import NextLink
from .tools.enums import TypeTableau
from constants.fenetre import Titre
from constants.instructions import Contenu
from model.module import Module


class Module_10(Module):
    def __init__(self, root, geometrie):
        self.next_link = NextLink(
            "Premier cas qui semble être vrai?",
            {
                0: "même rangée/même colonne?\n\nmême rangée",
                1: "même rangée/même colonne?\n\nmême colonne 1",
                2: "même rangée/même colonne?\n\nmême colonne 2",

                3: "symétrie colonnes?\n\npremière et dernière colonne",
                4: "symétrie colonnes?\n\n2e et avant-dernière colonne",
                5: "symétrie colonnes?\n\nles colonnes du centre",

                6: "sinon,\n\ncontient 1 première rangée",
                7: "sinon,\n\ncontient 1 dernière rangée",
                8: "sinon,\n\ncontient 1 première colonne",
                },
            [
                lambda scan: TypeTableau._2 if 0 = = scan else None,
                lambda scan: TypeTableau._3 if 1 = = scan else None,
                lambda scan: TypeTableau._6 if 2 = = scan else None,
                lambda scan: TypeTableau._0 if 3 = = scan else None,
                lambda scan: TypeTableau._1 if 4 = = scan else None,
                lambda scan: TypeTableau._7 if 5 = = scan else None,
                lambda scan: TypeTableau._5 if 6 = = scan else None,
                lambda scan: TypeTableau._4 if 7 = = scan else None,
                lambda scan: TypeTableau._8 if 8 = = scan else None,
            ],
        )

        super().__init__(Titre.MODULE_10, Contenu.MODULE_10, root, geometrie)

    def redessiner(self):
        self.next_link.do(self.cadre, 0)
