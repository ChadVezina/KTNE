from tkinter import Frame
from typing import Callable
from .etape import Etape
from .tableau import Tableau
from ..tools.enums import TypeTableau

class NextLink:
    def __init__(
        self,
        texte: str,
        options: dict[int, str],
        actions: list[Callable[[int], TypeTableau | None]] = [],
        ):
        self.texte = texte
        self.options = options
        self.actions = actions
        self.tableau: Tableau = Tableau()
        self.etape: Etape | None = None
        self.type: TypeTableau | None = None

    def do(self, parent: Frame, row: int):
        self.destroy()
        self.parent = parent
        self.row = row
        self.etape = Etape(parent, row, self.texte, self.options, lambda scan: self.clic(scan))
        self.tableau.do(parent, row + 1)
        if len(self.options.items()) != 0:
            self.next(self.etape.options.get_active_option())

    def destroy(self):
        if self.tableau is not None:
            self.tableau.destroy()
        if(self.etape is not None):
            self.etape.destroy()
            self.etape = None
            self.parent = None
            self.row = None

    def clic(self, scan: int):
        if(self.etape is not None):
            self.etape.clic(scan)
            self.next(self.etape.options.get_active_option())

    def next(self, active_option: int):
        for condition in self.actions:
            action = condition(active_option)
            if action is not None:
                self.tableau.set_type(action)
                return
        self.tableau.clear_type()
