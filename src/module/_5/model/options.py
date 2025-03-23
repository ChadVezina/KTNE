from tkinter import Frame, Entry, StringVar
from typing import Callable
from ..tools.constantes import GridPad, Font

class Options(Frame):
    def __init__(self, parent: Frame, row: int, commande: Callable[[], None]):
        super().__init__(parent)
        self.grid(row=row, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        self.sv: dict[int, StringVar] = {}
        self.inputs: dict[int, Entry] = {}
        self.result: int = -1
        self.make_options(commande)

    def make_options(self, commande: Callable[[], None]):
        for scan in range(6):
            self.sv[scan] = StringVar()
            self.inputs[scan] = self.make_entry(scan)
            self.inputs[scan].bind("<KeyRelease>", lambda e: commande())

    def make_entry(self, colonne: int):
        x = colonne // 2
        y = colonne % 2
        input = Entry(self, font=Font.BODY, bg="white", textvariable=self.sv[colonne])
        input.grid(row=x, column=y, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)
        return input

    def get_option(self, scan: int):
        return self.sv[scan].get().strip()

    def get_options(self):
        options: list[str] = []
        for scan in range(6):
            options.append(self.get_option(scan))
        return options

    def get_active_option(self):
        return self.result

    def is_active(self, scan: int):
        return self.result == scan

    def is_exist(self, scan: int):
        self.inputs[scan]["bg"] = "green"

    def is_not_exist(self, scan: int):
        self.inputs[scan]["bg"] = "white"

    def activer(self, scan: int):
        if(self.result != -1 and not self.is_active(scan)):
            self.desactiver(self.result)
        self.inputs[scan]["bg"] = "pink"
        self.result = scan

    def desactiver(self, scan: int):
        if(self.is_active(scan)):
            self.inputs[scan]["bg"] = "white"
            self.result = -1
