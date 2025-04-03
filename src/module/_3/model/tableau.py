from tkinter import Frame
from typing import Callable

from .case import Case
from .conclusion import Conclusion

from model.root import Root
from tools.functions import get_width_height, calculate_x_y


class Tableau:
    def __init__(self, caracteres: list[str], hints: list[str], colonnes: list[list[str]]):
        self.caracteres = caracteres
        self.hints = hints
        self.colonnes = colonnes
        self.length = len(self.caracteres)
        self.root: Root | None = None
        self.initialiser_tableau()

    def do(self, parent: Frame, row: int):
        self.destroy()
        self.parent = parent
        self.row = row
        self.root = Root(parent, row)
        self.placer_tableau(self.root)
        self.placer_solution(self.root)

    def destroy(self):
        if(self.root is not None):
            self.root.destroy()
            self.root = None
            self.parent = None
            self.row = None

    def placer_tableau(self, parent):
        composante = Frame(parent)
        composante.grid(row = 0)
        n_y = self.calculate_y(parent)
        for scan in range(self.length):
            x = scan // n_y
            y = scan % n_y
            self.cases[scan].placer_case(composante, x, y)

    def placer_solution(self, parent):
        composante = Frame(parent)
        composante.grid(row = 1)
        self.conclusion = Conclusion(parent)
        self.afficher_solution()

    def initialiser_tableau(self):
        self.cases: list[Case] = []
        for i in range(self.length):
            self.cases.append(Case(i, self.caracteres[i], self.hints[i], lambda: self.afficher_solution()))

    def calculate_y(self, parent):
        screen_width, screen_height = get_width_height(parent)
        return calculate_x_y(screen_width, screen_height, self.length)[1]

    def valider_coordonnees(self, i):
        return i in range(self.length)

    def obtenir_commande(self, numero: int):
        if not self.valider_coordonnees(numero):
            return None

        return lambda: self.cases[numero].clic()

    def obtenir_colonnes_communes(self):
        colonnes_communes: dict[int, list[str]] = {}
        for case in self.cases:
            colonnes_valides = case.colonnes_valides(self.colonnes)
            if colonnes_valides is not None:
                for colonne in colonnes_valides:
                    old_value = colonnes_communes.get(colonne, [])
                    old_value.append(case.texte)
                    colonnes_communes[colonne] = old_value
        return sorted(colonnes_communes.items(), key = lambda x: len(x[1]), reverse = True)

    def get_solution(self):
        colonnes_communes = self.obtenir_colonnes_communes()
        if len(colonnes_communes) == 0:
            return None, False
        result: list[list[tuple[str, str, bool, Callable[[], None]]]] = []
        if len(colonnes_communes[0][1]) == 4 and (len(colonnes_communes) == 1 or len(colonnes_communes[1][1]) != 4):
            solution = self.colonnes[colonnes_communes[0][0]].copy()
            selection = colonnes_communes[0][1].copy()
            result.append([(val, self.hints[self.caracteres.index(val)], True, self.obtenir_commande(self.caracteres.index(val))) for val in solution if val in selection])
            return result, True
        for colonne, caracteres in colonnes_communes:
            solution = self.colonnes[colonne].copy()
            selection = caracteres.copy()
            result.append([(val, self.hints[self.caracteres.index(val)], True if val in selection else False, self.obtenir_commande(self.caracteres.index(val))) for val in solution])
        return result, False

    def afficher_solution(self):
        self.conclusion.setText(*self.get_solution())
