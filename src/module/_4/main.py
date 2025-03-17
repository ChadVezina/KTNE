from tkinter import Frame, messagebox, Toplevel, CENTER

from .model.next_link import NextLink
from .tools.fonctions import make_menu
from .tools.constantes import FenetrePad
from constants.fenetre import Titre


class Module_4(Toplevel):
    def __init__(self, root, geometrie):
        super().__init__(root)

        self.title(Titre.MODULE_4.value)
        self.geometry(geometrie)
        self.resizable(True, True)

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
                    ),
            ],
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
