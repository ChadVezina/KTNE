from tkinter import Frame, Label, Button, Menu, Toplevel, Text, INSERT, DISABLED, WORD

from .constantes import GridPad, TextPad, ButtonPad, Font
from constants.instructions import Titre, Contenu


def make_question(root: Frame, texte: str, rangee: int, options: list[dict[str, str]], commandeText, commandeId):
    composante = Frame(root)
    composante.grid(row=rangee)

    label = Label(composante, font=Font.BODY, text=texte)
    label.grid(columnspan=len(options), padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
    for scan, option in enumerate(options):
        make_choix(composante, commandeText(option), commandeId(option, scan+1), 1, scan)
    return composante


def make_conclusion(root, texte, rangee):
    composante = Frame(root)
    composante.grid(row=rangee)

    label = Label(composante, font=Font.BODY, text=texte)
    label.grid(padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
    return composante


def make_choix(root, texte, commande, rangee, colonne):
    composante = Button(root, font=Font.BODY, text=texte, command=commande, bg="white")
    composante.grid(row=rangee, column=colonne, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
    return composante


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
    instructions_window.title(Titre.MODULE_2)

    instructions_text = Text(instructions_window, wrap=WORD, font=Font.BODY, padx=TextPad.PADDING_X, pady=TextPad.PADDING_Y)
    instructions_text.insert(INSERT, Contenu.MODULE_2)
    instructions_text.config(state=DISABLED)
    instructions_text.pack()

    ok_button = Button(instructions_window, font=Font.BODY, text="OK", command=instructions_window.destroy)
    ok_button.pack(padx=ButtonPad.PADDING_X, pady=ButtonPad.PADDING_Y)
