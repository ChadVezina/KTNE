from tkinter import Frame
from .etape import Etape

class NextLink:
    def __init__(
        self,
        ):
        self.caracteres = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }
        self.mots = {
            "shell": "3.505 MHz",
            "halls": "3.515 MHz",
            "slick": "3.522 MHz",
            "trick": "3.532 MHz",
            "boxes": "3.535 MHz",
            "leaks": "3.542 MHz",
            "strobe": "3.545 MHz",
            "bistro": "3.552 MHz",
            "flick": "3.555 MHz",
            "bombs": "3.565 MHz",
            "break": "3.572 MHz",
            "brick": "3.575 MHz",
            "steak": "3.582 MHz",
            "sting": "3.592 MHz",
            "vector": "3.595 MHz",
            "beats": "3.600 MHz",
        }
        self.etape: Etape | None = None

    def do(self, parent: Frame, row: int):
        self.undo()
        self.parent = parent
        self.row = row
        self.etape = Etape(parent, row, lambda: self.clic())

    def undo(self):
        if(self.etape is not None):
            self.etape.destroy()
            self.etape = None
            self.parent = None
            self.row = None

    def scan_options(self, options: list[str]):
        for scan, option in enumerate(options):
            if(option in self.caracteres.values()):
                index = list(self.caracteres.values()).index(option)
                caractere = list(self.caracteres.keys())[index]
                self.etape.options.is_exist(scan, caractere)
            else:
                self.etape.options.is_not_exist(scan)

    def scan_labels(self, labels: dict[str, int]):
        solution: str | None = None
        for mot, value in self.mots.items():
            condition = True
            for label, n in labels.items():
                if mot.count(label) < n:
                    condition = False
                    break
            if condition:
                if solution is None:
                    solution = f"Mot: {mot}\nFréquence: {value}"
                else:
                    solution = None
                    break
        if(solution is None):
            self.etape.texte.desactiver()
        else:
            self.etape.texte.set_texte(solution)

    def clic(self):
        if(self.etape is not None):
            options = self.etape.options.get_options()
            self.scan_options(options)
            labels = self.etape.options.get_labels()
            self.scan_labels(labels)
