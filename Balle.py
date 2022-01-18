import pygame
from pygame import Vector2
import core

class Balle:
    def __init__(self):
        self.rayon = 12
        self.couleur = (255, 255, 0)
        self.position = Vector2(400, 800)

        self.gravity = 10
        self.direction = Vector2(self.direction.x, (self.direction.y + self.gravity))
        self.position = self.position + self.direction

        if self.position.y > 0:
            self.gravity = self.gravity * -1

        if self.position.y < core.WINDOW_SIZE[1]:
            self.gravity = self.gravity * -1

    def afficher (self, screen):

        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)