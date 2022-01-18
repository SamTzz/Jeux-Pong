import pygame
from pygame import Vector2




class Joueur:
    def __init__(self):

        self.couleur = (255, 255, 255)
        self.dimension = 15, 120
        self.position = Vector2(0, 400)
        self.direction = Vector2()

    def deplacement(self, z, s):

        if z and self.position.y > 0:
            self.direction = Vector2(self.direction.x, -2)
        if s and self.position.y < 785:
            self.direction = Vector2(self.direction.x, 2)

        self.position = self.position + self.direction
        self.direction = Vector2(0, 0)


    def afficher(self, screen):

        pygame.draw.rect(screen, self.couleur, (self.position, self.dimension), 0, 10)
