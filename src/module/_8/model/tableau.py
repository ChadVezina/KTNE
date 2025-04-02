from tkinter import Frame
from .case import Case
from .root import Root


class Tableau:
    def __init__(self):
        self.length = 6
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
            self.cases.append(Case(i))

    def placer_tableau(self, parent):
        for scan in range(self.length):
            self.cases[scan].placer_case(parent)
