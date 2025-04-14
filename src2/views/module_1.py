from tkinter import Frame
from typing import Any, Callable
from models.auth import Data
from designs.composite import Composite, Leaf
from designs.abstract_factory import ConcreteFactory1


class Module1View(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.is_state: Callable[[str, Any], bool] = lambda key, value: False
        self.update_state: Callable[[Data], None] = lambda state: None
        self.init_boutons()
        self.init_questions()

    def init(self) -> None:
        self.tree.init_actions()
        self.tree.show(0)

    def init_boutons(self, row: int = 0):
        self.root_boutons = Frame(self)
        self.root_boutons.grid(row=row)

        factory = ConcreteFactory1()
        self.module2 = factory.create_bouton(self.root_boutons, 0, 0, "Module 2")
        #self.module1 = factory.create_bouton(self.root_boutons, 0, 1, "Module 1")

    def init_questions(self, row: int = 1):
        self.root_questions = Frame(self)
        self.root_questions.grid(row=row)

        self.tree = self.question_1()

    def is_active(self, key: str) -> Callable[[str], bool]:
        return lambda value: self.is_state(key, value)

    def get_action(self, key: str) -> Callable[[str | None], None]:
        return lambda val, key=key: self.update_state({key: val})

    def choix_args(self, key: str):
        return self.is_active(key), self.get_action(key)

    def question_1(self) -> Composite:
        branch = Composite(1, "1) Bouton est ...?", self.root_questions)

        branch.add_choix("bleu", *self.choix_args("module1_couleur"))
        branch.add_choix("\"Annuler\"", *self.choix_args("module1_texte"))

        branch.add_action(self.derniere_question(), lambda x: x.is_active(0) and x.is_active(1))
        branch.add_action(self.question_2(), lambda x: not x.is_active(1))
        branch.add_action(self.question_3())

        return branch

    def question_2(self) -> Composite:
        branch = Composite(2, "2) Combien de piles? Bouton est ...?", self.root_questions)

        branch.add_choix("plus qu'une")
        branch.add_choix("\"Exploser\"", *self.choix_args("module1_texte")) # question 1-1

        branch.add_action(self.conclusion(), lambda x: x.is_active(0) and x.is_active(1))
        branch.add_action(self.question_3(), lambda x: x.parent_numero_is_active(1, 0))
        branch.add_action(self.question_4())

        return branch

    def question_3(self) -> Composite:
        branch = Composite(3, "3) Bouton est ...? Indicateur est ...?", self.root_questions)

        branch.add_choix("blanc", *self.choix_args("module1_couleur")) # question 1-0
        branch.add_choix("allumé avec \"CAR\"")

        branch.add_action(self.derniere_question(), lambda x: x.is_active(0) and x.is_active(1))
        branch.add_action(self.question_4(), lambda x: x.parent_numero_is_active(2, 0, True))
        branch.add_action(self.question_5())

        return branch

    def question_4(self) -> Composite:
        branch = Composite(4, "4) Combien de piles? Indicateur est ...?", self.root_questions)

        branch.add_choix("plus que 2") # question 2-0
        branch.add_choix("allumé avec \"FRK\"")

        branch.add_action(self.conclusion(), lambda x: x.is_active(0) and x.is_active(1))
        branch.add_action(self.question_5(), lambda x: x.parent_numero_is_active(1, 0) and x.parent_numero_is_active(3, 0))
        branch.add_action(self.derniere_question())

        return branch

    def question_5(self) -> Composite:
        branch = Composite(5, "5) Bouton est ...?", self.root_questions)

        branch.add_choix("rouge", *self.choix_args("module1_couleur")) # question 3-0 et 1-0

        branch.add_action(self.conclusion(), lambda x: x.is_active(0))
        branch.add_action(self.derniere_question())

        return branch

    def derniere_question(self) -> Composite:
        branch = Composite(6, "6) Maintenir le bouton appuyé et...\nDe quelle couleur est la bande qui vient de s'allumer à droite?", self.root_questions, False)

        branch.add_choix("bleu")
        branch.add_choix("blanc")
        branch.add_choix("jaune")

        branch.add_action(self.conclusion(4), lambda x: x.is_active(0))
        branch.add_action(self.conclusion(5), lambda x: x.is_active(2))
        branch.add_action(self.conclusion(1))

        return branch

    def conclusion(self, chiffre: int = -1) -> Leaf:
        if chiffre == -1:
            return Leaf("Appuyer et immédiatement relâcher le bouton", self.root_questions)
        else:
            return Leaf(f"Relâcher le bouton quand le minuteur affiche un {chiffre} dans n'importe quelle position", self.root_questions)

