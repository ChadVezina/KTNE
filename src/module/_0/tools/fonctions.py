from tkinter import Label, Entry, Button, Menu, Toplevel, Text, E, INSERT, DISABLED, WORD

from constants.config import GridPad, TextPad, ButtonPad, EntrySize, Font


def make_label(root, texte, rangee, colonne = 0):
    composante = Label(root, font = Font.BODY, text = texte)
    composante.grid(row = rangee, column = colonne, padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)
    return composante


def make_label_entry(root, texte, rangee, colonne = 0):
    composante = Label(root, font = Font.BODY, text = texte)
    composante.grid(row = rangee, column = colonne, padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y, sticky = E)
    entry = Entry(root, font = Font.BODY, width = EntrySize.WIDTH)
    entry.grid(row = rangee, column = (colonne+1), padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)
    return entry


def make_bouton(root, texte, rangee, colonne = 0):
    composante = Button(root, font = Font.BODY, text = texte)
    composante.grid(row = rangee, column = colonne, padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)
    return composante


def make_menu(root, nouvelle, configurer, charger, sauvegarder, quitter):
    root.bind("<Control-n>", lambda event: nouvelle())
    root.bind("<Control-comma>", lambda event: configurer())
    root.bind("<Control-o>", lambda event: charger())
    root.bind("<Control-s>", lambda event: sauvegarder())
    root.bind("<Alt-F4>", lambda event: quitter())

    popup_menu = Menu(root, tearoff = 0)
    popup_menu.add_command(label = "Nouvelle", command = nouvelle, accelerator = "Ctrl+N")
    popup_menu.add_command(label = "Configurer", command = configurer, accelerator = "Ctrl+,")
    popup_menu.add_separator()
    popup_menu.add_command(label = "Charger", command = charger, accelerator = "Ctrl+O")
    popup_menu.add_command(label = "Sauvegarder", command = sauvegarder, accelerator = "Ctrl+S")
    popup_menu.add_separator()
    popup_menu.add_command(label = "Quitter", command = quitter, accelerator = "Alt+F4")

    menu = Menu(root)
    menu.add_cascade(label = "Fichier", menu = popup_menu)
    menu.add_command(label = "Instructions", command = show_instructions)

    root.config(menu = menu)


def validate_entry(entry, message):
    if entry.isdigit():
        if int(entry) not in range(1, 31):
            raise ValueError(message + ": Le nombre doit être compris entre 1 et 30")
    else:
        raise TypeError(message + ": L'entrée doit être un entier")
    return int(entry)


def validate_entry_mines(lignes, colonnes, mines):
    if lignes * colonnes < mines:
        raise ValueError("Le nombre de mines doit être inférieur au nombre de cases")


def show_instructions():
    instructions_window = Toplevel()
    instructions_window.title("Instructions du jeu Démineur")

    instructions_text = Text(instructions_window, wrap = WORD, font = Font.BODY, padx = TextPad.PADDING_X, pady = TextPad.PADDING_Y, width = 30, height = 15)
    instructions_text.insert(INSERT,
    """Le Démineur est un jeu de réflexion dont le but est de localiser des mines cachées dans un champ de cases.

1. Le jeu commence avec un plateau de cases non révélées.
2. Chaque case contient soit une mine, soit un nombre indiquant le nombre de mines adjacentes, soit rien (si aucune mine n'est adjacente).
3. Cliquez sur une case pour la révéler. Si vous cliquez sur une mine, vous perdez. Sinon, le nombre de mines adjacentes sera affiché.
4. Pour marquer une case que vous pensez contenir une mine, faites un clic droit dessus. Cela place un drapeau sur la case.
5. Le but du jeu est de révéler toutes les cases qui ne contiennent pas de mines, sans cliquer sur une mine.
6. Vous gagnez si vous révélez toutes les cases sans mines et marquez correctement toutes les mines avec des drapeaux.

Bonne chance !""")
    instructions_text.config(state = DISABLED)
    instructions_text.pack()

    ok_button = Button(instructions_window, font = Font.BODY, text = "OK", command = instructions_window.destroy)
    ok_button.pack(padx = ButtonPad.PADDING_X, pady = ButtonPad.PADDING_Y)
