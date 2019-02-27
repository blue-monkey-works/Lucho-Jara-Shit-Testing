import pygame
from pygame.rect import Rect


class Tile:

    size = 64

    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.grid_color = (50, 50, 50)
        self.rect = Rect(x, y, self.size, self.size)
        self.surface = surface

    def contains(self, x, y):
        return x in range(self.x) and y in range(self.y)

    def getTile(self):
        return self

    def draw(self):
        pygame.draw.rect(self.surface, self.grid_color, self.rect, 1)
