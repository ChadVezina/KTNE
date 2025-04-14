from models.main import Model
from views.main import View


class Module1Controller:
    def __init__(self, name: str, model: Model, view: View) -> None:
        self.name = name
        self.model = model
        self.view = view
        self.frame = self.view.views[name]
        self._bind()
        self.init()

    def init(self) -> None:
        self.frame.is_state = lambda key, value: self.model.auth.is_state(self.name, key, value)
        self.frame.update_state = lambda key, value: self.model.auth.update(self.name, key, value)
        self.frame.init()

    def _bind(self) -> None:
        self.frame.module2.config(command=self.module2)

    def module2(self) -> None:
        self.view.switch(self.module2.__name__)

