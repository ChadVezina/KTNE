from tkinter import Frame
from typing import Callable
from .etape import Etape

class NextLink:
    def __init__(
        self,
        ):
        self.mots = [
            "about",
            "after",
            "again",
            "below",
            "could",
            "every",
            "first",
            "found",
            "great",
            "house",
            "large",
            "learn",
            "never",
            "other",
            "place",
            "plant",
            "point",
            "right",
            "small",
            "sound",
            "spell",
            "still",
            "study",
            "their",
            "there",
            "these",
            "thing",
            "think",
            "three",
            "water",
            "where",
            "which",
            "world",
            "would",
            "write",
        ]
        self.etape: Etape | None = None

    def do(self, parent: Frame, row: int):
        self.destroy()
        self.parent = parent
        self.row = row
        self.etape = Etape(parent, row, lambda: self.clic())

    def destroy(self):
        if(self.etape is not None):
            self.etape.destroy()
            self.etape = None
            self.parent = None
            self.row = None

    def scan_options(self, options: list[str]):
        mots_acceptes: list[str] = []
        for mot in self.mots:
            is_mot_accepte = True
            for scan, option in enumerate(options):
                is_accepte = True if option == "" else False
                for letter in option:
                    if(mot[scan] == letter):
                        is_accepte = True
                        break
                if is_accepte == False:
                    is_mot_accepte = False
                    break
            if is_mot_accepte == True:
                mots_acceptes.append(mot)
        if len(mots_acceptes) == 0:
            return "Aucun mot trouvé"
        elif len(mots_acceptes) < 6:
            return "\n".join(mots_acceptes)
        return "\n".join(mots_acceptes[0:5])

    def clic(self):
        if(self.etape is not None):
            options = self.etape.options.get_options()
            texte = self.scan_options(options)
            self.etape.texte.set_texte(texte)
