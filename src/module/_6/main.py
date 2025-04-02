from .model.next_link import NextLink
from .tools.fonctions import make_menu
from constants.fenetre import Titre
from tools.module import Module


def switch_case(scan: int, a: int | None, b: int | None, c: int | None, d: int | None):
    if scan == 0:
        return a
    elif scan == 1:
        return b
    elif scan == 2:
        return c
    elif scan == 3:
        return d
    return None


class Module_6(Module):
    def __init__(self, root, geometrie):
        super().__init__(root, geometrie)

        self.title(Titre.MODULE_6.value)

        self.next_link = NextLink(
            "Étape 1: L'écran affiche ...?",
            [
                lambda historique, scan: NextLink(
                    None,
                    [
                        lambda historique, scan: NextLink(
                            "Étape 2: L'écran affiche ...?",
                            [
                                lambda historique, scan: NextLink(
                                    None,
                                    [
                                        lambda historique, scan: NextLink(
                                            "Étape 3: L'écran affiche ...?",
                                            [
                                                lambda historique, scan: NextLink(
                                                    None,
                                                    [
                                                        lambda historique, scan: NextLink(
                                                            "Étape 4: L'écran affiche ...?",
                                                            [
                                                                lambda historique, scan: NextLink(
                                                                    None,
                                                                    [
                                                                        lambda historique, scan: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            [
                                                                                lambda historique, scan: NextLink(
                                                                                    "Appuyez sur le bouton portant le chiffre \'{}\'".format(
                                                                                        switch_case(scan, historique[0][1], historique[1][1], historique[3][1], historique[2][1])
                                                                                        ),
                                                                                ) if scan != -1 else None,
                                                                            ],
                                                                        ) if scan != -1 else None,
                                                                    ],
                                                                    switch_case(scan, historique[0][0], 1, historique[1][0], historique[1][0]),
                                                                ) if scan != -1 else None,
                                                            ],
                                                        ) if scan != -1 else None,
                                                    ],
                                                    switch_case(scan, None, None, 3, None),
                                                    switch_case(scan, historique[1][1], historique[0][1], None, 4),
                                                ) if scan != -1 else None,
                                            ],
                                        ) if scan != -1 else None,
                                    ],
                                    switch_case(scan, None, historique[0][0], 1, historique[0][0]),
                                    switch_case(scan, 4, None, None, None),
                                ) if scan != -1 else None,
                            ],
                        ) if scan != -1 else None,
                    ],
                    switch_case(scan, 2, 2, 3, 4),
                ) if scan != -1 else None,
            ],
        )

        make_menu(self, self.nouvelle_partie, self.quitter)

        self.ouvrir_partie()

    def redessiner(self):
        self.next_link.undo()
        self.next_link.do(self.cadre, 0)
