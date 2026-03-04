#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUI du jeu Casse-Briques basé sur la classe backend CasseBriques
"""

import tkinter as tk


class CasseBriquesGUI(tk.Tk):
    """
    Interface graphique pour le jeu Casse-Briques.

    Attributes:
        casse_briques (CasseBriques): Instance backend contenant la logique du jeu.
        largeur_canevas (int): Largeur de la fenêtre du jeu.
        hauteur_canevas (int): Hauteur de la fenêtre du jeu.
        vx (int): Vitesse horizontale de la balle.
        vy (int): Vitesse verticale de la balle.
        canvas (tk.Canvas): Canevas sur lequel les éléments du jeu sont dessinés.
        raquette (int): ID Tkinter de la raquette.
        balle (int): ID Tkinter de la balle.
        score_text (int): ID Tkinter du texte affichant le score.
    """

    def __init__(self, casse_briques):
        """
        Initialise l'interface graphique et crée les widgets du jeu.

        Args:
            casse_briques (CasseBriques): Instance du backend CasseBriques.
        """
        super().__init__()
        self.casse_briques = casse_briques
        self.geometry("800x600")
        self.title("Casse-Briques")
        self.largeur_canevas = 800
        self.hauteur_canevas = 600
        self.vx = 3
        self.vy = -3

        self.creer_widgets()

        self.derniere_brique = None

    def creer_widgets(self):
        """
        Crée le canevas, dessine les briques, la raquette, la balle et le texte du score.
        Associe le déplacement de la raquette aux touches gauche/droite.
        """
        self.canvas = tk.Canvas(
            self, width=self.largeur_canevas, height=self.hauteur_canevas, bg="white"
        )
        self.canvas.pack()

        # Dessiner les briques
        for brique in self.casse_briques.briques:
            self.dessiner_brique(brique)

        # Créer la raquette
        self.raquette = self.canvas.create_rectangle(350, 550, 450, 570, fill="gray")

        # Créer la balle
        self.balle = self.canvas.create_oval(390, 530, 410, 550, fill="black")

        # Déplacement raquette
        self.bind("<KeyPress>", self.deplacer_raquette)

        # Texte du score (en bas, sous la raquette)
        self.score_text = self.canvas.create_text(
            self.largeur_canevas // 2,
            self.hauteur_canevas - 15,
            text=f"Score : {self.casse_briques.score}",
            fill="black",
            font=("Arial", 14),
        )

    def dessiner_brique(self, brique):
        """
        Dessine une brique sur le canevas et enregistre son ID Tkinter.

        Args:
            brique (Brique): Objet brique à dessiner.
        """
        x0, y0, x1, y1 = brique.get_limits()
        brique.canvas_id = self.canvas.create_rectangle(
            x0, y0, x1, y1, fill=brique.couleur, outline="black"
        )

    def deplacer_raquette(self, event):
        """
        Déplace la raquette horizontalement selon la touche pressée.

        Args:
            event (tk.Event): Événement de pression de touche (gauche/droite).
        """
        dx = 0
        if event.keysym == "Left":
            dx = -20
        elif event.keysym == "Right":
            dx = 20
        self.canvas.move(self.raquette, dx, 0)

    def animer_balle(self):
        """
        Anime la balle en déplaçant son oval sur le canevas, gère :
        - les rebonds sur les murs et la raquette,
        - la détection de collision avec les briques via le backend,
        - la mise à jour du score et la suppression graphique des briques détruites.

        Cette méthode se rappelle automatiquement toutes les 30 ms.
        """

        self.canvas.move(self.balle, self.vx, self.vy)
        coords = self.canvas.coords(self.balle)

        if len(coords) != 4:
            return

        x0, y0, x1, y1 = coords

        # Rebond sur murs
        if x0 <= 0 or x1 >= self.largeur_canevas:
            self.vx = -self.vx
        if y0 <= 0 or y1 >= self.largeur_canevas:
            self.vy = -self.vy

        # Rebond sur raquette
        raq_coords = self.canvas.coords(self.raquette)
        if (
            x1 >= raq_coords[0]
            and x0 <= raq_coords[2]
            and y1 >= raq_coords[1]
            and y1 <= raq_coords[3]
        ):
            self.vy = -self.vy

        # Demande s'il y a collision
        ball_centre_x = (x0 + x1) / 2
        ball_centre_y = (y0 + y1) / 2
        briques_avant = list(self.casse_briques.briques)

        brique_touchee = self.casse_briques.impact_brique(ball_centre_x, ball_centre_y)

        # Si une brique est touchée
        if brique_touchee is not None:
            # Si ce n’est pas la même brique que lors de l'itération précédente
            if brique_touchee is not self.derniere_brique_touchee:
                self.vy = -self.vy
                self.derniere_brique_touchee = brique_touchee
        else:
            self.derniere_brique_touchee = None

        self.canvas.itemconfig(
            self.score_text, text=f"Score : {self.casse_briques.score}"
        )

        # Mise à jour graphique
        for brique in briques_avant:
            if brique not in self.casse_briques.briques:
                self.canvas.delete(brique.canvas_id)

        self.after(30, self.animer_balle)

    def demarrer(self):
        """
        Démarre la boucle principale Tkinter et lance l’animation de la balle.
        """
        self.animer_balle()
        self.mainloop()
