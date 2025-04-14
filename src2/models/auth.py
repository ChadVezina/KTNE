from typing import Optional, TypedDict, TypeVar, get_type_hints
from .base import ObservableModel
from designs.memento import Caretaker


T = TypeVar("T")


class Data(TypedDict):
    module1_couleur: Optional[str]
    module1_texte: Optional[str]

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
            return {
                "module1_couleur": None,
                "module1_texte": None
            }
        return self.current_memento.state

    def is_state(self, key: str, value: T) -> bool:
        return self.state.get(key, None) == value

    def update(self, memento: Data) -> None:
        state = self.state
        for key in memento.keys():
            state[key] = memento[key]
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

