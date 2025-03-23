from tkinter import Frame
from typing import Callable
from .options import Options
from .texte import Texte

class Etape(Frame):
    def __init__(self, parent: Frame, row: int, texte: str, command: Callable[[int], None], options: dict[int, str] = {}):
        super().__init__(parent)
        self.grid(row=row)
        self.texte = Texte(self, 0, texte)
        if len(options.items()) != 0:
            self.options = Options(self, 1, options)
            for scan in options.keys():
                self.options.add_command(scan, command)
        else:
            self.options = None

    def clic(self, i: int):
        if(self.options is not None):
            #if self.options.is_active(i):
                #self.options.desactiver(i)
            #else:
            self.options.activer(i)
