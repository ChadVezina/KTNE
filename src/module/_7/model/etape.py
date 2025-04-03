from tkinter import Frame
from typing import Callable
from .options import Options
from model.texte import Texte

class Etape(Frame):
    def __init__(self, parent: Frame, row: int, commande: Callable[[], None]):
        super().__init__(parent)
        self.grid(row=row)
        self.texte = Texte(self, 0)
        self.options = Options(self, 1, commande)
