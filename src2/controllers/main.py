from models.main import Model
from models.auth import Auth
from views.main import View

from .signup import SignUpController
from .signin import SignInController
from .module_1 import Module1Controller
from .module_2 import Module2Controller
from .home import HomeController


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.signup_controller = SignUpController(model, view)
        self.signin_controller = SignInController(model, view)
        self.module1_controller = Module1Controller(model, view)
        self.module2_controller = Module2Controller(model, view)
        self.home_controller = HomeController(model, view)

        self.model.auth.add_event_listener("auth_changed", self.auth_state_listener)

    def auth_state_listener(self, data: Auth) -> None:
        pass

    def start(self) -> None:
        self.view.switch("module1")
        self.view.start_mainloop()
