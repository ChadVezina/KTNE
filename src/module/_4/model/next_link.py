from tkinter import Frame
from typing import Callable
from .etape import Etape

class NextLink:
    def __init__(
        self,
        texte: str,
        options: dict[int, str] = {},
        actions: list[Callable[[int], "NextLink | None"]] = [],
        ):
        self.texte = texte
        self.options = options
        self.actions = actions
        self.etape: Etape | None = None
        self.next_link: NextLink | None = None

    def do(self, parent: Frame, row: int, historique: list[str] = []):
        self.destroy()
        self.parent = parent
        self.row = row
        self.historique = historique
        if len(self.options.items()) == 0:
            etapes = historique.copy()
            etapes.append(self.texte)
            self.etape = Etape(parent, row, etapes, lambda scan: self.clic(scan), self.options)
        else:
            self.etape = Etape(parent, row, self.texte, lambda scan: self.clic(scan), self.options)
        if len(self.options.items()) != 0:
            self.next(self.etape.options.get_active_option())

    def destroy(self):
        if(self.next_link is not None):
            self.next_link.destroy()
            self.next_link = None
        if(self.etape is not None):
            self.etape.destroy()
            self.etape = None
            self.parent = None
            self.row = None

    def clic(self, scan: int):
        if(self.etape is not None):
            self.etape.clic(scan)
            self.next(self.etape.options.get_active_option())
            if(self.next_link is not None):
                self.next_link.historique.append(self.next_link.texte)

    def next(self, active_option: list[int]):
        historique: list[str] = []
        if(self.next_link is not None):
            historique = self.next_link.historique.copy()
            self.next_link.destroy()
            self.next_link = None
        for condition in self.actions:
            action = condition(active_option)
            if action is not None:
                self.next_link = action
                self.next_link.do(self.parent, self.row + 1, historique)
                return
