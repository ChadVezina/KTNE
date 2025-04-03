from tkinter import Frame
from typing import Callable
from .options import Options
from .texte import Texte

class Etape(Frame):
    def __init__(self, parent: Frame, row: int, texte: str, options: dict[int, str], commande: Callable[[int], None], multiple: bool = True):
        super().__init__(parent)
        self.grid(row = row)
        self.multiple = multiple
        self.texte = Texte(self, 0, texte = texte)
        self.options = Options(self, 1, options, commande)

    def clic(self, i: int):
        if(not self.multiple):
            for scan in self.options.get_active_options():
                if(scan ! = i):
                    self.options.desactiver(scan)
        if self.options.is_active(i):
            self.options.desactiver(i)
        else:
            self.options.activer(i)
