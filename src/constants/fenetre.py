from enum import Enum


PHASE_X = 7 # décalage des fenêtres vers la gauche
PHASE_Y = 20 # height of the windows bar at bottom
DEPHASE_X = 2 # width of the windows border
DEPHASE_Y = 50 # height of the windows border + height of the windows bar at top (title bar)
N_MODULES = 1#12 # nombre de fenêtres


class Titre(Enum):
    MODULE_1 = "Fils"
    MODULE_2 = "Bouton"
    MODULE_3 = "Clavier"
    MODULE_4 = "Simon"

    MODULE_5 = "Jeux de mots"
    MODULE_6 = "Memory"
    MODULE_7 = "Code Morse"
    MODULE_8 = "Fils compliqués"

    MODULE_9 = "Séquences de fils"
    MODULE_10 = "Labyrinthe"
    MODULE_11 = "Mot de passe"
    MODULE_12 = "x"

    def index(self):
        enum_values = [e.value for e in self.__class__]
        return enum_values.index(self.value)

    @classmethod
    def get_value_by_index(cls, search_index: int) -> str | None:
        enum_values = [e.value for e in cls]
        if search_index in range(len(enum_values)):
            return enum_values[search_index]
        return None
