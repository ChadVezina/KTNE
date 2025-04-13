from models.main import Model
from views.main import View


class Module1Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["module1"]
        self.init()
        self._bind()

    def init(self) -> None:
        self.frame.is_state = self.model.auth.is_state
        self.frame.update_state = self.model.auth.update

    def _bind(self) -> None:
        self.frame.init_boutons()
        self.frame.module2.config(command=self.module2)
        self.frame.init_questions()

    def module2(self) -> None:
        self.view.switch("module2")

