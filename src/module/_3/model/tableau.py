from tkinter import Frame
from .case import Case
from .conclusion import Conclusion


class Tableau:
    def __init__(self, caracteres: list[str], colonnes: list[list[str]]):
        self.caracteres = caracteres
        self.colonnes = colonnes
        self.length = len(self.caracteres)
        self.initialiser_tableau()

    def placer_tableau(self, parent):
        composante = Frame(parent)
        composante.grid(row=0)
        ratio = self.calculateRatio(parent)
        n_y = self.calculate_x_y(ratio)
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
        return sorted(colonnes_communes.items(), key=lambda x: len(x[1]))

    def initialiser_tableau(self):
        self.cases: list[Case] = []
        for i in range(self.length):
            self.cases.append(Case(i, self.caracteres[i], lambda: self.afficher_solution()))

    def get_solution(self):
        colonnes_communes = self.obtenir_colonnes_communes()
        if len(colonnes_communes) == 0:
            return "Aucune colonne commune"
        if len(colonnes_communes[0][1]) == 4:
            solution = self.colonnes[colonnes_communes[0][0]].copy()
            for solution_case in solution:
                if solution_case not in colonnes_communes[0][1]:
                    solution.remove(solution_case)
            result = str.join(" ", solution)
            return f"Solution unique: {result}"
        texte: list[str] = []
        for colonne, caracteres in colonnes_communes:
            solution = self.colonnes[colonne].copy()
            for solution_case in solution:
                if solution_case in caracteres:
                    scan = solution.index(solution_case)
                    solution[scan] = f"({solution_case})"
            texte.append(str.join(" ", solution))
        result = str.join("\n", texte)
        return f"Solutions possibles: {result}"

    def afficher_solution(self):
        texte = self.get_solution()
        self.conclusion.setText(texte)

    def calculateRatio(self, parent: Frame):
        phase_y = 20
        dephase_x = 2
        dephase_y = 50
        screen_width = parent.winfo_screenwidth()-(dephase_x//2)
        screen_height = parent.winfo_screenheight()-(dephase_y//2)-phase_y
        return screen_width / screen_height

    def calculate_x_y(self, ratio):
        unit = self.length / (ratio+1)
        n_x = round(unit * ratio)
        n_y = round(unit)
        diff = self.length - (n_x * n_y)
        while(diff < 0):
            if(ratio >= 1):
                n_x -= 1
            else:
                n_y -= 1
            diff = self.length - (n_x * n_y)
        while(diff > 0):
            if(ratio >= 1):
                n_y += 1
            else:
                n_x += 1
            diff = self.length - (n_x * n_y)
        return n_y


