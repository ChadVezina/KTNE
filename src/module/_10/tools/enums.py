from enum import Enum

class TypeCase(Enum):
    POINT_A = 0 # cercle A
    POINT_B = 1 # cercle B
    DEPART = 2 # point blanc
    ARRIVEE = 3 # triangle rouge
    MUR = 4 # | ou -
    VIDE = 5 # .
