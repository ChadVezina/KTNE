from typing import Callable, Optional, TypeAlias, TypedDict, get_type_hints
from .base import ObservableModel
from designs.memento import Caretaker


Comparaison: TypeAlias = tuple[int, Callable[[int], bool]]


class Data(TypedDict):
    module1_module2_couleur: Optional[str]
    module1_module2_texte: Optional[str]
    module1_module2_n_piles: Optional[Comparaison]

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
            split = key.split("_module")
            end = split[split.__len__() - 1]
            end = end[end.index("_") + 1:]
            if end == key_module:
                return key
        return None

    def get_value(self, key: str, value: str) -> str | int | float | Comparaison | None:
        if key.startswith("n_"):
            match value:
                case "plus qu'une":
                    return 2, lambda x: x > 1
                case "plus que 2":
                    return 3, lambda x: x > 2
                case _:
                    try:
                        return int(value)
                    except ValueError:
                        try:
                            return float(value)
                        except ValueError:
                            return None
        else:
            return value

    def is_state(self, name: str, key_module: str, value_module: str) -> bool:
        key = self.get_key(name, key_module)
        if key:
            value = self.get_value(key, value_module)
            if value is Comparaison:
                old_value = self.state.get(key, (0, lambda x: False))
                return old_value[1](value[0])
            return self.state.get(key, None) == value
        else:
            return False

    def update(self, name: str, key_module: str, value_module: str) -> None:
        state = self.state
        key = self.get_key(name, key_module)
        if key:
            value = self.get_value(key, value_module)
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

