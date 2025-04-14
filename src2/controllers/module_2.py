from models.main import Model
from views.main import View


class Module2Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.name = "module2"
        self.model = model
        self.view = view
        self.frame = self.view.views[self.name]
        self._bind()
        self.init()

    def init(self) -> None:
        self.view.root.redessiner = lambda name=self.name: self.model.auth.clear(name)
        self.frame.is_state = lambda key, value, name=self.name: self.model.auth.is_state(name, key, value)
        self.frame.update_state = lambda key, value, name=self.name: self.model.auth.update(name, key, value)
        self.frame.init()

    def _bind(self) -> None:
        self.frame.module1.config(command=self.module1)

    def module1(self) -> None:
        self.view.switch(self.module1.__name__)
