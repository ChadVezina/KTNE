from typing import TypedDict

from .root import Root
from .module_1 import Module1View
from .module_2 import Module2View


class Frames(TypedDict):
    module1: Module1View
    module2: Module2View


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}

        self._name = "module1"
        self._add_frame(Module1View, "module1")
        self._add_frame(Module2View, "module2")

    @property
    def name(self) -> int:
        return self._name

    def _add_frame(self, View, name: str) -> None:
        self.frames[name] = View(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        self._name = name
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()

