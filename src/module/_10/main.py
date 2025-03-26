from tkinter import Frame, messagebox, Toplevel, Canvas, BOTH, LEFT, TOP

from .tools.fonctions import make_menu
from .tools.constantes import FenetrePad
from constants.fenetre import Titre
from .model.tableau import Tableau

class Module_10(Toplevel):
    def __init__(self, root, geometrie):
        super().__init__(root)

        self.title(Titre.MODULE_10.value)
        self.geometry(geometrie)
        self.resizable(True, True)

        self.tableau = Tableau()

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
        for widget in self.cadre.winfo_children():
            widget.destroy()
        self.redessiner()

    def redessiner(self):
        self.tableau.placer_tableau(self.cadre)
        self.tableau.placer_solution(self.cadre)

    def nouvelle_partie(self):
        self.ouvrir_partie()

    def quitter(self):
        if messagebox.askyesno("Quitter", "Êtes-vous sûr de vouloir quitter?"):
            self.quit()
