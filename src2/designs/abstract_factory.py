from __future__ import annotations
from abc import ABC, abstractmethod
from tkinter import Frame
from typing import Callable, Literal
from unittest import result

from pyrsistent import b;
from constants.config import Font
from products.bouton import Bouton


class AbstractFactory(ABC):
    @abstractmethod
    def create_bouton(
            self,
            parent: Frame,
            row: int = 0,
            col: int = 0,
            texte: str = "",
            commande: Callable[[], None] = None,
            font = Font.BODY,
            relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = "raised",
            border: str | float = None,
            wraplength: str | float = None,
            no_margin: bool = False,
            no_padding: bool = False,
            no_color: bool = False,
        ) -> Bouton:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_bouton(
            self,
            parent: Frame,
            row: int = 0,
            col: int = 0,
            texte: str = "",
            commande: Callable[[], None] = None,
            font = Font.BODY,
            relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = "raised",
            border: str | float = None,
            wraplength: str | float = None,
            no_margin: bool = False,
            no_padding: bool = False,
            no_color: bool = False,
        ) -> ConcreteBouton1:
        return ConcreteBouton1(parent, row, col, texte, commande, font, relief, border, wraplength, no_margin, no_padding, no_color)

    def test(self, parent, row: int = 0, col: int = 0) -> None:
        bouton = self.create_bouton(parent, row, col, "Bouton 1")
        result = bouton.get_texte()
        print(f"{result}")


class ConcreteFactory2(AbstractFactory):
    def create_bouton(
            self,
            parent: Frame,
            row: int = 0,
            col: int = 0,
            texte: str = "",
            commande: Callable[[], None] = None,
            font = Font.BODY,
            relief: Literal["raised", "sunken", "flat", "ridge", "solid", "groove"] = "raised",
            border: str | float = None,
            wraplength: str | float = None,
            no_margin: bool = False,
            no_padding: bool = False,
            no_color: bool = False,
        ) -> ConcreteBouton2:
        return ConcreteBouton2(parent, row, col, texte, commande, font, relief, border, wraplength, no_margin, no_padding, no_color)

    def test(self, parent, row: int = 0, col: int = 0) -> None:
        bouton = self.create_bouton(parent, row, col)
        bouton.set_texte("Bouton 2")
        result = bouton.cget("text")
        print(f"{result}")


class ConcreteBouton1(Bouton):
    def get_texte(self) -> str:
        return self.cget("text")


class ConcreteBouton2(Bouton):
    def set_texte(self, texte: str) -> None:
        self["text"] = texte


def client_code(factory: AbstractFactory, parent: Frame, row: int = 0, col: int = 0) -> None:
    if isinstance(factory, ConcreteFactory1):
        factory.test(parent, row, col)
    elif isinstance(factory, ConcreteFactory2):
        factory.test(parent, row, col)
