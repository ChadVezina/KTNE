from tkinter import Frame, Entry, StringVar
from typing import Callable
from constants.config import GridPad, Font

class Options(Frame):
    def __init__(self, parent: Frame, row: int, commande: Callable[[], None]):
        super().__init__(parent)
        self.grid(row = row, padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)
        self.sv: dict[int, StringVar] = {}
        self.inputs: dict[int, Entry] = {}
        self.make_options(commande)

    def make_options(self, commande: Callable[[], None]):
        for scan in range(5):
            self.sv[scan] = StringVar()
            self.inputs[scan] = self.make_entry(scan)
            self.inputs[scan].bind("<KeyRelease>", lambda e: commande())

    def make_entry(self, colonne: int):
        x = colonne // 2
        y = colonne % 2
        input = Entry(self, font = Font.BODY, textvariable = self.sv[colonne], bg = "white")
        input.grid(row = x, column = y, padx = GridPad.PADDING_X, pady = GridPad.PADDING_Y)
        return input

    def get_option(self, scan: int):
        return self.sv[scan].get().lower().strip()

    def get_options(self):
        options: list[str] = []
        for scan in range(5):
            options.append(self.get_option(scan))
        return options
