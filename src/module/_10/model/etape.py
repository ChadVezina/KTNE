from tkinter import Frame
from typing import Callable

from model.texte import Texte
from model.options_single import Options

class Etape(Frame):
    def __init__(self, parent: Frame, row: int, texte: str, options: dict[int, str], command: Callable[[int], None]):
        super().__init__(parent)
        self.grid(row = row)
        self.texte = Texte(self, 0, 0, texte)
        self.options = Options(self, 1, options, command)

    def clic(self, i: int):
        if self.options.is_active(i):
            self.options.desactiver(i)
        else:
            self.options.activer(i)
