from .model.next_link import NextLink
from constants.fenetre import Titre
from constants.instructions import Contenu
from tools.module import Module


class Module_2(Module):
    def __init__(self, root, geometrie):
        self.next_link = NextLink(
            "Bouton est ...?",
            {
                0: "bleu",
                1: "\"Annuler\"",
                },
            [
                lambda liste_1: NextLink(
                    "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                    {
                        0: "bleu",
                        1: "blanc",
                        2: "jaune",
                        },
                    [
                        lambda liste: NextLink(
                            "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                            ) if 0 in liste else NextLink(
                            "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                            ) if 2 in liste else NextLink(
                            "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                            ),
                    ],
                    False,
                    ) if 0 in liste_1 and 1 in liste_1 else NextLink(
                    "Combien de piles? Bouton est ...?",
                    {
                        0: "plus qu'une",
                        1: "\"Exploser\"",
                        },
                    [
                        lambda liste_2: NextLink(
                            "Appuyer et immédiatement relâcher le bouton",
                            ) if 0 in liste_2 and 1 in liste_2 else NextLink(
                            "Bouton est ...? Indicateur est ...?" if not 0 in liste_1 else "Indicateur est ...?",
                            {
                                0: "blanc",
                                1: "allumé avec \"CAR\"",
                                } if not 0 in liste_1 else {
                                0: "allumé avec \"CAR\"",
                                },
                            [
                                lambda liste_3: NextLink(
                                    "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                    {
                                        0: "bleu",
                                        1: "blanc",
                                        2: "jaune",
                                        },
                                    [
                                        lambda liste: NextLink(
                                            "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                            ) if 0 in liste else NextLink(
                                            "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                            ) if 2 in liste else NextLink(
                                            "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                            ),
                                    ],
                                    False,
                                    ) if 0 in liste_3 and 1 in liste_3 else NextLink(
                                    "Combien de piles? Indicateur est ...?",
                                    {
                                        0: "plus que 2",
                                        1: "allumé avec \"FRK\"",
                                        },
                                    [
                                        lambda liste_4: NextLink(
                                            "Appuyer et immédiatement relâcher le bouton",
                                            ) if 0 in liste_4 and 1 in liste_4 else NextLink(
                                            "Bouton est ...?",
                                            {
                                                0: "jaune",
                                                },
                                            [
                                                lambda liste_5: NextLink(
                                                    "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                                    {
                                                        0: "bleu",
                                                        1: "blanc",
                                                        2: "jaune",
                                                        },
                                                    [
                                                        lambda liste: NextLink(
                                                            "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                                            ) if 0 in liste else NextLink(
                                                            "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                                            ) if 2 in liste else NextLink(
                                                            "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                                            ),
                                                    ],
                                                    False,
                                                    ) if 0 in liste_5 else NextLink(
                                                    "Bouton est ...?",
                                                    {
                                                        0: "rouge",
                                                        1: "\"Maintenir\"",
                                                        },
                                                    [
                                                        lambda liste_6: NextLink(
                                                            "Appuyer et immédiatement relâcher le bouton",
                                                            ) if 0 in liste_6 and 1 in liste_6 else NextLink(
                                                            "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                                            {
                                                                0: "bleu",
                                                                1: "blanc",
                                                                2: "jaune",
                                                                },
                                                            [
                                                                lambda liste: NextLink(
                                                                    "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                                                    ) if 0 in liste else NextLink(
                                                                    "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                                                    ) if 2 in liste else NextLink(
                                                                    "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                                                    ),
                                                            ],
                                                            False,
                                                            ),
                                                    ],
                                                    ) if not 0 in liste_1 and not 0 in liste_3 and not 1 in liste_1 and not 1 in liste_2 else NextLink(
                                                    "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                                    {
                                                        0: "bleu",
                                                        1: "blanc",
                                                        2: "jaune",
                                                        },
                                                    [
                                                        lambda liste: NextLink(
                                                            "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                                            ) if 0 in liste else NextLink(
                                                            "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                                            ) if 2 in liste else NextLink(
                                                            "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                                            ),
                                                    ],
                                                    False,
                                                    ),
                                            ],
                                            ) if not 0 in liste_1 and not 0 in liste_3 else NextLink(
                                            "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                            {
                                                0: "bleu",
                                                1: "blanc",
                                                2: "jaune",
                                                },
                                            [
                                                lambda liste: NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                                    ) if 0 in liste else NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                                    ) if 2 in liste else NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                                    ),
                                            ],
                                            False,
                                            ),
                                    ],
                                    ) if not 1 in liste_3 and 0 in liste_2 else NextLink(
                                    "Bouton est ...?",
                                    {
                                        0: "jaune",
                                        },
                                    [
                                        lambda liste_5: NextLink(
                                            "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                            {
                                                0: "bleu",
                                                1: "blanc",
                                                2: "jaune",
                                                },
                                            [
                                                lambda liste: NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                                    ) if 0 in liste else NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                                    ) if 2 in liste else NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                                    ),
                                            ],
                                            False,
                                            ) if 0 in liste_5 else NextLink(
                                            "Bouton est ...?",
                                            {
                                                0: "rouge",
                                                1: "\"Maintenir\"",
                                                },
                                            [
                                                lambda liste_6: NextLink(
                                                    "Appuyer et immédiatement relâcher le bouton",
                                                    ) if 0 in liste_6 and 1 in liste_6 else NextLink(
                                                    "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                                    {
                                                        0: "bleu",
                                                        1: "blanc",
                                                        2: "jaune",
                                                        },
                                                    [
                                                        lambda liste: NextLink(
                                                            "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                                            ) if 0 in liste else NextLink(
                                                            "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                                            ) if 2 in liste else NextLink(
                                                            "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                                            ),
                                                    ],
                                                    False,
                                                    ),
                                            ],
                                            ) if not 0 in liste_1 and not 0 in liste_3 and not 1 in liste_1 and not 1 in liste_2 else NextLink(
                                            "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                            {
                                                0: "bleu",
                                                1: "blanc",
                                                2: "jaune",
                                                },
                                            [
                                                lambda liste: NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                                    ) if 0 in liste else NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                                    ) if 2 in liste else NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                                    ),
                                            ],
                                            False,
                                            ),
                                    ],
                                    ) if not 0 in liste_1 and not 0 in liste_3 else NextLink(
                                    "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                    {
                                        0: "bleu",
                                        1: "blanc",
                                        2: "jaune",
                                        },
                                    [
                                        lambda liste: NextLink(
                                            "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                            ) if 0 in liste else NextLink(
                                            "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                            ) if 2 in liste else NextLink(
                                            "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                            ),
                                    ],
                                    False,
                                    ),
                            ],
                            ),
                    ],
                    ) if not 1 in liste_1 else NextLink(
                    "Bouton est ...? Indicateur est ...?" if not 0 in liste_1 else "Indicateur est ...?",
                    {
                        0: "blanc",
                        1: "allumé avec \"CAR\"",
                        } if not 0 in liste_1 else {
                        0: "allumé avec \"CAR\"",
                        },
                    [
                        lambda liste_3: NextLink(
                            "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                            {
                                0: "bleu",
                                1: "blanc",
                                2: "jaune",
                                },
                            [
                                lambda liste: NextLink(
                                    "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                    ) if 0 in liste else NextLink(
                                    "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                    ) if 2 in liste else NextLink(
                                    "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                    ),
                            ],
                            False,
                            ) if 0 in liste_3 and 1 in liste_3 else NextLink(
                            "Combien de piles? Indicateur est ...?",
                            {
                                0: "plus que 2",
                                1: "allumé avec \"FRK\"",
                                },
                            [
                                lambda liste_4: NextLink(
                                    "Appuyer et immédiatement relâcher le bouton",
                                    ) if 0 in liste_4 and 1 in liste_4 else NextLink(
                                    "Bouton est ...?",
                                    {
                                        0: "jaune",
                                        },
                                    [
                                        lambda liste_5: NextLink(
                                            "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                            {
                                                0: "bleu",
                                                1: "blanc",
                                                2: "jaune",
                                                },
                                            [
                                                lambda liste: NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                                    ) if 0 in liste else NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                                    ) if 2 in liste else NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                                    ),
                                            ],
                                            False,
                                            ) if 0 in liste_5 else NextLink(
                                            "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                            {
                                                0: "bleu",
                                                1: "blanc",
                                                2: "jaune",
                                                },
                                            [
                                                lambda liste: NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                                    ) if 0 in liste else NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                                    ) if 2 in liste else NextLink(
                                                    "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                                    ),
                                            ],
                                            False,
                                            ),
                                    ],
                                    ) if not 0 in liste_1 and not 0 in liste_3 else NextLink(
                                    "Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?",
                                    {
                                        0: "bleu",
                                        1: "blanc",
                                        2: "jaune",
                                        },
                                    [
                                        lambda liste: NextLink(
                                            "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
                                            ) if 0 in liste else NextLink(
                                            "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
                                            ) if 2 in liste else NextLink(
                                            "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
                                            ),
                                    ],
                                    False,
                                    ),
                            ],
                            ),
                    ],
                    ),
            ],
        )

        super().__init__(Titre.MODULE_2, Contenu.MODULE_2, root, geometrie)

    def redessiner(self):
        self.next_link.do(self.cadre, 0)
