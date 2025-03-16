from tkinter import Tk, Toplevel, Frame

from constants.fenetre import PHASE_X, PHASE_Y, DEPHASE_X, DEPHASE_Y


def get_width_height(parent: Tk | Toplevel | Frame) -> tuple[int, int]:
    screen_width = parent.winfo_screenwidth()-(DEPHASE_X//2)
    screen_height = parent.winfo_screenheight()-(DEPHASE_Y//2)-PHASE_Y
    return screen_width, screen_height


def calculate_x_y(screen_width: int, screen_height: int, length: int) -> tuple[int, int]:
    ratio = screen_width / screen_height

    unit = length / (ratio+1)
    n_x = round(unit * ratio)
    n_y = round(unit)
    diff = length - (n_x * n_y)
    while(diff < 0):
        if(ratio >= 1):
            n_x -= 1
        else:
            n_y -= 1
        diff = length - (n_x * n_y)
    while(diff > 0):
        if(ratio >= 1):
            n_y += 1
        else:
            n_x += 1
        diff = length - (n_x * n_y)
    return n_x, n_y


def calculateSize(fenetre: Tk, n_fenetres: int) -> list[str]:
    screen_width, screen_height = get_width_height(fenetre)
    n_fenetres_x, n_fenetres_y = calculate_x_y(screen_width, screen_height, n_fenetres)
    width = screen_width // n_fenetres_x
    height = screen_height // n_fenetres_y
    geometries = []
    for j in range(n_fenetres_y):
        for i in range(n_fenetres_x):
            geometries.append("{}x{}+{}+{}".format(width-DEPHASE_X, height-DEPHASE_Y, i*width-PHASE_X, j*height))
    return geometries
