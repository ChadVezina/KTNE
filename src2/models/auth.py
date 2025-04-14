from typing import Optional, TypedDict, TypeVar, get_type_hints
from .base import ObservableModel
from designs.memento import Caretaker


T = TypeVar("T")


class Data(TypedDict):
    module1_module2_couleur: Optional[str]
    module1_module2_texte: Optional[str]

    @staticmethod
    def keys():
        return get_type_hints(Data).keys()


class Auth(ObservableModel):
    def __init__(self):
        super().__init__()
        self.current_memento: Optional[Caretaker] = None

    @property
    def state(self) -> Data:
        if self.current_memento is None:
            state: Data = {}
            for key in Data.keys():
                state[key] = None
            return state
        return self.current_memento.state

    def get_key(self, name: str, key_module: str) -> str | None:
        keys = filter(lambda x: x.__contains__(name), Data.keys())
        for key in keys:
            if key.__contains__(key_module):
                return key
        return None

    def is_state(self, name: str, key_module: str, value: T) -> bool:
        key = self.get_key(name, key_module)
        if key:
            return self.state.get(key, None) == value
        else:
            return False

    def update(self, name: str, key_module: str, value: T) -> None:
        state = self.state
        key = self.get_key(name, key_module)
        if key:
            state[key] = value
        else:
            return
        if self.current_memento is None:
            self.current_memento = Caretaker(state)
        else:
            self.current_memento.update(state)
        self.trigger_event("auth_changed")

    def clear(self, name: str) -> None:
        state = self.state
        for key in Data.keys():
            if key.__contains__(name):
                state[key] = None
        if self.current_memento is None:
            self.current_memento = Caretaker(state)
        else:
            self.current_memento.update(state)
        self.trigger_event("auth_changed")

    def undo(self) -> None:
        if self.current_memento is not None:
            self.current_memento.undo()
            self.trigger_event("auth_changed")

    def reset(self) -> None:
        self.current_memento = None
        self.trigger_event("auth_changed")

