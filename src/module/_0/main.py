"""
Ce fichier présente une ébauche d'interface pour le TP4. Vous pouvez le modifier à souhait.
"""
from tkinter import Tk, Frame, Button, messagebox, Toplevel, CENTER

from .model.case import Case
from .model.tableau import Tableau
from .model.bouton_case import BoutonCase
from .tools.fonctions import make_label, make_label_entry, make_menu, validate_entry, validate_entry_mines
from .tools.constantes import FenetrePad, Font


class Module_0(Tk):
    def __init__(self):
        """
        Constructeur de la classe Module_0.
        Crée tous les boutons existants dans l'interface, dont ceux qui
        correspondent à des cases
        """
        super().__init__()

        # Nom de la fenêtre.
        self.title("Démineur")
        self.resizable(True, True)

        self.dimension_rangee = 5
        self.dimension_colonne = 5
        self.nombre_mines = 5

        make_menu(self, self.nouvelle_partie, self.configurer, self.charger, self.sauvegarder, self.quitter)

        self.cadre = Frame(self)
        self.cadre.grid(padx=FenetrePad.PADDING_X, pady=FenetrePad.PADDING_Y)
        self.cadre.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.ouvrir_partie()

    def ouvrir_partie(self, dictionnaire_cases=None, activer_jeu=True):
        """
        Redémarre le tableau avec de nouveaux emplacements de mines
        """
        for bouton in self.cadre.winfo_children():
            bouton.destroy()
        self.dictionnaire_boutons = {}
        for i in range(self.dimension_rangee):
            for j in range(self.dimension_colonne):
                bouton = BoutonCase(self.cadre, i + 1, j + 1)
                bouton.grid(row=i, column=j)
                self.dictionnaire_boutons[(i + 1, j + 1)] = bouton
        self.tableau_mines = Tableau(self.dimension_rangee, self.dimension_colonne, self.nombre_mines)
        if dictionnaire_cases is not None:
            self.tableau_mines.dictionnaire_cases = dictionnaire_cases
            for case in self.tableau_mines.dictionnaire_cases.values():
                if case.est_devoilee:
                    self.tableau_mines.nombre_cases_sans_mine_a_devoiler -= 1
        if activer_jeu:
            self.activer_jeu()
        else:
            self.desactiver_jeu()
        self.redessiner()

    def redessiner(self):
        """
        Affiche l'apparence de tous les boutons en fonction de si ils
        ont été dévoilés. Cette méthode doit être appelée chaque fois que l'état
        du jeu a été modifié.
        """
        for i in range(1, self.tableau_mines.dimension_rangee + 1):
            for j in range(1, self.tableau_mines.dimension_colonne + 1):
                case = self.tableau_mines.obtenir_case(i, j)
                self.dictionnaire_boutons[(i, j)]['text'] = case.obtenir_apparence()

    def activer_jeu(self):
        """
        Rend tous les boutons de case cliquables.
        """
        for bouton in self.dictionnaire_boutons.values():
            bouton.activer(self.devoiler_case)

    def desactiver_jeu(self):
        """
        Rend tous les boutons de case non-cliquables.
        """
        for bouton in self.dictionnaire_boutons.values():
            bouton.desactiver()

    def devoiler_case(self, event):
        """
        Déclenche un dévoilement en cascade à partir de la case cliquée

        Args:
            event (Tkinter.event): L'événement de clic, qui contient le bouton cliqué
                en attribut
        """
        bouton = event.widget
        rangee_x, colonne_y = bouton.rangee_x, bouton.colonne_y
        self.tableau_mines.devoilement_en_cascade(rangee_x, colonne_y)
        self.detecter_fin(rangee_x, colonne_y)
        self.redessiner()
        bouton.desactiver()

    def detecter_fin(self, rangee_x, colonne_y):
        """
        Détecte la fin de la partie. Si la partie est terminée,
        un message indiquant s'il s'agit d'une victoire ou d'une défaite est affiché,
        puis les cases sont toutes révélées, et le jeu est désactivé.

        Note: vous pouvez vous inspirer de la classe Partie du TP3 pour savoir
        comment détecter la fin de la partie

        Args:
            rangee_x (int): Numéro de la rangée
            colonne_y (int): Numéro de la colonne
        """
        if self.tableau_mines.obtenir_case(rangee_x, colonne_y).est_minee or not self.tableau_mines.contient_cases_a_devoiler():
            message = "Défaite..."
            if not self.tableau_mines.contient_cases_a_devoiler():
                message = "Victoire!"
            fenetre = Toplevel(self)
            fenetre.title("La partie est terminée")
            make_label(fenetre, message, 0)
            self.tableau_mines.tout_devoiler()
            self.desactiver_jeu()


    def nouvelle_partie(self):
        """
        Ouvre une partie en utilisant la méthode ouvrir_partie avec les arguments par défaut.
        """
        self.ouvrir_partie()

    def configurer(self):
        self.fenetre_configuration = Toplevel(self)
        self.fenetre_configuration.title("Configuration")

        self.input_nombre_lignes = make_label_entry(self.fenetre_configuration, "Nombre de lignes", 0)
        self.input_nombre_colonnes = make_label_entry(self.fenetre_configuration, "Nombre de colonnes", 1)
        self.input_nombre_mines = make_label_entry(self.fenetre_configuration, "Nombre de mines", 2)

        bouton_ok = Button(self.fenetre_configuration, font=Font.BODY, text="Lancer la nouvelle partie",
                           command=self.lancer_partie_configuree)
        bouton_ok.grid(row=3, column=0)

    def lancer_partie_configuree(self):
        try:
            dimension_rangee = validate_entry(self.input_nombre_lignes.get(), "Nombre de lignes")
            dimension_colonne = validate_entry(self.input_nombre_colonnes.get(), "Nombre de colonnes")
            nombre_mines = validate_entry(self.input_nombre_mines.get(), "Nombre de mines")

            validate_entry_mines(dimension_rangee, dimension_colonne, nombre_mines)

            self.dimension_rangee = dimension_rangee
            self.dimension_colonne = dimension_colonne
            self.nombre_mines = nombre_mines

            self.ouvrir_partie()
            self.fenetre_configuration.destroy()
        except ValueError as e:
            messagebox.showerror("Erreur de valeur", str(e))
        except TypeError as e:
            messagebox.showerror("Erreur de type", str(e))

    def sauvegarder(self):
        """
        Sauvegarde la partie en cours dans un fichier texte nommé 'sauvegarde.txt'.
        Se référer à la méthode charger pour connaître le format attendu.
        """
        f = open("sauvegarde.txt", "w")
        for x in range(1, self.dimension_rangee+1):
            for y in range(1, self.dimension_colonne + 1):
                case = self.tableau_mines.dictionnaire_cases[(x, y)]
                est_devoilee = "o" if case.est_devoilee else "n"
                est_minee = "M" if case.est_minee else str(case.nombre_mines_voisines)
                f.write(est_devoilee + est_minee)
                f.write(" ")
            f.write("\n")
        f.close()

    def charger(self):
        """
        Charge une partie sauvegardée. Celle-ci doit être stockée dans un fichier nommé
        'sauvegarde.txt' et doit correspondre au format suivant:

        Dans ce fichier, chaque case doit être représentée par deux caractères,
            - un 'o' si la case est dévoilée, un 'n' sinon
            - un 'M' si la case est minée, sinon un entier de 0 à 8
            représentant le nombre de mines voisines

        Les cases d'une même rangée sont séparées par un espace,
        celles sur des rangées différentes par un retour de ligne.

        Exemple (partie 5x5 où l'on a cliqué aux coordonnées 1,3):
        nM o1 o0 o1 n1
        n2 o2 o1 o2 nM
        nM n2 n1 nM n2
        nM n2 n1 n1 n1
        n1 n1 n0 n0 n0
        """
        f = open("sauvegarde.txt", "r")
        x, y_max, n_mines = 0, 1, 0
        dictionnaire_cases = {}
        jeu_en_cours = False
        for ligne in f.readlines():
            x += 1
            y = 0
            rangee = ligne.rstrip().split(" ")
            for str_case in rangee:
                y += 1
                y_max = max(y, y_max)
                case = Case()
                if str_case[0] == "o":
                    case.devoiler()
                else:
                    jeu_en_cours = True
                if str_case[1] == "M":
                    case.ajouter_mine()
                    n_mines += 1
                else:
                    mines_voisines = int(str_case[1])
                    for i in range(mines_voisines):
                        case.ajouter_une_mine_voisine()
                dictionnaire_cases[(x, y)] = case
        f.close()
        self.dimension_rangee = x
        self.dimension_colonne = y_max
        self.nombre_mines = n_mines
        self.ouvrir_partie(dictionnaire_cases, jeu_en_cours)

    def quitter(self):
        """
        Affiche un message de confirmation, et dans l'affirmative,
        quitte l'interface.

        Vous aurez besoin de messagebox.askyesno et de self.quit.
        """
        if messagebox.askyesno("Quitter", "Êtes-vous sûr de vouloir quitter?"):
            self.quit()
