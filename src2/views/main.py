from typing import TypedDict, get_type_hints

from .root import Root
from .module_1 import Module1View
from .module_2 import Module2View


class Views(TypedDict):
    module1: Module1View
    module2: Module2View

    @staticmethod
    def items():
        return get_type_hints(Views).items()


class View:
    def __init__(self):
        self.root = Root()
        self.views: Views = {}
        for name, View in Views.items():
            self._add_view(name, View)

    @property
    def name(self) -> str:
        return self.root.name

    def _add_view(self, name: str, View) -> None:
        self.views[name] = View(self.root.cadre)
        self.views[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        self.root.name = name
        frame = self.views[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()

