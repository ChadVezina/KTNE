from typing import Optional, TypedDict
from .base import ObservableModel
from designs.memento import Caretaker


class Data(TypedDict):
    module1_couleur: Optional[str]
    module1_texte: Optional[str]


class Auth(ObservableModel):
    def __init__(self):
        super().__init__()
        self.current_memento: Optional[Caretaker] = None

    @property
    def state(self) -> Data:
        return self.current_memento.state if self.current_memento else {}

    def update(self, memento: Data) -> None:
        if self.current_memento is None:
            self.current_memento = Caretaker(memento)
        else:
            state = self.state
            for key, value in memento.items():
                if value is not None:
                    state[key] = value
            self.current_memento.update(state)
        self.trigger_event("auth_changed")

    def clear_fields(self, keys: list[str]) -> None:
        if self.current_memento is None:
            return
        else:
            state = self.state
            for key in keys:
                if key in state.keys():
                    state[key] = None
            self.current_memento.update(state)
        self.trigger_event("auth_changed")

    def clear(self) -> None:
        if self.current_memento is None:
            return
        else:
            self.current_memento.update({})
        self.trigger_event("auth_changed")

    def undo(self) -> None:
        if self.current_memento is not None:
            self.current_memento.undo()
            self.trigger_event("auth_changed")

    def reset(self) -> None:
        self.current_memento = None
        self.trigger_event("auth_changed")

