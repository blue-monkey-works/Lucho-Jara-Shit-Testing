import pygame

class luchoJara:
    def __init__(self):
        self._image_surf = None
        self.width = 64
        self.height = 64
        self.selectable = True
        self.movable = False
        self.class = "unit"

    def draw(self):
