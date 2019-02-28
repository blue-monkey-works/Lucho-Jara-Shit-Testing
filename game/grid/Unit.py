import pygame
from game.grid.Tile import Tile
import pytweening as tween

class Unit:
    def __init__(self, sprImg, displaysurface,rootgrid):
        self.rootGrid = rootgrid
        self.surface = pygame.Surface((64,64))
        self.sprite = pygame.image.load(sprImg)
        self.speed = 8
        self.path = []
        self.x = 64
        self.y = 64
        self.display_surf = displaysurface
        self.spriteRect = self.sprite.get_rect();
        self.selectable = True
        self.movable = False
        self.type = ["unit"]

    def draw(self, x, y):
        self.display_surf.blit(self.sprite,(x,y))
        self.setSpritePos(x,y)

    def setSpritePos(self, x,y):
        self.spritex = x
        self.spritey = y

    def getTilePos(self):
        actualTile = self.rootGrid.get_tile(self.x,self.y)
        return (actualTile.x,actualTile.y)

    def getPos(self):
        return (self.x,self.y)

    def setPathToPoint(self,x,y):
        self.path = tween.getLine(self.x,self.y,x,y)
        return self.path