from tkinter import Frame, messagebox, Toplevel, Canvas, BOTH, LEFT, TOP

from .model.next_link import NextLink
from .tools.fonctions import make_menu
from .tools.constantes import FenetrePad
from constants.fenetre import Titre


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


class Module_6(Toplevel):
    def __init__(self, root, geometrie):
        super().__init__(root)

        self.title(Titre.MODULE_6.value)
        self.geometry(geometrie)
        self.resizable(True, True)

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

        container = Frame(self)
        container.pack(fill=BOTH, expand=True)
        self.canvas = Canvas(container, bd=0, highlightthickness=0)

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
        self.bind("<Button-2>", lambda e: self.redessiner())
        self.bind("<Button-3>", lambda e: self.clic())
        self.ouvrir_partie()

    def clic(self):
        if self.state() == "zoomed":
            self.state("normal")
        else:
            self.state("zoomed")

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
