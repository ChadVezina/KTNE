from tkinter import Frame, Entry, Label, StringVar
from typing import Callable
from ..tools.constantes import GridPad, Font

class Options(Frame):
    def __init__(self, parent: Frame, row: int, commande: Callable[[], None]):
        super().__init__(parent)
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        self.sv: dict[int, StringVar] = {}
        self.inputs: dict[int, Entry] = {}
        self.labels: dict[int, Label] = {}
        self.make_options(commande)

    def make_options(self, commande: Callable[[], None]):
        for scan in range(6):
            self.sv[scan] = StringVar()
            self.inputs[scan] = self.make_entry(scan)
            self.labels[scan] = self.make_label(scan)
            self.inputs[scan].bind("<KeyRelease>", lambda e: commande())

    def make_entry(self, colonne: int):
        input = Entry(self, font=Font.BODY, bg="white", textvariable=self.sv[colonne])
        input.grid(row=colonne, column=0, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        return input

    def make_label(self, colonne: int):
        label = Label(self, font=Font.BODY, text="", bg="white")
        label.grid(row=colonne, column=1, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        return label

    def get_label(self, scan: int):
        return self.labels[scan]["text"]

    def get_labels(self):
        labels: dict[str, int] = {}
        for scan in range(6):
            texte = self.get_label(scan)
            if(texte == ""):
                continue
            label = labels.get(texte, 0)
            labels[texte] = label + 1
        return labels

    def set_texte(self, scan: int, texte: str):
        self.labels[scan]["text"] = texte

    def desactiver(self, scan: int):
        self.labels[scan]["text"] = ""

    def get_option(self, scan: int):
        return self.sv[scan].get().strip()

    def get_options(self):
        options: list[str] = []
        for scan in range(6):
            options.append(self.get_option(scan))
        return options

    def is_exist(self, scan: int, texte: str):
        self.inputs[scan]["bg"] = "green"
        self.set_texte(scan, texte)

    def is_not_exist(self, scan: int):
        self.inputs[scan]["bg"] = "white"
        self.desactiver(scan)
