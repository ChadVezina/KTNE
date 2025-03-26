from enum import Enum


class TypeFil(Enum):
    ROUGE = 0
    BLEU = 1
    ETOILE = 2
    LUMIERE_ALLUMEE = 3


class TypeSolution(Enum):
    C = 0
    N = 1
    S = 2
    P = 3
    B = 4

    @property
    def str_value2(self):
        match self.value:
            case 0:
                return "C"
            case 1:
                return "N"
            case 2:
                return "S"
            case 3:
                return "P"
            case 4:
                return "B"
            case _:
                pass

    @property
    def str_value(self):
        match self.value:
            case 0:
                return "Couper le fil"
            case 1:
                return "Ne pas couper le fil"
            case 2:
                return "Couper le fil\nsi le dernier chiffre\ndu numéro de série est pair"
            case 3:
                return "Couper le fil\nsi la bombe a\nun port parallèle"
            case 4:
                return "Couper le fil\nsi la bombe a\ndeux piles ou plus"
            case _:
                pass
