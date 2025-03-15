from tkinter import Frame, messagebox, Toplevel, CENTER

from .tools.fonctions import make_menu, make_question, make_conclusion
from .tools.constantes import FenetrePad
from constants.fenetre import Titre


class Module_2(Toplevel):
    def __init__(self, root, geometrie):
        super().__init__(root)

        self.title(Titre.MODULE_2)
        self.geometry(geometrie)
        self.resizable(True, True)

        self.questions: dict[str, dict[str, str | list[dict[str, str]]]] = {
            "q1": {
                "text": "Bouton bleu? Bouton écrit \"Annuler\"?",
                "options": [
                    {"text": "Oui", "next_id": "q7"},
                    {"text": "Non", "next_id": "q2"},
                ]
            },
            "q2": {
                "text": "Plus qu'une pile? Bouton écrit \"Exploser\"?",
                "options": [
                    {"text": "Oui", "next_id": "c1"},
                    {"text": "Non", "next_id": "q3"},
                ]
            },
            "q3": {
                "text": "Bouton blanc? Indicateur allumé avec \"CAR\"?",
                "options": [
                    {"text": "Oui", "next_id": "q7"},
                    {"text": "Non", "next_id": "q4"},
                ]
            },
            "q4": {
                "text": "Plus de 2 piles? Indicateur allumé avec \"FRK\"?",
                "options": [
                    {"text": "Oui", "next_id": "c1"},
                    {"text": "Non", "next_id": "q5"},
                ]
            },
            "q5": {
                "text": "Bouton jaune?",
                "options": [
                    {"text": "Oui", "next_id": "q7"},
                    {"text": "Non", "next_id": "q6"},
                ]
            },
            "q6": {
                "text": "Bouton rouge? Bouton écrit \"Maintenir\"?",
                "options": [
                    {"text": "Oui", "next_id": "c1"},
                    {"text": "Non", "next_id": "q7"},
                ]
            },
            "q7": {
                "text": "Maintenir le bouton appuyé et... De quelle couleur est la bande qui vient de s'allumer à droite?",
                "options": [
                    {"text": "Bleu", "next_id": "c2.1"},
                    {"text": "Blanc", "next_id": "c2.2"},
                    {"text": "Jaune", "next_id": "c2.3"},
                    {"text": "Autre", "next_id": "c2.2"},
                ]
            },
        }
        self.conclusions = {
            "c1": "Appuyer et immédiatement relâcher le bouton",
            "c2.1": "Relâcher le bouton quand le minuteur affiche un 4 dans n'importe quelle position",
            "c2.2": "Relâcher le bouton quand le minuteur affiche un 1 dans n'importe quelle position",
            "c2.3": "Relâcher le bouton quand le minuteur affiche un 5 dans n'importe quelle position",
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
