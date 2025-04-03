from tkinter import Frame
from typing import Callable
from .conclusion import Conclusion
from model.etape import Etape

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
        self.etape: Etape | Conclusion | None = None
        self.next_link: NextLink | None = None

    def do(self, parent: Frame, row: int, historique: list[str] = []):
        self.destroy()
        self.parent = parent
        self.row = row
        self.historique = historique
        if len(self.options.items()) = = 0:
            etapes = historique.copy()
            etapes.append(self.texte)
            self.etape = Conclusion(parent, row, etapes, 3)
        else:
            self.etape = Etape(parent, row, self.texte, self.options, lambda scan: self.clic(scan), False)
            self.next(-1)

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
            active_options = self.etape.options.get_active_options()
            active_option = -1 if len(active_options) = = 0 else active_options[0]
            self.next(active_option)
            if(self.next_link is not None):
                self.next_link.historique.append(self.next_link.texte)

    def next(self, active_option: int):
        next_link: NextLink | None = None
        historique: list[str] = []
        if(self.next_link is not None):
            historique = self.next_link.historique.copy()
            self.next_link.destroy()
            if len(self.next_link.options.items()) = = 0:
                next_link = self.next_link
            self.next_link = None
        for condition in self.actions:
            action = condition(active_option)
            if action is not None:
                self.next_link = action
                self.next_link.do(self.parent, self.row + 1, historique)
                return
        if next_link is not None:
            self.next_link = next_link
            self.next_link.do(self.parent, self.row + 1, historique)
