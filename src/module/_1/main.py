from tkinter import Tk, Frame, messagebox, Button, CENTER

from .tools.fonctions import make_menu, make_question, make_conclusion
from .tools.constantes import FenetrePad
from constants.fenetre import Titre


class Module_1(Tk):
    def __init__(self):
        super().__init__()

        self.title(Titre.MODULE_1.value)
        self.resizable(True, True)

        self.questions: dict[str, dict[str, str | list[dict[str, str]]]] = {
            "q1": {
                "text": "Combien de fils?",
                "options": [
                    {"text": "3", "next_id": "q3.1"},
                    {"text": "4", "next_id": "q4.1"},
                    {"text": "5", "next_id": "q5.1"},
                    {"text": "6", "next_id": "q6.1"},
                ]
            },
            "q3.1": {
                "text": "Combien de fils rouges?",
                "options": [
                    {"text": "0", "next_id": "c3.1"},
                    {"text": "plusieurs", "next_id": "q3.2"},
                ]
            },
            "q3.2": {
                "text": "Le dernier fil est ...?",
                "options": [
                    {"text": "blanc", "next_id": "c3.2"},
                    {"text": "autre", "next_id": "q3.3"},
                ]
            },
            "q3.3": {
                "text": "Combien de fils bleus?",
                "options": [
                    {"text": "plus qu'un", "next_id": "c3.3"},
                    {"text": "autre", "next_id": "c3.4"},
                ]
            },
            "q4.1": {
                "text": "Combien de fils rouges? Le dernier chiffre du numéro de série est ...?",
                "options": [
                    {"text": "plus qu'un / impair", "next_id": "c4.1"},
                    {"text": "autre", "next_id": "q4.2"},
                ]
            },
            "q4.2": {
                "text": "Combien de fils rouges? Le dernier fil est ...?",
                "options": [
                    {"text": "0 / jaune", "next_id": "c4.2"},
                    {"text": "autre", "next_id": "q4.3"},
                ]
            },
            "q4.3": {
                "text": "Combien de fils bleus?",
                "options": [
                    {"text": "1", "next_id": "c4.3"},
                    {"text": "autre", "next_id": "q4.4"},
                ]
            },
            "q4.4": {
                "text": "Combien de fils jaunes?",
                "options": [
                    {"text": "plus qu'un", "next_id": "c4.4"},
                    {"text": "autre", "next_id": "c4.5"},
                ]
            },
            "q5.1": {
                "text": "Le dernier fil est ...? Le dernier chiffre du numéro de série est ...?",
                "options": [
                    {"text": "noir / impair", "next_id": "c5.1"},
                    {"text": "autre", "next_id": "q5.2"},
                ]
            },
            "q5.2": {
                "text": "Combien de fils rouges? Combien de fils jaunes?",
                "options": [
                    {"text": "1 / plus qu'un", "next_id": "c5.2"},
                    {"text": "autre", "next_id": "q5.3"},
                ]
            },
            "q5.3": {
                "text": "Combien de fils noirs?",
                "options": [
                    {"text": "0", "next_id": "c5.3"},
                    {"text": "plusieurs", "next_id": "c5.4"},
                ]
            },
            "q6.1": {
                "text": "Combien de fils jaunes? Le dernier chiffre du numéro de série est ...?",
                "options": [
                    {"text": "0 / impair", "next_id": "c6.1"},
                    {"text": "autre", "next_id": "q6.2"},
                ]
            },
            "q6.2": {
                "text": "Combien de fils jaunes? Combien de fils blancs?",
                "options": [
                    {"text": "1 / plus qu'un", "next_id": "c6.2"},
                    {"text": "autre", "next_id": "q6.3"},
                ]
            },
            "q6.3": {
                "text": "Combien de fils rouges?",
                "options": [
                    {"text": "0", "next_id": "c6.3"},
                    {"text": "plusieurs", "next_id": "c6.4"},
                ]
            },
        }
        self.conclusions = {
            "c3.1": "Couper le 2e fil",
            "c3.2": "Couper le dernier fil",
            "c3.3": "Couper le dernier fil bleu",
            "c3.4": "Couper le dernier fil",

            "c4.1": "Couper le dernier fil rouge",
            "c4.2": "Couper le premier fil",
            "c4.3": "Couper le premier fil",
            "c4.4": "Couper le dernier fil",
            "c4.5": "Couper le 2e fil",

            "c5.1": "Couper le 4e fil",
            "c5.2": "Couper le premier fil",
            "c5.3": "Couper le 2e fil",
            "c5.4": "Couper le premier fil",

            "c6.1": "Couper le 3e fil",
            "c6.2": "Couper le 4e fil",
            "c6.3": "Couper le dernier fil",
            "c6.4": "Couper le 4e fil",
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
