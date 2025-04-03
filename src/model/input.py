from tkinter import Entry, StringVar
from constants.config import GridPad, Font

class Input(Entry):
    def __init__(self, parent, row, col=0):
        self.sv = StringVar()
        super().__init__(parent, font=Font.BODY, textvariable=self.sv, bg="white")
        self.grid(row=row, column=col, padx=GridPad.PADDING_X, pady=GridPad.PADDING_Y)

    def get_texte(self):
        return self.sv.get().lower().strip()

    def is_exist(self):
        self["bg"] = "green"

    def is_not_exist(self):
        self["bg"] = "white"
