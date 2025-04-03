from tkinter import Frame

class Root(Frame):
    def __init__(self, parent: Frame, row: int):
        super().__init__(parent)
        self.grid(row=row)
