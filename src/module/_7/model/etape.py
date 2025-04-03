from tkinter import Frame
from typing import Callable
from .options import Options
from model.texte import Texte
from model.root import Root

class Etape(Root):
    def __init__(self, parent: Frame, row: int, commande: Callable[[], None]):
        super().__init__(parent, row)
        self.texte = Texte(self, 0)
        self.options = Options(self, 1, commande)
