from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypeVar


T = TypeVar("T")


class Memento(ABC):
    @abstractmethod
    def get_state(self) -> T:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class Originator:
    def __init__(self, state: T) -> None:
        self._state = state
        print(f"Originator: Etat actuel: {self._state}")

    @property
    def state(self) -> T:
        return self._state

    @state.setter
    def state(self, state: T) -> None:
        self._state = state
        print(f"Originator: Etat actuel devient: {self._state}")

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: Etat actuel était: {self._state}")


class ConcreteMemento(Memento):
    def __init__(self, state: T) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> T:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state.__str__()[0:9]}...)"


class Caretaker:
    def __init__(self, state: T) -> None:
        self._mementos: list[Memento] = []
        self._originator = Originator(state)

    @property
    def state(self) -> T:
        return self._originator.state

    def update(self, new_state: T) -> None:
        self.backup()
        self._originator.state = new_state

    def backup(self) -> None:
        print("\nCaretaker: Sauvegarde en cours...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return
        self.afficher_historique()
        memento = self._mementos.pop()
        print(f"\nCaretaker: Charger: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def afficher_historique(self) -> None:
        print("\nCaretaker: Historique:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    caretaker = Caretaker("a")
    caretaker.update(3)
    caretaker.update("c")
    caretaker.update("d")
    caretaker.undo()
    caretaker.undo()

