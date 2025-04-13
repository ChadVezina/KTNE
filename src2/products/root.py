from tkinter import Frame

class Root(Frame):
    def __init__(self, parent: Frame, row: int = 0, visible: bool = True):
        super().__init__(parent)
        self.row = row
        if visible:
            self.grid(row = row)

    def hide(self) -> None:
        if self.winfo_ismapped():
            self.grid_remove()

    def show(self) -> None:
        self.hide()
        self.grid(row = self.row)

    def place(self, row: int = -1) -> None:
        if row != -1:
            self.row = row
        self.show()
