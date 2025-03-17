from tkinter import Frame, messagebox, Toplevel, CENTER

from .model.next_link import NextLink
from .tools.fonctions import make_menu
from .tools.constantes import FenetrePad
from constants.fenetre import Titre


class Module_6(Toplevel):
    def __init__(self, root, geometrie):
        super().__init__(root)

        self.title(Titre.MODULE_6.value)
        self.geometry(geometrie)
        self.resizable(True, True)

        self.next_link = NextLink(
            "Étape 1: L'écran affiche ...?",
            {
                0: "1",
                1: "2",
                2: "3",
                3: "4",
                },
            [
                lambda liste_1: NextLink(
                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                    {
                        0: "1",
                        1: "2",
                        2: "3",
                        3: "4",
                        },
                    [
                        lambda liste_2: NextLink(
                            "Étape 2: L'écran affiche ...?",
                            {
                                0: "1",
                                1: "2",
                                2: "3",
                                3: "4",
                                },
                            [
                                lambda liste_3: NextLink(
                                    "Quelle est la position du bouton portant le chiffre \'4\'? ...et appuyez dessus",
                                    {
                                        0: "1",
                                        1: "2",
                                        2: "3",
                                        3: "4",
                                        },
                                    [
                                        lambda liste_4: NextLink(
                                            "Étape 3: L'écran affiche ...?",
                                            {
                                                0: "1",
                                                1: "2",
                                                2: "3",
                                                3: "4",
                                                },
                                            [
                                                lambda liste_5: NextLink(
                                                    f"Quelle est la position du bouton portant le chiffre \'{4 if 0 in liste_5 else liste_2[0]+1}\'? ...et appuyez dessus",
                                                    {
                                                        0: "1",
                                                        1: "2",
                                                        2: "3",
                                                        3: "4",
                                                        },
                                                    [
                                                        lambda liste_6: NextLink(
                                                            "Étape 4: L'écran affiche ...?",
                                                            {
                                                                0: "1",
                                                                1: "2",
                                                                2: "3",
                                                                3: "4",
                                                                },
                                                            [
                                                                lambda liste_7: NextLink(
                                                                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    f"Appuyer sur {liste_2[0]+1}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur 4?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur 1?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    f"Appuyer sur {4 if 0 in liste_5 else liste_2[0]+1}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en 1re position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    f"Appuyer sur {liste_2[0]+1}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur 4?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur 2?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    f"Appuyer sur {4 if 0 in liste_5 else liste_2[0]+1}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 1 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    f"Quelle est la valeur du bouton en {liste_4[0]}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    f"Appuyer sur {liste_2[0]+1}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur 4?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    f"Appuyer sur {liste_7[0]+1}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    f"Appuyer sur {4 if 0 in liste_5 else liste_2[0]+1}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 2 in liste_7 or 3 in liste_7 else None,
                                                            ],
                                                            False,
                                                            ),
                                                    ],
                                                    False,
                                                    ) if 0 in liste_5 or 1 in liste_5 else None,
                                                lambda liste_5: NextLink(
                                                    "Quelle est la valeur du bouton en 3e position? ...et appuyez dessus",
                                                    {
                                                        0: "1",
                                                        1: "2",
                                                        2: "3",
                                                        3: "4",
                                                        },
                                                    [
                                                        lambda liste_6: NextLink(
                                                            "Étape 4: L'écran affiche ...?",
                                                            {
                                                                0: "1",
                                                                1: "2",
                                                                2: "3",
                                                                3: "4",
                                                                },
                                                            [
                                                                lambda liste_7: NextLink(
                                                                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en 1re position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en {}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                            ],
                                                            False,
                                                            ),
                                                    ],
                                                    False,
                                                    ) if 2 in liste_5 else None,
                                                lambda liste_5: NextLink(
                                                    "Quelle est la position du bouton portant le chiffre \'4\'? ...et appuyez dessus",
                                                    {
                                                        0: "1",
                                                        1: "2",
                                                        2: "3",
                                                        3: "4",
                                                        },
                                                    [
                                                        lambda liste_6: NextLink(
                                                            "Étape 4: L'écran affiche ...?",
                                                            {
                                                                0: "1",
                                                                1: "2",
                                                                2: "3",
                                                                3: "4",
                                                                },
                                                            [
                                                                lambda liste_7: NextLink(
                                                                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en 1re position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en {}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                            ],
                                                            False,
                                                            ),
                                                    ],
                                                    False,
                                                    ) if 3 in liste_5 else None,
                                            ],
                                            False,
                                            ),
                                    ],
                                    False,
                                    ) if 0 in liste_3 else None,
                                lambda liste_3: NextLink(
                                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                                    {
                                        0: "1",
                                        1: "2",
                                        2: "3",
                                        3: "4",
                                        },
                                    [
                                        lambda liste_4: NextLink(
                                            "Étape 3: L'écran affiche ...?",
                                            {
                                                0: "1",
                                                1: "2",
                                                2: "3",
                                                3: "4",
                                                },
                                            [
                                                lambda liste_5: NextLink(
                                                    "Quelle est la position du bouton portant le chiffre \'{}\'? ...et appuyez dessus",
                                                    {
                                                        0: "1",
                                                        1: "2",
                                                        2: "3",
                                                        3: "4",
                                                        },
                                                    [
                                                        lambda liste_6: NextLink(
                                                            "Étape 4: L'écran affiche ...?",
                                                            {
                                                                0: "1",
                                                                1: "2",
                                                                2: "3",
                                                                3: "4",
                                                                },
                                                            [
                                                                lambda liste_7: NextLink(
                                                                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en 1re position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en {}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                            ],
                                                            False,
                                                            ),
                                                    ],
                                                    False,
                                                    ) if 0 in liste_5 or 1 in liste_5 else None,
                                                lambda liste_5: NextLink(
                                                    "Quelle est la valeur du bouton en 3e position? ...et appuyez dessus",
                                                    {
                                                        0: "1",
                                                        1: "2",
                                                        2: "3",
                                                        3: "4",
                                                        },
                                                    [
                                                        lambda liste_6: NextLink(
                                                            "Étape 4: L'écran affiche ...?",
                                                            {
                                                                0: "1",
                                                                1: "2",
                                                                2: "3",
                                                                3: "4",
                                                                },
                                                            [
                                                                lambda liste_7: NextLink(
                                                                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en 1re position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en {}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                            ],
                                                            False,
                                                            ),
                                                    ],
                                                    False,
                                                    ) if 2 in liste_5 else None,
                                                lambda liste_5: NextLink(
                                                    "Quelle est la position du bouton portant le chiffre \'4\'? ...et appuyez dessus",
                                                    {
                                                        0: "1",
                                                        1: "2",
                                                        2: "3",
                                                        3: "4",
                                                        },
                                                    [
                                                        lambda liste_6: NextLink(
                                                            "Étape 4: L'écran affiche ...?",
                                                            {
                                                                0: "1",
                                                                1: "2",
                                                                2: "3",
                                                                3: "4",
                                                                },
                                                            [
                                                                lambda liste_7: NextLink(
                                                                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en 1re position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en {}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                            ],
                                                            False,
                                                            ),
                                                    ],
                                                    False,
                                                    ) if 3 in liste_5 else None,
                                            ],
                                            False,
                                            ),
                                    ],
                                    False,
                                    ) if 1 in liste_3 or 3 in liste_3 else None,
                                lambda liste_3: NextLink(
                                    "Quelle est la valeur du bouton en 1re position? ...et appuyez dessus",
                                    {
                                        0: "1",
                                        1: "2",
                                        2: "3",
                                        3: "4",
                                        },
                                    [
                                        lambda liste_4: NextLink(
                                            "Étape 3: L'écran affiche ...?",
                                            {
                                                0: "1",
                                                1: "2",
                                                2: "3",
                                                3: "4",
                                                },
                                            [
                                                lambda liste_5: NextLink(
                                                    "Quelle est la position du bouton portant le chiffre \'{}\'? ...et appuyez dessus",
                                                    {
                                                        0: "1",
                                                        1: "2",
                                                        2: "3",
                                                        3: "4",
                                                        },
                                                    [
                                                        lambda liste_6: NextLink(
                                                            "Étape 4: L'écran affiche ...?",
                                                            {
                                                                0: "1",
                                                                1: "2",
                                                                2: "3",
                                                                3: "4",
                                                                },
                                                            [
                                                                lambda liste_7: NextLink(
                                                                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en 1re position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en {}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                            ],
                                                            False,
                                                            ),
                                                    ],
                                                    False,
                                                    ) if 0 in liste_5 or 1 in liste_5 else None,
                                                lambda liste_5: NextLink(
                                                    "Quelle est la valeur du bouton en 3e position? ...et appuyez dessus",
                                                    {
                                                        0: "1",
                                                        1: "2",
                                                        2: "3",
                                                        3: "4",
                                                        },
                                                    [
                                                        lambda liste_6: NextLink(
                                                            "Étape 4: L'écran affiche ...?",
                                                            {
                                                                0: "1",
                                                                1: "2",
                                                                2: "3",
                                                                3: "4",
                                                                },
                                                            [
                                                                lambda liste_7: NextLink(
                                                                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en 1re position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en {}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                            ],
                                                            False,
                                                            ),
                                                    ],
                                                    False,
                                                    ) if 2 in liste_5 else None,
                                                lambda liste_5: NextLink(
                                                    "Quelle est la position du bouton portant le chiffre \'4\'? ...et appuyez dessus",
                                                    {
                                                        0: "1",
                                                        1: "2",
                                                        2: "3",
                                                        3: "4",
                                                        },
                                                    [
                                                        lambda liste_6: NextLink(
                                                            "Étape 4: L'écran affiche ...?",
                                                            {
                                                                0: "1",
                                                                1: "2",
                                                                2: "3",
                                                                3: "4",
                                                                },
                                                            [
                                                                lambda liste_7: NextLink(
                                                                    f"Quelle est la valeur du bouton en {2 if 0 in liste_1 or 1 in liste_1 else 3 if 2 in liste_1 else 4}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en 1re position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                                lambda liste_7: NextLink(
                                                                    "Quelle est la valeur du bouton en {}e position? ...et appuyez dessus",
                                                                    {
                                                                        0: "1",
                                                                        1: "2",
                                                                        2: "3",
                                                                        3: "4",
                                                                        },
                                                                    [
                                                                        lambda liste_8: NextLink(
                                                                            "Étape 5: L'écran affiche ...?",
                                                                            {
                                                                                0: "1",
                                                                                1: "2",
                                                                                2: "3",
                                                                                3: "4",
                                                                                },
                                                                            [
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 0 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 1 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 2 in liste else None,
                                                                                lambda liste: NextLink(
                                                                                    "Appuyer sur {}?",
                                                                                    ) if 3 in liste else None,
                                                                            ],
                                                                            False,
                                                                            ),
                                                                    ],
                                                                    False,
                                                                    ) if 0 in liste_7 else None,
                                                            ],
                                                            False,
                                                            ),
                                                    ],
                                                    False,
                                                    ) if 3 in liste_5 else None,
                                            ],
                                            False,
                                            ),
                                    ],
                                    False,
                                    ) if 2 in liste_3 else None,
                            ],
                            False,
                            ),
                    ],
                    False,
                    ) if liste_1 != [] else None,
            ],
            False,
        )

        make_menu(self, self.nouvelle_partie, self.quitter)

        self.cadre = Frame(self)
        self.cadre.grid(padx=FenetrePad.PADDING_X, pady=FenetrePad.PADDING_Y)
        self.cadre.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.ouvrir_partie()

    def ouvrir_partie(self):
        self.redessiner()

    def redessiner(self):
        self.next_link.undo()
        self.next_link.do(self.cadre, 0)

    def nouvelle_partie(self):
        self.ouvrir_partie()

    def quitter(self):
        if messagebox.askyesno("Quitter", "Êtes-vous sûr de vouloir quitter?"):
            self.quit()
