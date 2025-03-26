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
    def str_value(self):
        match self.value:
            case 0:
                return "Couper le fil"
            case 1:
                return "Ne pas couper le fil"
            case 2:
                return "Couper le fil si le dernier chiffre du numéro de série est pair"
            case 3:
                return "Couper le fil si la bombe a un port parallèle"
            case 4:
                return "Couper le fil si la bombe a deux piles ou plus"
            case _:
                pass
