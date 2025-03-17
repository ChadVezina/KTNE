from tkinter import Frame, messagebox, Toplevel, CENTER

from .model.next_link import NextLink
from .tools.fonctions import make_menu
from .tools.constantes import FenetrePad
from constants.fenetre import Titre


def test():
    lambda liste: NextLink(
                    "",
                    {
                        
                        },
                    [
                        
                    ],
                    ) if 1 in liste else None,


class Module_4(Toplevel):
    def __init__(self, root, geometrie):
        super().__init__(root)

        self.title(Titre.MODULE_4.value)
        self.geometry(geometrie)
        self.resizable(True, True)

        self.next_link = NextLink(
            "Combien de fils?",
            {
                0: "3",
                1: "4",
                2: "5",
                3: "6",
            },
            [
                lambda liste: NextLink(
                    "Combien de fils rouges?",
                    {
                        0: "0",
                        },
                    [
                        lambda liste: NextLink(
                            "Couper le 2e fil",
                            ) if 0 in liste else NextLink(
                            "Le dernier fil est ...?",
                            {
                                0: "blanc",
                                },
                            [
                                lambda liste: NextLink(
                                    "Couper le dernier fil",
                                    ) if 0 in liste else NextLink(
                                    "Combien de fils bleus?",
                                    {
                                        0: "plus qu'un",
                                        },
                                    [
                                        lambda liste: NextLink(
                                            "Couper le dernier fil bleu",
                                            ) if 0 in liste else NextLink(
                                            "Couper le dernier fil",
                                            ),
                                    ],
                                    ),
                            ],
                            ),
                    ],
                    ) if 0 in liste else NextLink(
                    "Combien de fils rouges? Le dernier chiffre du numéro de série est ...?",
                    {
                        0: "plus qu'un",
                        1: "impair",
                        },
                    [
                        lambda liste: NextLink(
                            "Couper le dernier fil rouge",
                            ) if 0 in liste and 1 in liste else NextLink(
                            "Combien de fils rouges? Le dernier fil est ...?" if not 0 in liste else "Le dernier fil est ...?",
                            {
                                0: "0",
                                1: "jaune",
                                } if not 0 in liste else {
                                0: "jaune",
                                },
                            [
                                lambda liste: NextLink(
                                    "Couper le premier fil",
                                    ) if 0 in liste and 1 in liste else NextLink(
                                    "Combien de fils bleus?",
                                    {
                                        0: "1",
                                        },
                                    [
                                        lambda liste: NextLink(
                                            "Couper le premier fil",
                                            ) if 0 in liste else NextLink(
                                            "Combien de fils jaunes?",
                                            {
                                                0: "plus qu'un",
                                                },
                                            [
                                                lambda liste: NextLink(
                                                    "Couper le dernier fil",
                                                    ) if 0 in liste else NextLink(
                                                    "Couper le 2e fil",
                                                    ),
                                            ],
                                            ),
                                    ],
                                    ),
                            ],
                            ),
                    ],
                    ) if 1 in liste else NextLink(
                    "Le dernier fil est ...? Le dernier chiffre du numéro de série est ...?",
                    {
                        0: "noir",
                        1: "impair",
                        },
                    [
                        lambda liste0: NextLink(
                            "Couper le 4e fil",
                            ) if 0 in liste0 and 1 in liste0 else NextLink(
                            "Combien de fils rouges? Combien de fils jaunes?",
                            {
                                0: "1",
                                1: "plus qu'un",
                                },
                            [
                                lambda liste: NextLink(
                                    "Couper le premier fil",
                                    ) if 0 in liste and 1 in liste else NextLink(
                                    "Combien de fils noirs?",
                                    {
                                        0: "0",
                                        },
                                    [
                                        lambda liste: NextLink(
                                            "Couper le 2e fil",
                                            ) if 0 in liste else NextLink(
                                            "Couper le premier fil",
                                            ),
                                    ],
                                    ) if not 0 in liste0 else NextLink(
                                            "Couper le premier fil",
                                            ),
                            ],
                            ),
                    ],
                    ) if 2 in liste else NextLink(
                    "Combien de fils jaunes? Le dernier chiffre du numéro de série est ...?",
                    {
                        0: "0",
                        1: "impair",
                        },
                    [
                        lambda liste: NextLink(
                            "Couper le 3e fil",
                            ) if 0 in liste and 1 in liste else NextLink(
                            "Combien de fils jaunes? Combien de fils blancs?" if not 0 in liste else "Combien de fils blancs?",
                            {
                                0: "1",
                                1: "plus qu'un",
                                } if not 0 in liste else {
                                0: "plus qu'un",
                                },
                            [
                                lambda liste: NextLink(
                                    "Couper le 4e fil",
                                    ) if 0 in liste and 1 in liste else NextLink(
                                    "Combien de fils rouges?",
                                    {
                                        0: "0",
                                        },
                                    [
                                        lambda liste: NextLink(
                                            "Couper le dernier fil",
                                            ) if 0 in liste else NextLink(
                                            "Couper le 4e fil",
                                            ),
                                    ],
                                    ),
                            ],
                            ),
                    ],
                    ) if 3 in liste else None,
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
