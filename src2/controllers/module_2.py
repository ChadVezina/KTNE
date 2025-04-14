from models.main import Model
from views.main import View


class Module2Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["module2"]
        self._bind()
        self.init()

    def init(self) -> None:
        self.frame.is_state = self.model.auth.is_state
        self.frame.update_state = self.model.auth.update
        self.frame.init()

    def _bind(self) -> None:
        self.frame.module1.config(command=self.module1)

    def module1(self) -> None:
        self.view.switch("module1")
