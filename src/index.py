from tkinter import Tk
from module._1.main import Module_1
from module._2.main import Module_2
from module._3.main import Module_3


def calculateSize(fenetre: Tk, n_fenetres: int) -> list[str]:
    phase_x = 7
    phase_y = 20
    dephase_x = 2
    dephase_y = 50
    screen_width = fenetre.winfo_screenwidth()-(dephase_x//2)
    screen_height = fenetre.winfo_screenheight()-(dephase_y//2)-phase_y
    ratio = screen_width / screen_height
    unit = n_fenetres / (ratio+1)
    n_fenetres_x = round(unit * ratio)
    n_fenetres_y = round(unit)
    diff = n_fenetres - (n_fenetres_x * n_fenetres_y)
    while(diff != 0):
        if(diff < 0):
            if(ratio >= 1):
                n_fenetres_x -= 1
            else:
                n_fenetres_y -= 1
        elif(diff > 0):
            if(ratio >= 1):
                n_fenetres_y += 1
            else:
                n_fenetres_x += 1
        diff = n_fenetres - (n_fenetres_x * n_fenetres_y)
    width = screen_width // n_fenetres_x
    height = screen_height // n_fenetres_y
    geometries = []
    for j in range(n_fenetres_y):
        for i in range(n_fenetres_x):
            geometries.append("{}x{}+{}+{}".format(width-dephase_x, height-dephase_y, i*width-phase_x, j*height))
    return geometries


def getModule(numero, fenetre, geometry):
    match numero:
        case 2:
            return Module_2(fenetre, geometry)
        case 3:
            return Module_3(fenetre, geometry)
        case _:
            pass


fenetre = Module_1()
n_modules = 12
geometries = calculateSize(fenetre, n_modules)
fenetre.geometry(geometries.pop(0))

for module in range(1, n_modules):
    getModule(module+1, fenetre, geometries.pop(0))

fenetre.mainloop()
