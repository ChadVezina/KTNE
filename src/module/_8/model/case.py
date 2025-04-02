from .bouton_case import BoutonCase
from .texte import Texte
from ..tools.enums import TypeFil, TypeSolution

class Case:
    def __init__(self, numero):
        self.numero = numero
        self.types = {
            TypeFil.ROUGE: False,
            TypeFil.BLEU: False,
            TypeFil.ETOILE: False,
            TypeFil.LUMIERE_ALLUMEE: False,
        }

    def placer_case(self, parent):
        self.destroy()
        self.label = Texte(parent, self.numero, 0, f"Fil {self.numero + 1}")
        self.solution = Texte(parent, self.numero, 1)
        self.update_solution()
        self.bouton_rouge = BoutonCase(parent, self.numero, 2, "rouge", lambda: self.clic(TypeFil.ROUGE))
        self.bouton_bleu = BoutonCase(parent, self.numero, 3, "bleu", lambda: self.clic(TypeFil.BLEU))
        self.bouton_etoile = BoutonCase(parent, self.numero, 4, "★", lambda: self.clic(TypeFil.ETOILE))
        self.bouton_lumiere_allumee = BoutonCase(parent, self.numero, 5, "lumière allumée", lambda: self.clic(TypeFil.LUMIERE_ALLUMEE))

    def destroy(self):
        self.types = {
            TypeFil.ROUGE: False,
            TypeFil.BLEU: False,
            TypeFil.ETOILE: False,
            TypeFil.LUMIERE_ALLUMEE: False,
        }

    def get_solution(self):
        if self.types[TypeFil.ROUGE]:
            if self.types[TypeFil.LUMIERE_ALLUMEE]:
                if self.types[TypeFil.BLEU]:
                    if self.types[TypeFil.ETOILE]:
                        return TypeSolution.N
                    else:
                        return TypeSolution.S
                else:
                    return TypeSolution.B
            elif self.types[TypeFil.ETOILE]:
                if self.types[TypeFil.BLEU]:
                    return TypeSolution.P
                else:
                    return TypeSolution.C
            else:
                return TypeSolution.S
        elif self.types[TypeFil.LUMIERE_ALLUMEE]:
            if self.types[TypeFil.BLEU]:
                return TypeSolution.P
            elif self.types[TypeFil.ETOILE]:
                return TypeSolution.B
            else:
                return TypeSolution.N
        elif self.types[TypeFil.BLEU]:
            if self.types[TypeFil.ETOILE]:
                return TypeSolution.N
            else:
                return TypeSolution.S
        else:
            return TypeSolution.C

    def update_solution(self):
        self.type_solution = self.get_solution()
        self.solution.set_texte(self.type_solution.str_value)

    def clic(self, type: TypeFil):
        if self.types[type]:
            self.desactiver(type)
        else:
            self.activer(type)
        self.update_solution()

    def activer(self, type: TypeFil):
        match type:
            case TypeFil.ROUGE:
                self.bouton_rouge.activer()
            case TypeFil.BLEU:
                self.bouton_bleu.activer()
            case TypeFil.ETOILE:
                self.bouton_etoile.activer()
            case TypeFil.LUMIERE_ALLUMEE:
                self.bouton_lumiere_allumee.activer()
        self.types[type] = True

    def desactiver(self, type: TypeFil):
        match type:
            case TypeFil.ROUGE:
                self.bouton_rouge.desactiver()
            case TypeFil.BLEU:
                self.bouton_bleu.desactiver()
            case TypeFil.ETOILE:
                self.bouton_etoile.desactiver()
            case TypeFil.LUMIERE_ALLUMEE:
                self.bouton_lumiere_allumee.desactiver()
        self.types[type] = False
