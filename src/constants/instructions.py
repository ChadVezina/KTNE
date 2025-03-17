from enum import Enum
from .fenetre import Titre as TitreFenetre

class Titre(Enum):
    MODULE_1 = f"À propos des {TitreFenetre.MODULE_1.value}"
    MODULE_2 = f"À propos du {TitreFenetre.MODULE_2.value}"
    MODULE_3 = f"À propos du {TitreFenetre.MODULE_3.value}"
    MODULE_4 = f"À propos du {TitreFenetre.MODULE_4.value}"
    
    MODULE_5 = f"À propos de {TitreFenetre.MODULE_5.value}"
    MODULE_6 = f"À propos du {TitreFenetre.MODULE_6.value}"
    MODULE_7 = f"À propos du {TitreFenetre.MODULE_7.value}"
    MODULE_8 = f"À propos des {TitreFenetre.MODULE_8.value}"
    
    MODULE_9 = f"À propos des {TitreFenetre.MODULE_9.value}"
    MODULE_10 = f"À propos du {TitreFenetre.MODULE_10.value}"
    MODULE_11 = f"À propos du {TitreFenetre.MODULE_11.value}"
    MODULE_12 = f"À propos de {TitreFenetre.MODULE_12.value}"


N_FENETRES = len(Titre)


class Contenu(Enum):
    MODULE_1 = """Les fils sont comme le sang de l'électronique ! Non... L'électricité est le sang.
    Les fils sont plus comme les artères. Les veines ? Peu importe.

    - Un module de fils peut contenir entre 3 et 6 fils.
    - Seul un fil a besoin d'être coupé pour désamorcer le module.
    - Les fils sont ordonnés de haut en bas.
    """
    MODULE_2 = """On pourrait penser qu'appuyer sur un bouton est assez simple.
    C'est en pensant de cette façon que des bombes explosent.

    - Se référer à l'Annexe A pour identifier les indicateurs.
    - Se référer à l'Annexe B pour identifier les piles.
    """
    MODULE_3 = """Je ne sais pas ce que sont ces symboles, mais je soupçonne quelques sorcelleries.

    - Seulement l'une de ces colonnes contient les 4 symboles présents sur le clavier.
    - Appuyer sur les 4 boutons dans leur ordre d'apparition dans cette colonne de haut en bas.
    """
    MODULE_4 = """Les modules peuvent être identifiés par leur petite lumière en haut à droite.
    Lorsque cette lumière est verte, le module est désarmé.

    - 1 des 4 boutons s'allumera.
    - En utilisant la table, appuyer sur le bouton correspondant.
    - Le bouton original s'allumera suivi d'un autre. Répéter la séquence dans l'ordre en utilisant la correspondance des couleurs.
    - La séquence s'allongera d'une couleur à chaque fois que la bonne séquence sera entrée, jusqu'à ce que le module soit désarmé.
    """
    MODULE_5 = """ """
    MODULE_6 = """ """
    MODULE_7 = """ """
    MODULE_8 = """ """
    MODULE_9 = """ """
    MODULE_10 = """ """
    MODULE_11 = """ """
    MODULE_12 = """ Annexe """

