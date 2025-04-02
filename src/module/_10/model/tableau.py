from tkinter import Frame
import heapq

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
        self.tableau = None
        self.solution = None
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
            TypeTableau._1: ({
                0: [0, 1, 2, 3, 4, 5], #horizontal
                1: [0, 3, 6], #vertical
                2: [0, 2, 5], #horizontal
                3: [0, 2, 4, 6], #vertical
                4: [1, 3, 4], #horizontal
                5: [0, 1, 3, 6], #vertical
                6: [2, 4], #horizontal
                7: [0, 2, 4, 5, 6], #vertical
                8: [1, 3], #horizontal
                9: [0, 1, 2, 3, 5, 6], #vertical
                10: [4], #horizontal
                11: [0, 1, 3, 6], #vertical
                12: [0, 1, 2, 3, 4, 5], #horizontal
            }, (1, 4), (3, 1)),
            TypeTableau._2: ({
                0: [0, 1, 2, 3, 4, 5], #horizontal
                1: [0, 3, 4, 6], #vertical
                2: [1], #horizontal
                3: [0, 1, 2, 3, 5, 6], #vertical
                4: [0, 3, 4], #horizontal
                5: [0, 2, 3, 5, 6], #vertical
                6: [], #horizontal
                7: [0, 1, 2, 3, 4, 5, 6], #vertical
                8: [], #horizontal
                9: [0, 1, 3, 4, 5, 6], #vertical
                10: [1, 2], #horizontal
                11: [0, 4, 6], #vertical
                12: [0, 1, 2, 3, 4, 5], #horizontal
            }, (3, 3), (3, 5)),
            TypeTableau._3: ({
                0: [0, 1, 2, 3, 4, 5], #horizontal
                1: [0, 2, 6], #vertical
                2: [2, 3, 4], #horizontal
                3: [0, 1, 2, 6], #vertical
                4: [3, 4], #horizontal
                5: [0, 1, 3, 5, 6], #vertical
                6: [1, 2, 4], #horizontal
                7: [0, 1, 6], #vertical
                8: [1, 2, 3, 4], #horizontal
                9: [0, 5, 6], #vertical
                10: [1, 2, 3], #horizontal
                11: [0, 3, 5, 6], #vertical
                12: [0, 1, 2, 3, 4, 5], #horizontal
            }, (0, 0), (3, 0)),
            TypeTableau._4: ({
                0: [0, 1, 2, 3, 4, 5], #horizontal
                1: [0, 6], #vertical
                2: [0, 1, 2, 3], #horizontal
                3: [0, 5, 6], #vertical
                4: [1, 2, 4, 5], #horizontal
                5: [0, 2, 4, 6], #vertical
                6: [2, 3], #horizontal
                7: [0, 1, 4, 5, 6], #vertical
                8: [1, 2, 4], #horizontal
                9: [0, 1, 5, 6], #vertical
                10: [2, 3, 4], #horizontal
                11: [0, 1, 6], #vertical
                12: [0, 1, 2, 3, 4, 5], #horizontal
            }, (2, 4), (5, 3)),
            TypeTableau._5: ({
                0: [0, 1, 2, 3, 4, 5], #horizontal
                1: [0, 1, 3, 6], #vertical
                2: [3], #horizontal
                3: [0, 1, 2, 3, 5, 6], #vertical
                4: [4], #horizontal
                5: [0, 2, 3, 4, 6], #vertical
                6: [1, 2, 5], #horizontal
                7: [0, 2, 4, 5, 6], #vertical
                8: [0], #horizontal
                9: [0, 2, 3, 4, 6], #vertical
                10: [1, 2, 4], #horizontal
                11: [0, 4, 6], #vertical
                12: [0, 1, 2, 3, 4, 5], #horizontal
            }, (0, 4), (4, 2)),
            TypeTableau._6: ({
                0: [0, 1, 2, 3, 4, 5], #horizontal
                1: [0, 4, 6], #vertical
                2: [1, 2], #horizontal
                3: [0, 1, 3, 5, 6], #vertical
                4: [2, 3, 4], #horizontal
                5: [0, 2, 4, 6], #vertical
                6: [0, 1, 3, 5], #horizontal
                7: [0, 2, 5, 6], #vertical
                8: [3, 4], #horizontal
                9: [0, 1, 2, 5, 6], #vertical
                10: [1, 2, 3], #horizontal
                11: [0, 6], #vertical
                12: [0, 1, 2, 3, 4, 5], #horizontal
            }, (0, 1), (5, 1)),
            TypeTableau._7: ({
                0: [0, 1, 2, 3, 4, 5], #horizontal
                1: [0, 1, 4, 6], #vertical
                2: [2], #horizontal
                3: [0, 3, 5, 6], #vertical
                4: [1, 2, 3, 4], #horizontal
                5: [0, 1, 5, 6], #vertical
                6: [2, 3], #horizontal
                7: [0, 1, 3, 6], #vertical
                8: [1, 3, 4, 5], #horizontal
                9: [0, 1, 2, 6], #vertical
                10: [2, 3, 4, 5], #horizontal
                11: [0, 6], #vertical
                12: [0, 1, 2, 3, 4, 5], #horizontal
            }, (0, 3), (3, 2)),
            TypeTableau._8: ({
                0: [0, 1, 2, 3, 4, 5], #horizontal
                1: [0, 1, 6], #vertical
                2: [2, 3], #horizontal
                3: [0, 1, 2, 4, 5, 6], #vertical
                4: [3], #horizontal
                5: [0, 3, 5, 6], #vertical
                6: [1, 2, 4], #horizontal
                7: [0, 1, 2, 4, 6], #vertical
                8: [3, 4], #horizontal
                9: [0, 1, 2, 3, 5, 6], #vertical
                10: [5], #horizontal
                11: [0, 2, 4, 6], #vertical
                12: [0, 1, 2, 3, 4, 5], #horizontal
            }, (1, 2), (4, 0)),
        }
        self.initialiser_tableau()

    def initialiser_tableau(self):
        self.cases: list[list[Case]] = []
        for i in range(self.max_row):
            cases: list[Case] = []
            for j in range(self.max_col):
                cases.append(Case(i, j))
            self.cases.append(cases)

    def set_type(self, type: TypeTableau):
        self.clear()
        self.add_a(*self.types[type][1])
        self.add_b(*self.types[type][2])
        if self.depart is not None:
            case = self.cases[self.depart[0]][self.depart[1]]
            if case.type == TypeCase.VIDE:
                case.setType(TypeCase.DEPART)
            else:
                self.depart = None
        if self.arrivee is not None:
            case = self.cases[self.arrivee[0]][self.arrivee[1]]
            if case.type == TypeCase.VIDE:
                case.setType(TypeCase.ARRIVEE)
            else:
                self.arrivee = None
        self.afficher_solution()

    def clear_type(self):
        self.clear()
        if self.depart is not None:
            self.cases[self.depart[0]][self.depart[1]].setType(TypeCase.DEPART)
        if self.arrivee is not None:
            self.cases[self.arrivee[0]][self.arrivee[1]].setType(TypeCase.ARRIVEE)
        if(self.a is not None):
            x, y = self.get_coords(*self.a)
            self.cases[x][y].setType(TypeCase.VIDE)
        if(self.b is not None):
            x, y = self.get_coords(*self.b)
            self.cases[x][y].setType(TypeCase.VIDE)
        self.a = None
        self.b = None

    def clic(self, x: int, y: int, type: TypeCase):
        match type:
            case TypeCase.DEPART:
                self.depart = None
                self.cases[x][y].setType(TypeCase.VIDE)
                self.afficher_solution()
            case TypeCase.ARRIVEE:
                self.arrivee = None
                self.cases[x][y].setType(TypeCase.VIDE)
                self.afficher_solution()
            case TypeCase.VIDE:
                if self.depart is None:
                    self.depart = (x, y)
                    self.cases[x][y].setType(TypeCase.DEPART)
                elif self.arrivee is None:
                    self.arrivee = (x, y)
                    self.cases[x][y].setType(TypeCase.ARRIVEE)
                self.afficher_solution()
            case _:
                pass

    def do(self, parent, row: int):
        self.tableau = self.placer_tableau(parent, row)
        self.solution = self.placer_solution(parent, row)

    def undo(self):
        if self.tableau is not None:
            self.depart = None
            self.arrivee = None
            self.clear_type()
            self.tableau.destroy()
            self.tableau = None
        if self.solution is not None:
            self.solution.destroy()
            self.solution = None

    def placer_tableau(self, parent, row: int):
        composante = Frame(parent)
        composante.grid(row=row)
        for i in range(self.max_row):
            for j in range(self.max_col):
                self.cases[i][j].placer_case(composante, i, j, lambda x, y, type: self.clic(x, y, type))
        return composante

    def placer_solution(self, parent, row: int):
        composante = Frame(parent)
        composante.grid(row=row+1)
        texte = self.get_solution()
        self.conclusion = Conclusion(composante, texte)
        return composante

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

    def get_solution(self) -> str:
        solution = self.solve()
        if solution == []:
            return "Pas de solution"
        else:
            lignes = [" -> ".join(x) for x in zip(solution[0::3], solution[1::3], solution[2::3])]
            n_deplacements = len(solution)
            if n_deplacements % 3 == 2:
                lignes.append(" -> ".join(solution[-2:]))
            elif n_deplacements % 3 == 1:
                lignes.append(solution[-1])
            return "\n".join(lignes)

    def solve(self) -> list[str]:
        if(self.depart is None or self.arrivee is None):
            return []

        # Construire le graphe des déplacements possibles
        graphe: dict[tuple[int, int], list[tuple[int, int]]] = {}
        for i in range(1, 13, 2):
            for j in range(1, 13, 2):
                noeud = (i, j)
                voisins: list[tuple[int, int]] = []
                # Vérifier déplacement haut
                if i - 2 >= 0 and self.cases[i-1][j].type == TypeCase.MUR_VIDE:
                    voisins.append((i-2, j))
                # Vérifier déplacement bas
                if i + 2 < 13 and self.cases[i+1][j].type == TypeCase.MUR_VIDE:
                    voisins.append((i+2, j))
                # Vérifier déplacement gauche
                if j - 2 >= 0 and self.cases[i][j-1].type == TypeCase.MUR_VIDE:
                    voisins.append((i, j-2))
                # Vérifier déplacement droite
                if j + 2 < 13 and self.cases[i][j+1].type == TypeCase.MUR_VIDE:
                    voisins.append((i, j+2))
                graphe[noeud] = voisins

        # Algorithme de Dijkstra
        file_priorite: list[tuple[int, tuple[int, int]]] = []
        heapq.heappush(file_priorite, (0, self.depart))
        predecesseurs: dict[tuple[int, int], tuple[int, int]] = {}
        couts = {noeud: float('inf') for noeud in graphe}
        couts[self.depart] = 0
        while file_priorite.count != 0:
            cout_actuel, noeud_actuel = heapq.heappop(file_priorite)
            if noeud_actuel == self.arrivee:
                break
            if cout_actuel > couts[noeud_actuel]:
                continue
            for voisin in graphe[noeud_actuel]:
                nouveau_cout = cout_actuel + 1
                if nouveau_cout < couts[voisin]:
                    couts[voisin] = nouveau_cout
                    predecesseurs[voisin] = noeud_actuel
                    heapq.heappush(file_priorite, (nouveau_cout, voisin))

        # Reconstituer le chemin
        chemin: list[tuple[int, int]] = []
        noeud_courant: tuple[int, int] | None = self.arrivee
        if noeud_courant not in predecesseurs and noeud_courant != self.depart:
            return []
        while noeud_courant is not None:
            chemin.append(noeud_courant)
            noeud_courant = predecesseurs.get(noeud_courant, None)
        chemin.reverse()
        if chemin[0] != self.depart:
            return []

        # Convertir le chemin en directions
        directions: list[str] = []
        for i in range(len(chemin)-1):
            x1, y1 = chemin[i]
            x2, y2 = chemin[i+1]
            if x2 > x1:
                directions.append("bas")
            elif x2 < x1:
                directions.append("haut")
            elif y2 > y1:
                directions.append("droite")
            elif y2 < y1:
                directions.append("gauche")
        return directions

    def afficher_solution(self):
        self.conclusion.setText("Chargement...")
        texte = self.get_solution()
        self.conclusion.setText(texte)

