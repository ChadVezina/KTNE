from tkinter import Button, Menu, Toplevel, Text, INSERT, DISABLED, WORD

from .constantes import TextPad, ButtonPad, Font
from constants.instructions import Titre, Contenu


def make_menu(root, nouvelle, quitter):
    root.bind("<Control-n>", lambda event: nouvelle())
    root.bind("<Alt-F4>", lambda event: quitter())

    popup_menu = Menu(root, tearoff=0)
    popup_menu.add_command(label="Nouvelle", command=nouvelle, accelerator="Ctrl+N")
    popup_menu.add_separator()
    popup_menu.add_command(label="Quitter", command=quitter, accelerator="Alt+F4")

    menu = Menu(root)
    menu.add_cascade(label="Fichier", menu=popup_menu)
    menu.add_command(label="Instructions", command=show_instructions)

    root.config(menu=menu)


def show_instructions():
    instructions_window = Toplevel()
    instructions_window.title(Titre.MODULE_6.value)

    instructions_text = Text(instructions_window, wrap=WORD, font=Font.BODY, padx=TextPad.PADDING_X, pady=TextPad.PADDING_Y)
    instructions_text.insert(INSERT, Contenu.MODULE_6.value)
    instructions_text.config(state=DISABLED)
    instructions_text.pack()

    ok_button = Button(instructions_window, font=Font.BODY, text="OK", command=instructions_window.destroy)
    ok_button.pack(padx=ButtonPad.PADDING_X, pady=ButtonPad.PADDING_Y)
