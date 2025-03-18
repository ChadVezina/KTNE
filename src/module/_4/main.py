from tkinter import Frame, messagebox, Toplevel, Canvas, BOTH, LEFT, TOP

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
        self.update_scroll()
        self.bind("<Enter>", lambda e: self.bind_mouse_scroll())
        self.ouvrir_partie()

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
