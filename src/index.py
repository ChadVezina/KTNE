from tkinter import Tk
from module._1.main import Module_1
from module._2.main import Module_2
from module._3.main import Module_3
from module._4.main import Module_4
from constants.fenetre import N_MODULES
from tools.functions import calculateSize


def getModule(numero, fenetre, geometry):
    match numero:
        case 2:
            return Module_2(fenetre, geometry)
        case 3:
            return Module_3(fenetre, geometry)
        case 4:
            return Module_4(fenetre, geometry)
        case _:
            pass


fenetre = Module_1()
geometries = calculateSize(fenetre, N_MODULES)
fenetre.geometry(geometries.pop(0))

for module in range(1, N_MODULES):
    getModule(module+1, fenetre, geometries.pop(0))

fenetre.mainloop()
