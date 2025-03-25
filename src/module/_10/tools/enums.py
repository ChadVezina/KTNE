from enum import Enum

class TypeCase(Enum):
    POINT_A = 0 # cercle A
    POINT_B = 1 # cercle B
    DEPART = 2 # point blanc
    ARRIVEE = 3 # triangle rouge
    MUR = 4 # | ou -
    MUR_VIDE = 5 #
    VIDE = 6 # .

class TypeTableau(Enum):
    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
