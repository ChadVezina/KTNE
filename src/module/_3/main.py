from .model.tableau import Tableau
from constants.fenetre import Titre
from constants.instructions import Contenu
from model.module import Module

class Module_3(Module):
    def __init__(self, root, geometrie):
        self.caracteres0 = [
            "Ϙ", # U+03D8
            "Ѧ", # U+0466
            "ƛ", # U+019B
            "Ϟ", # U+03DE
            "Ѭ", # U+046C
            "ϗ", # U+03D7
            "Ͽ", # U+03FF
            "Ӭ", # U+04EC
            "Ҩ", # U+04A8
            "☆", # U+2606
            "¿", # U+00BF
            "©", # U+00A9
            "Ѽ", # U+047C
            "Җ", # U+0496
            "Ԇ", # U+0506
            "Ϭ", # U+03EC
            "¶", # U+00B6
            "ƀ", # U+0180
            "ټ", # U+067C
            "ψ", # U+03C8
            "Ͼ", # U+03FE
            "Ѯ", # U+046E
            "★", # U+2605
            "҂", # U+0482
            "æ", # U+00E6
            "Ҋ", # U+048A
            "Ω", # U+03A9
        ]
        self.hints0 = [
            "raquette",
            "a t",
            "lambda",
            "éclair",
            "bébite",
            "cédille",
            "c à l'envers",
            "tréma",
            "cursive",
            "étoile vide",
            "? à l'envers",
            "copyright",
            "seins",
            "double k",
            "lâche lousse",
            "6",
            "paragraphe",
            "b",
            "sourire",
            "chandelier",
            "c à l'endroit",
            "3",
            "étoile pleine",
            "cicatrice",
            "ae",
            "n h",
            "omega",
        ]
        self.hints = sorted(self.hints0.copy())
        self.caracteres = sorted(self.caracteres0.copy(), key = lambda x: self.hints.index(self.hints0[self.caracteres0.index(x)]))
        self.colonnes = [
            ["Ϙ", "Ѧ", "ƛ", "Ϟ", "Ѭ", "ϗ", "Ͽ"],
            ["Ӭ", "Ϙ", "Ͽ", "Ҩ", "☆", "ϗ", "¿"],
            ["©", "Ѽ", "Ҩ", "Җ", "Ԇ", "ƛ", "☆"],
            ["Ϭ", "¶", "ƀ", "Ѭ", "Җ", "¿", "ټ"],
            ["ψ", "ټ", "ƀ", "Ͼ", "¶", "Ѯ", "★"],
            ["Ϭ", "Ӭ", "҂", "æ", "ψ", "Ҋ", "Ω"],
        ]
        self.tableau = Tableau(self.caracteres, self.hints, self.colonnes)

        super().__init__(Titre.MODULE_3, Contenu.MODULE_3, root, geometrie)

    def redessiner(self):
        self.tableau.do(self.cadre, 0)
