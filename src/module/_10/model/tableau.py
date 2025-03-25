from tkinter import Frame

from .case import Case
from .conclusion import Conclusion
from ..tools.enums import TypeTableau, TypeCase


class Tableau:
    def __init__(self):
        self.max_row = 13
        self.max_col = 13
        self.a = None
        self.b = None
        self.depart = None
        self.arrivee = None
        self.types = {
            TypeTableau._0: ({
                0: [0, 1, 2, 3, 4, 5], #horizontal
                1: [0, 3, 6], #vertical
                2: [1, 4, 5], #horizontal
                3: [0, 1, 3, 6], #vertical
                4: [2, 3, 4], #horizontal
                5: [0, 1, 3, 6], #vertical
                6: [1, 4], #horizontal
                7: [0, 1, 4, 6], #vertical
                8: [1, 2, 3, 4], #horizontal
                9: [0, 3, 5, 6], #vertical
                10: [1, 4], #horizontal
                11: [0, 2, 4, 6], #vertical
                12: [0, 1, 2, 3, 4, 5], #horizontal
            }, (1, 0), (2, 5)),
        }
        self.initialiser_tableau()
        self.add_a(1, 0)
        self.add_b(2, 5)

    def initialiser_tableau(self):
        self.cases: list[list[Case]] = []
        for i in range(self.max_row):
            cases: list[Case] = []
            for j in range(self.max_col):
                cases.append(Case(i, j))
            self.cases.append(cases)

    def clic(self, x: int, y: int, type: TypeCase):
        match type:
            case TypeCase.DEPART:
                self.depart = None
                self.cases[x][y].setType(TypeCase.VIDE)
            case TypeCase.ARRIVEE:
                self.arrivee = None
                self.cases[x][y].setType(TypeCase.VIDE)
            case TypeCase.VIDE:
                if self.depart is None:
                    self.depart = (x, y)
                    self.cases[x][y].setType(TypeCase.DEPART)
                elif self.arrivee is None:
                    self.arrivee = (x, y)
                    self.cases[x][y].setType(TypeCase.ARRIVEE)
            case _:
                pass

    def placer_tableau(self, parent):
        composante = Frame(parent)
        composante.grid(row=0)
        for i in range(self.max_row):
            for j in range(self.max_col):
                self.cases[i][j].placer_case(composante, i, j, lambda x, y, type: self.clic(x, y, type))

    def placer_solution(self, parent):
        composante = Frame(parent)
        composante.grid(row=1)
        texte = self.get_solution()
        self.conclusion = Conclusion(parent, texte)

    def valider_coordonnees(self, i: int, j: int):
        return i in range(self.max_row) and j in range(self.max_col)

    def obtenir_case(self, x, y):
        if not self.valider_coordonnees(x, y):
            return None

        return self.cases[x][y]

    def remplir_tableau(self, type: TypeTableau):
        for i in range(self.max_row):
            for j in self.types[type][0][i]:
                if i % 2 == 0:
                    self.add_mur(i, j*2+1)
                else:
                    self.add_mur(i, j*2)

    def add_mur(self, i: int, j: int):
        self.cases[i][j].setType(TypeCase.MUR)

    def get_coords(self, i: int, j: int):
        return i*2+1, j*2+1

    def add_a(self, i: int, j: int):
        if self.a is not None:
            if self.a == (i, j):
                return
            x, y = self.get_coords(*self.a)
            self.cases[x][y].setType(TypeCase.VIDE)
        x, y = self.get_coords(i, j)
        self.cases[x][y].setType(TypeCase.POINT_A)
        self.a = (i, j)
        if self.b is not None:
            self.remplir()

    def add_b(self, i: int, j: int):
        if self.b is not None:
            if self.b == (i, j):
                return
            x, y = self.get_coords(*self.b)
            self.cases[x][y].setType(TypeCase.VIDE)
        x, y = self.get_coords(i, j)
        self.cases[x][y].setType(TypeCase.POINT_B)
        self.b = (i, j)
        if self.a is not None:
            self.remplir()

    def get_type_tableau(self):
        for type in TypeTableau:
            if self.a == self.types[type][1] and self.b == self.types[type][2]:
                return type
        return None

    def remplir(self):
        self.clear()
        type = self.get_type_tableau()
        if type is not None:
            self.remplir_tableau(type)

    def clear(self):
        for i in range(self.max_row):
            for j in range(self.max_col):
                self.cases[i][j].init()

    def get_solution(self):
        return "Solution"

    def afficher_solution(self):
        texte = self.get_solution()
        self.conclusion.setText(texte)

