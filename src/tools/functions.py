from tkinter import Tk, Toplevel, Frame, Button, Menu, Toplevel, Text, INSERT, DISABLED, WORD
from typing import Callable

from constants.config import TextPad, ButtonPad, Font
from constants.fenetre import Titre, PHASE_X, PHASE_Y, DEPHASE_X, DEPHASE_Y
from constants.instructions import Titre as NewTitre, Contenu


def make_menu(root: Tk | Toplevel, nouvelle: Callable, quitter: Callable, titre: Titre, contenu: Contenu):
    new_titre = NewTitre.get_value_by_index(titre.index())
    root.title(titre.value)
    root.resizable(True, True)

    root.bind("<Control-n>", lambda event: nouvelle())
    root.bind("<Alt-F4>", lambda event: quitter())

    popup_menu = Menu(root, tearoff=0)
    popup_menu.add_command(label="Nouvelle", command=nouvelle, accelerator="Ctrl+N")
    popup_menu.add_separator()
    popup_menu.add_command(label="Quitter", command=quitter, accelerator="Alt+F4")

    menu = Menu(root)
    menu.add_cascade(label="Fichier", menu=popup_menu)
    menu.add_command(label="Instructions", command=lambda root=root, titre=new_titre, contenu=contenu: show_instructions(root, titre, contenu))

    root.config(menu=menu)


def show_instructions(root: Tk | Toplevel, titre: str | None, contenu: Contenu):
    instructions_window = Toplevel(root)
    instructions_window.title(titre if titre is not None else "Instructions")

    instructions_text = Text(instructions_window, wrap=WORD, font=Font.BODY, padx=TextPad.PADDING_X, pady=TextPad.PADDING_Y, width=30, height=15)
    instructions_text.insert(INSERT, contenu.value)
    instructions_text.config(state=DISABLED)
    instructions_text.pack()

    ok_button = Button(instructions_window, font=Font.BODY, text="OK", command=instructions_window.destroy)
    ok_button.pack(padx=ButtonPad.PADDING_X, pady=ButtonPad.PADDING_Y)


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
