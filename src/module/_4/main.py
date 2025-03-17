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
                                    "Appuyer sur le bouton rouge",
                                    ) if(
                                        (0 in liste_1 and (
                                            (0 in liste_2 and 3 in liste) or
                                            (1 in liste_2 and 0 in liste) or
                                            (2 in liste_2 and 3 in liste)
                                            )) or
                                        (not 0 in liste_1 and (
                                            (0 in liste_2 and 1 in liste) or
                                            (1 in liste_2 and 3 in liste) or
                                            (2 in liste_2 and 1 in liste)
                                            ))
                                        ) else None,
                                lambda liste: NextLink(
                                    "Appuyer sur le bouton bleu",
                                    ) if(
                                        (0 in liste_1 and (
                                            (0 in liste_2 and 0 in liste) or
                                            (1 in liste_2 and 1 in liste) or
                                            (2 in liste_2 and 2 in liste)
                                            )) or
                                        (not 0 in liste_1 and (
                                            (0 in liste_2 and 0 in liste) or
                                            (1 in liste_2 and 2 in liste) or
                                            (2 in liste_2 and 3 in liste)
                                            ))
                                        ) else None,
                                lambda liste: NextLink(
                                    "Appuyer sur le bouton vert",
                                    ) if(
                                        (0 in liste_1 and (
                                            (0 in liste_2 and 2 in liste) or
                                            (1 in liste_2 and 3 in liste) or
                                            (2 in liste_2 and 1 in liste)
                                            )) or
                                        (not 0 in liste_1 and (
                                            (0 in liste_2 and 3 in liste) or
                                            (1 in liste_2 and 1 in liste) or
                                            (2 in liste_2 and 0 in liste)
                                            ))
                                        ) else None,
                                lambda liste: NextLink(
                                    "Appuyer sur le bouton jaune",
                                    ) if(
                                        (0 in liste_1 and (
                                            (0 in liste_2 and 1 in liste) or
                                            (1 in liste_2 and 2 in liste) or
                                            (2 in liste_2 and 0 in liste)
                                            )) or
                                        (not 0 in liste_1 and (
                                            (0 in liste_2 and 2 in liste) or
                                            (1 in liste_2 and 0 in liste) or
                                            (2 in liste_2 and 2 in liste)
                                            ))
                                        ) else None,
                            ],
                            False,
                            ),
                    ],
                    False,
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
