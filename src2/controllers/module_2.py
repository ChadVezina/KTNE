from models.main import Model
from views.main import View


class Module2Controller:
    def __init__(self, name: str, model: Model, view: View) -> None:
        self.name = name
        self.model = model
        self.view = view
        self.frame = self.view.views[name]
        self.frame.is_state = lambda key, value: self.view.is_state(name, key, value)
        self.frame.update_state = lambda key, value: self.view.update_state(name, key, value)
        self._bind()
        self.init()

    def init(self) -> None:
        #self.frame.is_state = lambda key, value: self.view.is_state(self.name, key, value)
        #self.frame.update_state = lambda key, value: self.view.update_state(self.name, key, value)
        self.frame.init()

    def refresh(self) -> None:
        self.frame.refresh()

    def _bind(self) -> None:
        self.frame.module1.config(command=self.module1)

    def module1(self) -> None:
        self.view.switch(self.module1.__name__)
