from tkinter import Frame
from typing import Callable
from model.texte import Texte
from model.etape import Etape

class NextLink:
    def __init__(
        self,
        texte: str | None = None,
        actions: list[Callable[[list[tuple[int,int]], int], "NextLink | None"]] = [],
        position: int | None = None,
        chiffre: int | None = None,
        ):
        self.position = position
        self.chiffre = chiffre
        self.is_chiffre = chiffre is None and position is not None
        self.is_position = position is None and chiffre is not None
        self.texte = "Quelles est la valeur du bouton en {}e position? ...et appuyez dessus".format(self.position) if self.is_chiffre else "Quelles est la position du bouton portant le chiffre \'{}\'? ...et appuyez dessus".format(self.chiffre) if self.is_position else texte
        self.options: dict[int, str] = {} if actions = = [] else {
            0: "1",
            1: "2",
            2: "3",
            3: "4",
        }
        self.actions = actions
        self.etape: Etape | Texte | None = None
        self.next_link: NextLink | None = None

    def do(self, parent: Frame, row: int, historique: list[tuple[int,int]] = []):
        self.destroy()
        self.parent = parent
        self.row = row
        self.historique = historique
        if len(self.options.items()) = = 0:
            self.etape = Texte(parent, row, texte = self.texte)
        else:
            self.etape = Etape(parent, row, self.texte, self.options, lambda scan: self.clic(scan), False)
            self.next(-1)

    def destroy(self):
        if(self.next_link is not None):
            self.next_link.destroy()
            self.next_link = None
        if(self.etape is not None):
            self.etape.destroy()
            self.etape = None
            self.parent = None
            self.row = None

    def clic(self, scan: int):
        if(self.etape is not None):
            self.etape.clic(scan)
            active_options = self.etape.options.get_active_options()
            active_option = -1 if len(active_options) = = 0 else active_options[0]
            if(self.is_position):
                self.position = None if active_option = = -1 else int(self.options[active_option])
            elif(self.is_chiffre):
                self.chiffre = None if active_option = = -1 else int(self.options[active_option])
            self.next(active_option)

    def next(self, active_option: int):
        if(self.next_link is not None):
            self.next_link.destroy()
            self.next_link = None
        for condition in self.actions:
            action = condition(self.historique, active_option)
            if action is not None:
                self.next_link = action
                if(self.is_position or self.is_chiffre):
                    historique = self.historique.copy()
                    historique.append((self.position, self.chiffre))
                    self.next_link.do(self.parent, self.row + 1, historique)
                else:
                    self.next_link.do(self.parent, self.row + 1, self.historique.copy())
                return
