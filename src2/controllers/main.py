from typing import TypedDict, get_type_hints

from models.main import Model
from models.auth import Auth
from views.main import View

from .module_1 import Module1Controller
from .module_2 import Module2Controller


class Controllers(TypedDict):
    module1: Module1Controller
    module2: Module2Controller

    @staticmethod
    def items():
        return get_type_hints(Controllers).items()


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.view.root.redessiner = lambda name: self.model.auth.clear(name)
        self.view.root.reset = self.model.auth.reset
        self.view.root.undo = self.model.auth.undo
        self.view.is_state = lambda name, key, value: self.model.auth.is_state(name, key, value)
        self.view.update_state = lambda name, key, value: self.model.auth.update(name, key, value)
        self.controllers: Controllers = {}
        for name, Controller in Controllers.items():
            self._add_controller(name, Controller)
        self.model.auth.add_event_listener("auth_changed", self.auth_state_listener)
        self.model.auth.add_event_listener("auth_refresh", self.refresh_listener)

    def _add_controller(self, name: str, Controller) -> None:
        self.controllers[name] = Controller(name, self.model, self.view)

    def auth_state_listener(self, data: Auth) -> None:
        for name, controller in self.controllers.items():
            if name == self.view.name:
                continue
            controller.init()

    def refresh_listener(self, data: Auth) -> None:
        for _, controller in self.controllers.items():
            controller.refresh()

    def start(self) -> None:
        self.view.switch("module1")
        self.view.start_mainloop()

