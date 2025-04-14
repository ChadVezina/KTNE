from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypeVar
from copy import copy
#from inspect import getsource


T = TypeVar("T")


@dataclass
class Data:
    _state: T

    @property
    def state(self) -> T:
        return self._state

    def copy(self) -> T:
        return copy(self._state)

    @staticmethod
    def build(state: T) -> Data:
        return Data(_state = state)


class Memento(ABC):
    @abstractmethod
    def get_data(self) -> Data:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class Originator:
    def __init__(self, state: T) -> None:
        self._data = Data.build(state)
        print(f"Originator: Etat actuel: {self._data.state}")

    @property
    def data(self) -> Data:
        return self._data

    @data.setter
    def data(self, state: T) -> None:
        self._data = Data.build(state)
        print(f"Originator: Etat actuel devient: {self._data.state}")

    def save(self) -> Memento:
        return ConcreteMemento(self._data)

    def restore(self, memento: Memento) -> None:
        self._data = memento.get_data()
        print(f"Originator: Etat actuel etait: {self._data.state}")


class ConcreteMemento(Memento):
    def __init__(self, data: Data) -> None:
        self._data = data
        self._date = str(datetime.now())[:19]

    def get_data(self) -> Data:
        return self._data

    def get_name(self) -> str:
        return f"{self._date} / ({self._data.state.__str__()})"


class Caretaker:
    def __init__(self, state: T) -> None:
        self._mementos: list[Memento] = []
        self._originator = Originator(state)

    @property
    def state(self) -> T:
        return self._originator.data.state

    def copy(self) -> T:
        return self._originator.data.copy()

    def update(self, new_state: T) -> None:
        self.backup()
        self._originator.data = new_state

    def backup(self) -> None:
        print("\nCaretaker: Sauvegarde en cours...")
        self._mementos.append(self._originator.save())

    def undo(self) -> bool:
        if not len(self._mementos):
            return False
        self.afficher_historique()
        memento = self._mementos.pop()
        print(f"\nCaretaker: Charger: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            return self.undo()
        return True

    def afficher_historique(self) -> None:
        print("\nCaretaker: Historique:")
        for memento in self._mementos:
            print(memento.get_name())

if __name__ == "__main__":
    #test = (["s", 45, 3.5], {"a": 1, "b": 2})
    test0 = {"s": 234, "a": "gdsg"}
    test = [0, None, 324, "dfgdfg", 4.5, False, test0]
    caretaker = Caretaker(test)
    state:list = caretaker.copy()
    state[0] = None
    state.append("test")
    #state = (None, state[1])
    print(state)
    now = caretaker.state
    print(now)

