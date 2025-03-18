from tkinter import Tk, Frame, messagebox, Canvas, BOTH, LEFT, TOP

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
                            ) if 0 in liste and 1 in liste else lambda liste: NextLink(
                            "",
                            {
                                
                                },
                            [
                                
                            ],
                            ),
    
    lambda liste0: NextLink(
                    "",
                    {
                        
                        },
                    [
                        
                    ],
                    ) if 1 in liste else None,


class Module_1(Tk):
    def __init__(self):
        super().__init__()

        self.title(Titre.MODULE_1.value)
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
