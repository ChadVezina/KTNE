from .case import Case
from ..tools.enums import TypeConnexion, TypeFil


class Tableau:
    def __init__(self):
        self.length = 6
        self.initialiser_tableau()

    def initialiser_tableau(self):
        self.cases: list[Case] = []
        for i in range(self.length):
            self.cases.append(Case(i))

    def placer_tableau(self, parent):
        for scan in range(self.length):
            self.cases[scan].placer_case(parent)
