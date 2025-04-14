from models.main import Model
from views.main import View


class Module1Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.name = "module1"
        self.model = model
        self.view = view
        self.frame = self.view.views[self.name]
        self._bind()
        self.init()

    def init(self) -> None:
        self.view.root.redessiner = lambda name=self.name: self.model.auth.clear(name)
        self.frame.is_state = self.model.auth.is_state
        self.frame.update_state = self.model.auth.update
        self.frame.init()

    def _bind(self) -> None:
        self.frame.module2.config(command=self.module2)

    def module2(self) -> None:
        self.view.switch(self.module2.__name__)

