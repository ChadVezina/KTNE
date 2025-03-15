from tkinter import Frame, messagebox, Toplevel, CENTER

from .tools.fonctions import make_menu, make_question, make_conclusion
from .tools.constantes import FenetrePad
from constants.fenetre import Titre


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

        self.questions: dict[str, dict[str, str | list[dict[str, str]]]] = {
            "q1": {
                "text": "Combien de fils?",
                "options": [
                    {"text": "3", "next_id": "c1"},
                    {"text": "4", "next_id": "q2"},
                    {"text": "5", "next_id": "q3"},
                    {"text": "6", "next_id": "q4"},
                ]
            },
        }
        self.conclusions = {
            "c1": "",
            "c2": "",
            "c3": "",
            "c4": "",
        }

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
        self.historique = []
        self.selectionner("q1")

    def selectionner(self, id, row=0, scan=-1):
        if(scan != -1):
            for i, bouton in enumerate(self.cadre.winfo_children()[row].winfo_children()):
                if(i == 0):
                    continue
                if i != scan:
                    bouton.config(bg="white")
                else:
                    bouton.config(bg="pink")
        if row < len(self.historique):
            self.historique = self.historique[:row+1]
            for scan, widget in enumerate(self.cadre.winfo_children()):
                if(scan > row):
                    widget.destroy()
        self.current = id
        self.display_question(id)

    def display_question(self, question_id):
        row = len(self.historique)
        self.historique.append(question_id)
        if question_id in self.conclusions:
            make_conclusion(self.cadre, self.conclusions[question_id], row)
            return
        question_data = self.questions[question_id]
        make_question(
            self.cadre,
            question_data['text'],
            row,
            question_data['options'],
            lambda option:
                option['text'],
            lambda option, scan: lambda n=option['next_id']:
                self.selectionner(n, row, scan)
            )

    def nouvelle_partie(self):
        self.ouvrir_partie()

    def quitter(self):
        if messagebox.askyesno("Quitter", "Êtes-vous sûr de vouloir quitter?"):
            self.quit()
