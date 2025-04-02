from .model.next_link import NextLink
from .tools.fonctions import make_menu
from constants.fenetre import Titre
from tools.module import Module


class Module_4(Module):
    def __init__(self, root, geometrie):
        super().__init__(root, geometrie)

        self.title(Titre.MODULE_4.value)

        self.next_link = NextLink(
            "Combien de voyelles contient le numéro de série?",
            {
                0: "0",
                },
            [
                lambda liste_1: NextLink(
                    "Combien d'erreurs?",
                    {
                        0: "0",
                        1: "1",
                        2: "2",
                        },
                    [
                        lambda liste_2: NextLink(
                            "Quelle couleur flash?",
                            {
                                0: "rouge",
                                1: "bleu",
                                2: "vert",
                                3: "jaune",
                                },
                            [
                                lambda liste: NextLink(
                                    "rouge",
                                    ) if(
                                        (0 == liste_1 and (
                                            (0 == liste_2 and 3 == liste) or
                                            (1 == liste_2 and 0 == liste) or
                                            (2 == liste_2 and 3 == liste)
                                            )) or
                                        (not 0 == liste_1 and (
                                            (0 == liste_2 and 1 == liste) or
                                            (1 == liste_2 and 3 == liste) or
                                            (2 == liste_2 and 1 == liste)
                                            ))
                                        ) else None,
                                lambda liste: NextLink(
                                    "bleu",
                                    ) if(
                                        (0 == liste_1 and (
                                            (0 == liste_2 and 0 == liste) or
                                            (1 == liste_2 and 1 == liste) or
                                            (2 == liste_2 and 2 == liste)
                                            )) or
                                        (not 0 == liste_1 and (
                                            (0 == liste_2 and 0 == liste) or
                                            (1 == liste_2 and 2 == liste) or
                                            (2 == liste_2 and 3 == liste)
                                            ))
                                        ) else None,
                                lambda liste: NextLink(
                                    "vert",
                                    ) if(
                                        (0 == liste_1 and (
                                            (0 == liste_2 and 2 == liste) or
                                            (1 == liste_2 and 3 == liste) or
                                            (2 == liste_2 and 1 == liste)
                                            )) or
                                        (not 0 == liste_1 and (
                                            (0 == liste_2 and 3 == liste) or
                                            (1 == liste_2 and 1 == liste) or
                                            (2 == liste_2 and 0 == liste)
                                            ))
                                        ) else None,
                                lambda liste: NextLink(
                                    "jaune",
                                    ) if(
                                        (0 == liste_1 and (
                                            (0 == liste_2 and 1 == liste) or
                                            (1 == liste_2 and 2 == liste) or
                                            (2 == liste_2 and 0 == liste)
                                            )) or
                                        (not 0 == liste_1 and (
                                            (0 == liste_2 and 2 == liste) or
                                            (1 == liste_2 and 0 == liste) or
                                            (2 == liste_2 and 2 == liste)
                                            ))
                                        ) else None,
                            ],
                            ),
                    ],
                    ),
            ],
        )

        make_menu(self, self.nouvelle_partie, self.quitter)

        self.ouvrir_partie()

    def redessiner(self):
        self.next_link.undo()
        self.next_link.do(self.cadre, 0)
