from tkinter import Frame
from .case import Case
from .conclusion import Conclusion
from tools.functions import get_width_height, calculate_x_y


class Tableau:
    def __init__(self):
        self.max_row = 13
        self.max_col = 13
        self.initialiser_tableau()

    def placer_tableau(self, parent):
        composante = Frame(parent)
        composante.grid(row=0)
        for i in range(self.max_row):
            for j in range(self.max_col):
                self.cases[i][j].placer_case(composante, i, j)

    def placer_solution(self, parent):
        composante = Frame(parent)
        composante.grid(row=1)
        texte = self.get_solution()
        self.conclusion = Conclusion(parent, texte)

    def valider_coordonnees(self, i, j):
        return i in range(self.max_row) and j in range(self.max_col)

    def obtenir_case(self, x, y):
        if not self.valider_coordonnees(x, y):
            return None

        return self.cases[x][y]

    def initialiser_tableau(self):
        self.cases: list[list[Case]] = []
        for i in range(self.max_row):
            cases: list[Case] = []
            for j in range(self.max_col):
                cases.append(Case(i, j))
            self.cases.append(cases)

    def get_solution(self):
        return "Solution"

    def afficher_solution(self):
        texte = self.get_solution()
        self.conclusion.setText(texte)

