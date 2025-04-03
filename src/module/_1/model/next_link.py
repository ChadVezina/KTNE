from tkinter import Frame
from typing import Callable
from model.texte import Texte
from model.etape import Etape

class NextLink:
    def __init__(
        self,
        texte: str,
        options: dict[int, str] = {},
        actions: list[Callable[[list[int]], "NextLink | None"]] = [],
        multiple: bool = True,
        ):
        self.texte = texte
        self.options = options
        self.actions = actions
        self.multiple = multiple
        self.etape: Etape | Texte | None = None
        self.next_link: NextLink | None = None

    def do(self, parent: Frame, row: int):
        self.destroy()
        self.parent = parent
        self.row = row
        if len(self.options.items()) == 0:
            self.etape = Texte(parent, row, self.texte)
        else:
            self.etape = Etape(parent, row, self.texte, self.options, lambda scan: self.clic(scan), self.multiple)
            self.next(self.etape.options.get_active_options())

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
            self.next(self.etape.options.get_active_options())

    def next(self, active_options: list[int]):
        if(self.next_link is not None):
            self.next_link.destroy()
            self.next_link = None
        for condition in self.actions:
            action = condition(active_options)
            if action is not None:
                self.next_link = action
                self.next_link.do(self.parent, self.row + 1)
                return
