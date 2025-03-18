from tkinter import Frame, messagebox, Toplevel, Canvas, BOTH, LEFT, TOP

from .model.next_link import NextLink
from .tools.fonctions import make_menu
from .tools.constantes import FenetrePad
from constants.fenetre import Titre


class Module_2(Toplevel):
    def __init__(self, root, geometrie):
        super().__init__(root)

        self.title(Titre.MODULE_2.value)
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

        make_menu(self, self.nouvelle_partie, self.quitter)

        container = Frame(self)
        container.pack(fill=BOTH, expand=True)
        self.canvas = Canvas(container)

        self.outer_frame = Frame(self.canvas)
        self.cadre = Frame(self.outer_frame)
        self.cadre.pack(side=TOP, padx=FenetrePad.PADDING_X, pady=FenetrePad.PADDING_Y)

        self.canvas.create_window((0, 0), window=self.outer_frame, anchor="n", tags="frame")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.outer_frame.bind("<Configure>", self.update_scroll)
        self.canvas.bind("<Configure>", self.center_content)
        self.cadre.bind("<Configure>", self.on_inner_frame_change)

        self.scroll_active = False
        self.bind("<Map>", lambda e: self.enter())
        self.bind("<Unmap>", lambda e: self.enter())
        self.bind("<Enter>", lambda e: self.bind_mouse_scroll())
        self.ouvrir_partie()

    def enter(self):
        self.on_inner_frame_change()

    def on_inner_frame_change(self, event=None):
        self.outer_frame.event_generate("<Configure>")
        self.canvas.event_generate("<Configure>")

    def center_content(self, event=None):
        canvas_width = self.canvas.winfo_width()
        self.canvas.itemconfig("frame", width=canvas_width)

    def update_scroll(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        content_height = self.outer_frame.winfo_height()
        canvas_height = self.canvas.winfo_height()

        if content_height > canvas_height:
            if not self.scroll_active:
                self.scroll_active = True
                self.bind_mouse_scroll()
        else:
            if self.scroll_active:
                self.scroll_active = False
                self.bind_mouse_scroll()

    def bind_mouse_scroll(self):
        if self.scroll_active:
            self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        else:
            self.canvas.unbind_all("<MouseWheel>")

    def on_mousewheel(self, event):
        if self.scroll_active:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

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
