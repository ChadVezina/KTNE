from tkinter import Frame
from .case import Case
from .root import Root
from ..tools.enums import TypeConnexion, TypeFil


class Tableau:
    def __init__(self):
        self.length = 9
        self.table = {
            TypeFil.ROUGE: [
                [TypeConnexion.C],
                [TypeConnexion.B],
                [TypeConnexion.A],
                [TypeConnexion.A, TypeConnexion.C],
                [TypeConnexion.B],
                [TypeConnexion.A, TypeConnexion.C],
                [TypeConnexion.A, TypeConnexion.B, TypeConnexion.C],
                [TypeConnexion.A, TypeConnexion.B],
                [TypeConnexion.B],
            ],
            TypeFil.BLEU: [
                [TypeConnexion.B],
                [TypeConnexion.A, TypeConnexion.C],
                [TypeConnexion.B],
                [TypeConnexion.A],
                [TypeConnexion.B],
                [TypeConnexion.B, TypeConnexion.C],
                [TypeConnexion.C],
                [TypeConnexion.A, TypeConnexion.C],
                [TypeConnexion.A],
            ],
            TypeFil.NOIR: [
                [TypeConnexion.A, TypeConnexion.B, TypeConnexion.C],
                [TypeConnexion.A, TypeConnexion.C],
                [TypeConnexion.B],
                [TypeConnexion.A, TypeConnexion.C],
                [TypeConnexion.B],
                [TypeConnexion.B, TypeConnexion.C],
                [TypeConnexion.A, TypeConnexion.B],
                [TypeConnexion.C],
                [TypeConnexion.C],
            ],
        }
        self.root: Root | None = None
        self.initialiser_tableau()

    def do(self, parent: Frame, row: int):
        self.destroy()
        self.parent = parent
        self.row = row
        self.root = Root(parent, row)
        self.placer_tableau(self.root)

    def destroy(self):
        if(self.root is not None):
            self.root.destroy()
            self.root = None
            self.parent = None
            self.row = None

    def initialiser_tableau(self):
        self.cases: list[Case] = []
        for i in range(self.length):
            self.cases.append(Case(i, lambda numero: self.clic(numero)))

    def placer_tableau(self, parent):
        for scan in range(self.length):
            self.cases[scan].placer_case(parent)

    def clic(self, numero: int):
        for scan, case in enumerate(self.cases, numero+1):
            if case.is_active:
                case.clear_solution()
        rouge = 0
        bleu = 0
        noir = 0
        for scan, case in enumerate(self.cases):
            if not case.is_active:
                return
            match case.type:
                case TypeFil.ROUGE:
                    table = self.table[TypeFil.ROUGE][rouge].copy()
                    case.add_solution(lambda connexion: connexion in table)
                    rouge += 1
                case TypeFil.BLEU:
                    table = self.table[TypeFil.BLEU][bleu].copy()
                    case.add_solution(lambda connexion: connexion in table)
                    bleu += 1
                case TypeFil.NOIR:
                    table = self.table[TypeFil.NOIR][noir].copy()
                    case.add_solution(lambda connexion: connexion in table)
                    noir += 1
                case _:
                    pass
