import pygame

class Unit:
    def __init__(self, sprImg, displaysurface):
        self.surface = pygame.Surface((64,64))
        self.sprite = pygame.image.load(sprImg)
        self.x = 64
        self.y = 64
        self.display_surf = displaysurface
        self.spriteRect = self.sprite.get_rect();
        self.selectable = True
        self.movable = False
        self.type = ["unit"]
    def draw(self, x, y):
        self.display_surf.blit(self.sprite,(x,y))


