from models.main import Model
from models.auth import User
from views.main import View


class Module2Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["module2"]
        self._bind()

    def _bind(self) -> None:
        self.frame.model = self.model
        self.frame.init_boutons()
        self.frame.module1.config(command=self.module1)
        self.frame.init_questions()

    def module1(self) -> None:
        self.view.switch("module1")
