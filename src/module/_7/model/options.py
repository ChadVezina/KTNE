from tkinter import Frame
from typing import Callable
from model.texte import Texte
from model.input import Input
from constants.config import GridPad

class Options(Frame):
    def __init__(self, parent: Frame, row: int, commande: Callable[[], None], n_options: int = 6):
        super().__init__(parent)
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        self.n_options = n_options
        self.inputs: dict[int, Input] = {}
        self.labels: dict[int, Texte] = {}
        self.make_options(commande)

    def make_options(self, commande: Callable[[], None]):
        for scan in range(self.n_options):
            self.inputs[scan] = Input(self, scan)
            self.labels[scan] = Texte(self, scan, 1)
        for scan in range(self.n_options):
            self.add_command(scan, commande)

    def add_command(self, scan: int, commande: Callable[[], None]):
        self.inputs[scan].bind("<KeyRelease>", lambda e: commande())

    def get_label(self, scan: int) -> str:
        return self.labels[scan].get_texte()

    def get_labels(self):
        labels: dict[str, int] = {}
        for scan in range(self.n_options):
            texte = self.get_label(scan)
            if(texte == ""):
                continue
            label = labels.get(texte, 0)
            labels[texte] = label + 1
        return labels

    def get_option(self, scan: int):
        return self.inputs[scan].get_texte()

    def get_options(self):
        options: list[str] = []
        for scan in range(self.n_options):
            options.append(self.get_option(scan))
        return options

    def is_exist(self, scan: int, texte: str):
        self.inputs[scan].is_exist()
        self.labels[scan].set_texte(texte)

    def is_not_exist(self, scan: int):
        self.inputs[scan].is_not_exist()
        self.labels[scan].clear_texte()
