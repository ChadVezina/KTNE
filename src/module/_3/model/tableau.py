from tkinter import Frame
from .case import Case
from .conclusion import Conclusion
from tools.functions import get_width_height, calculate_x_y


class Tableau:
    def __init__(self, caracteres: list[str], hints: list[str], colonnes: list[list[str]]):
        self.caracteres = caracteres
        self.hints = hints
        self.colonnes = colonnes
        self.length = len(self.caracteres)
        self.initialiser_tableau()

    def placer_tableau(self, parent):
        composante = Frame(parent)
        composante.grid(row=0)
        n_y = self.calculate_y(parent)
        for scan in range(self.length):
            x = scan // n_y
            y = scan % n_y
            self.cases[scan].placer_case(composante, x, y)

    def placer_solution(self, parent):
        composante = Frame(parent)
        composante.grid(row=1)
        texte = self.get_solution()
        self.conclusion = Conclusion(parent, texte)

    def valider_coordonnees(self, i):
        return i in range(self.length)

    def obtenir_case(self, numero):
        if not self.valider_coordonnees(numero):
            return None

        return self.cases[numero]

    def obtenir_colonnes_communes(self):
        colonnes_communes: dict[int, list[str]] = {}
        for case in self.cases:
            colonnes_valides = case.colonnes_valides(self.colonnes)
            if colonnes_valides is not None:
                for colonne in colonnes_valides:
                    old_value = colonnes_communes.get(colonne, [])
                    old_value.append(case.texte)
                    colonnes_communes[colonne] = old_value
        return sorted(colonnes_communes.items(), key=lambda x: len(x[1]), reverse=True)

    def initialiser_tableau(self):
        self.cases: list[Case] = []
        for i in range(self.length):
            self.cases.append(Case(i, self.caracteres[i], self.hints[i], lambda: self.afficher_solution()))

    def get_solution(self):
        colonnes_communes = self.obtenir_colonnes_communes()
        if len(colonnes_communes) == 0:
            return "Solution indéterminée..."
        if len(colonnes_communes[0][1]) == 4 and (len(colonnes_communes) == 1 or len(colonnes_communes[1][1]) != 4):
            solution = self.colonnes[colonnes_communes[0][0]].copy()
            selection = colonnes_communes[0][1].copy()
            solution = [val for val in solution if val in selection]
            result = str.join("\t", solution)
            solution_hint = [f"{self.hints[self.caracteres.index(val)]}" for val in solution]
            result_hint = str.join("\t", solution_hint)
            return f"Solution unique:\n\n{result}\n{result_hint}"
        texte: list[str] = []
        for colonne, caracteres in colonnes_communes:
            solution = self.colonnes[colonne].copy()
            for solution_case in solution:
                if solution_case in caracteres:
                    scan = solution.index(solution_case)
                    solution[scan] = f"({solution_case})"
            result = str.join("\t", solution)
            n_caracteres = len(caracteres)
            texte.append(f"{result}\t\t{n_caracteres}")
        result = str.join("\n\n", texte)
        return f"Solutions possibles:\n\n{result}"

    def afficher_solution(self):
        texte = self.get_solution()
        self.conclusion.setText(texte)

    def calculate_y(self, parent):
        screen_width, screen_height = get_width_height(parent)
        return calculate_x_y(screen_width, screen_height, self.length)[1]


