import pygame
from pygame import Color
from pygame.rect import Rect

from game.grid.Tile import Tile


class Grid:

    width = 800
    height = 600
    tile_size = 64
    tiles = []

    def __init__(self, display_surf):
        self.offset_x = (self.width % self.tile_size) / 2
        self.offset_y = (self.height % self.tile_size) / 2
        self.surface = pygame.Surface((self.width, self.height))
        tiles_x = int(self.width / self.tile_size)
        tiles_y = int(self.height / self.tile_size)
        self.init_grid(tiles_x, tiles_y)
        self.display_surf = display_surf

    def init_grid(self, tiles_x, tiles_y):
        for x in range(tiles_x):
            row = []
            for y in range(tiles_y):
                row.append(Tile(self.tile_size * x, self.tile_size * y, self.surface))
            self.tiles.append(row)

    def draw(self):
        for tile_column in self.tiles:
            for tile in tile_column:
                tile.draw()
        self.display_surf.blit(self.surface, (self.offset_x, self.offset_y))
