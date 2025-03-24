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
    MODULE_5 = """Si vous avez du mal à désamorcer ce module, et bien... Je ne peux pas vous aider !

    - Lire l'écran et utiliser l'étape 1 pour déterminer quel libellé de bouton lire.
    - En utilisant le libellé de ce bouton, se référer à l'étape 2 pour savoir sur quel bouton appuyer.
    - Recommencer jusqu'à ce que le module soit désarmé.
    """
    MODULE_6 = """La mémoire est une chose fragile, mais bon tout l'est quand une bombe explose, alors faites attention!

    - Appuyer sur la bonne touche pour aller à la prochaine étape. Compléter toutes les étapes pour désarmer le module.
    - Appuyer sur un bouton incorrect vous fera revenir à l'étape 1.
    - Les boutons sont ordonnés de gauche à droite.
    """
    MODULE_7 = """Je sais que vous êtes en train de vous dire: "Sérieux ? Du code Morse ? Et puis quoi encore?"
    Mais au moins, c'est le vrai code Morse, donc concentrez-vous et vous apprendrez peut-être quelque chose.

    - Interpréter le signal de la lumière clignotante en utilisant la table de décodage du code Morse pour épeler un mot du tableau sur la droite.
    - Le signal se répètera, avec une longue pause entre les répétitions.
    - Lorsque le mot a été identifié, régler la fréquence correspondante et appuyer sur le bouton de transmission (TX).
    """
    MODULE_8 = """Ces fils ne sont pas comme les autres. Ils peuvent avoir deux couleurs !
    Cela les rend complètement différents. La bonne nouvelle, c'est que vous avez à votre disposition
    des instructions très précises ! Peut-être trop précises...

    - Regarder chaque fil: il y a une lumière au-dessus et de l'espace pour le symbole "★" sous le fil.
    - Pour chaque combinaison de fil/lumière/symbole, utiliser le diagramme de Venn pour savoir s'il faut couper le fil ou non.
    - Chaque fil peut être rayé de multiples couleurs.
    """
    MODULE_9 = """C'est difficile d'expliquer comment ça fonctionne. C'est ingénieux, mais il y avait
    sûrement un moyen plus simple de gérer neuf fils.

    - Sur ce module, il y a plusieurs panneaux contenant des fils mais seulement l'un d'eux est visible à la fois. Passer au panneau suivant précédent avec la flèche du haut.
    - Couper tous les fils du panneau qui doivent être coupés, avant de passer au suivant.
    - Couper les fils comme décrit sur la table ci-dessous. Le nombre d'apparitions de fils est cumulatif sur tous les panneaux du module.
    """
    MODULE_10 = """On dirait une sorte de labyrinthe... Probablement plagié sur la nappe d'une table de restaurant.

    - Trouver le labyrinthe auquel les repères circulaires correspondent.
    - Le désamorceur doit amener le point blanc jusqu'au triangle rouge en utilisant les boutons en forme de flèche.
    - Attention: Ne pas traverser les lignes visibles dans les labyrinthes. Ces lignes sont invisibles sur la bombe.
    """
    MODULE_11 = """Heureusement que ces mots de passe ne suivent pas les normes gouvernementales:
    22 caractères, majuscules et minuscules, nombres aléatoires et pas de palindromes de 3 caractères ou plus.

    - Les boutons au-dessus et en dessous d'une position permettent de passer en revue les différentes lettres possibles pour cette position.
    - Seule une combinaison des lettres disponibles correspond à un mot de la liste en dessous.
    - Appuyer sur le bouton "Valider" lorsque les lettres forment un mot correct.
    """
    MODULE_12 = """ Annexe """

