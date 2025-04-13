from __future__ import annotations
from abc import ABC, abstractmethod
from tkinter import Frame
from typing import List, Callable

from products.root import Root
from products.bouton import Bouton
from products.texte import Texte


class Component(ABC):
    def __init__(self, texte: str) -> None:
        self._texte = texte
        self._parent: Composite | None = None

    @property
    def texte(self) -> str:
        return self._texte

    @texte.setter
    def texte(self, texte: str) -> None:
        self._texte = texte

    @property
    def parent(self) -> Composite | None:
        return self._parent

    @parent.setter
    def parent(self, parent: Composite | None) -> None:
        self._parent = parent

    def parent_numero_is_active(self, numero: int, scan: int, pas: bool = False) -> bool:
        parent = self._parent
        for _ in range(self.n_parents()+1):
            if parent is not None:
                if parent.numero == numero:
                    if pas:
                        return parent.is_active(scan)
                    else:
                        return not parent.is_active(scan)
                parent = parent.parent
        return True

    def n_parents(self) -> int:
        count = 0
        parent = self._parent
        while parent is not None:
            count += 1
            parent = parent.parent
        return count

    @abstractmethod
    def show(self, row: int) -> None:
        pass

    @abstractmethod
    def hide(self) -> None:
        pass


class Leaf(Component):
    def __init__(self, texte, parent: Frame) -> None:
        super().__init__(texte)
        self._widget = Texte(parent, texte=texte, visible=False)

    def show(self, row: int = -1) -> None:
        self._widget.place(row)

    def hide(self) -> None:
        self._widget.hide()


class Composite(Component):
    def __init__(self, numero: int, texte, parent: Frame, multiple: bool = True) -> None:
        super().__init__(texte)
        self._numero = numero
        self._multiple = multiple
        self._actives: List[bool] = []
        self._children_choix: List[str] = []
        self._children_action: List[tuple[Component, Callable[[Component], bool] | None]] = []
        self._boutons: List[Bouton] = []
        self._widget = Root(parent, visible=False)
        self._label = Texte(self._widget, row=0, texte=texte)
        self._options = Root(self._widget, 1)

    @property
    def numero(self) -> int:
        return self._numero

    def show(self, row: int = -1) -> None:
        for component, _ in self._children_action:
            component.hide()
        self._widget.place(row)
        self.clic(-1)

    def hide(self) -> None:
        for component, _ in self._children_action:
            component.hide()
        self._widget.hide()

    def add_choix(self, choix: str, active_action: Callable[[str], bool] | bool = False, action_model: Callable[[str | None], None] | None = None) -> None:
        if isinstance(active_action, bool):
            active = active_action
        else:
            active = active_action(choix)
        self._actives.append(active)
        self._children_choix.append(choix)
        col = len(self._children_choix) - 1
        bouton = Bouton(self._options, 0, col, choix)
        if active:
            bouton.config(bg="pink")
        self._boutons.append(bouton)
        self._boutons[col].add_command(lambda col=col, action=action_model: self.clic(col, action))

    def add_action(self, component: Component, action: Callable[[Composite], bool] | None = None) -> None:
        self._children_action.append((component, action))
        component.parent = self

    def get_actives(self) -> List[int]:
        return [scan for scan, x in enumerate(self._actives) if x]

    def is_active(self, scan: int) -> bool:
        return self._actives[scan]

    def set_active(self, scan: int) -> None:
        active = not self.is_active(scan)
        self._actives[scan] = active
        bouton = self._boutons[scan]
        if bouton is None:
            return
        if active:
            bouton.config(bg="pink")
        else:
            bouton.config(bg="white")

    def clic(self, i: int = -1, action_model: Callable[[str | None], None] | None = None) -> None:
        if i != -1:
            if not self._multiple:
                for scan in self.get_actives():
                    if scan != i:
                        self.set_active(scan)
            self.set_active(i)
            if action_model is not None:
                if self.is_active(i):
                    action_model(self._children_choix[i])
                else:
                    action_model(None)
        for component, _ in self._children_action:
            component.hide()
        for component, action in self._children_action:
            if action is None or action(self):
                component.show(self.n_parents()+1)
                return

