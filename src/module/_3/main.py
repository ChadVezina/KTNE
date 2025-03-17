from tkinter import Frame, messagebox, Toplevel, CENTER

from .tools.fonctions import make_menu
from .tools.constantes import FenetrePad
from constants.fenetre import Titre
from .model.tableau import Tableau

class Module_3(Toplevel):
    def __init__(self, root, geometrie):
        super().__init__(root)

        self.title(Titre.MODULE_3.value)
        self.geometry(geometrie)
        self.resizable(True, True)
        
        self.caracteres = [
            "Ϙ", # U+03D8
            "Ѧ", # U+0466
            "ƛ", # U+019B
            "Ϟ", # U+03DE
            "Ѭ", # U+046C
            "ϗ", # U+03D7
            "Ͽ", # U+03FF
            "Ӭ", # U+04EC
            "Ҩ", # U+04A8
            "☆", # U+2606
            "¿", # U+00BF
            "©", # U+00A9
            "Ѽ", # U+047C
            "Җ", # U+0496
            "Ԇ", # U+0506
            "Ϭ", # U+03EC
            "¶", # U+00B6
            "ƀ", # U+0180
            "ټ", # U+067C
            "ψ", # U+03C8
            "Ͼ", # U+03FE
            "Ѯ", # U+046E
            "★", # U+2605
            "҂", # U+0482
            "æ", # U+00E6
            "Ҋ", # U+048A
            "Ω", # U+03A9
        ]
        self.colonnes = [
            ["Ϙ", "Ѧ", "ƛ", "Ϟ", "Ѭ", "ϗ", "Ͽ"],
            ["Ӭ", "Ϙ", "Ͽ", "Ҩ", "☆", "ϗ", "¿"],
            ["©", "Ѽ", "Ҩ", "Җ", "Ԇ", "ƛ", "☆"],
            ["Ϭ", "¶", "ƀ", "Ѭ", "Җ", "¿", "ټ"],
            ["ψ", "ټ", "ƀ", "Ͼ", "¶", "Ѯ", "★"],
            ["Ϭ", "Ӭ", "҂", "æ", "ψ", "Ҋ", "Ω"],
        ]
        self.tableau = Tableau(self.caracteres, self.colonnes)

        make_menu(self, self.nouvelle_partie, self.quitter)

        self.cadre = Frame(self)
        self.cadre.grid(padx=FenetrePad.PADDING_X, pady=FenetrePad.PADDING_Y)
        self.cadre.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.ouvrir_partie()

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
