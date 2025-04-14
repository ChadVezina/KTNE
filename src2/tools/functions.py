from tkinter import Tk, Toplevel, Button, Menu, Toplevel, Text, INSERT, DISABLED, WORD
from typing import Callable

from constants.config import TextPad, ButtonPad, Font
from constants.fenetre import Titre
from constants.instructions import Titre as NewTitre, Contenu


def make_menu(root: Tk, nouvelle: Callable, quitter: Callable):
    root.resizable(True, True)

    root.bind("<Control-n>", lambda event: nouvelle())
    root.bind("<Alt-F4>", lambda event: quitter())

    popup_menu = Menu(root, tearoff = 0)
    popup_menu.add_command(label = "Nouvelle", command = nouvelle, accelerator = "Ctrl+N")
    popup_menu.add_separator()
    popup_menu.add_command(label = "Quitter", command = quitter, accelerator = "Alt+F4")

    menu = Menu(root)
    menu.add_cascade(label = "Fichier", menu = popup_menu)
    for search_index in range(len(Titre)):
        titre = Titre.get_value_by_index(search_index)
        new_titre = NewTitre.get_value_by_index(search_index)
        contenu = Contenu.get_value_by_index(search_index)
        if titre is None or new_titre is None:
            continue
        menu.add_command(label = f"Instructions: {titre}", command = lambda root = root, titre = new_titre, contenu = contenu: show_instructions(root, titre, contenu))

    root.config(menu = menu)


def show_instructions(root: Tk, titre: str | None, contenu: Contenu):
    instructions_window = Toplevel(root)
    instructions_window.title(titre if titre is not None else "Instructions")

    instructions_text = Text(instructions_window, wrap = WORD, font = Font.BODY, padx = TextPad.PADDING_X, pady = TextPad.PADDING_Y, width = 30, height = 15)
    instructions_text.insert(INSERT, contenu.value)
    instructions_text.config(state = DISABLED)
    instructions_text.pack()

    ok_button = Button(instructions_window, font = Font.BODY, text = "OK", command = instructions_window.destroy)
    ok_button.pack(padx = ButtonPad.PADDING_X, pady = ButtonPad.PADDING_Y)

