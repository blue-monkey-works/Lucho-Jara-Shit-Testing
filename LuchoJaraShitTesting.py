import pygame
from Unit import *
from pygame.locals import *


class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
        # constructor

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.LuchoJaraUnit = Unit("LuchoJaraHeroSprite.png",self._display_surf)
        self.LuchoJaraUnit.draw(64, 64)
        self._running = True
        # init stage

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        #elif event.type == pygame.MOUSEMOTION:
        #    self.LuchoJaraUnit.draw()
        # read data input on event stage

    def on_loop(self):
        pass
        # refactor data on loop stage

    def on_render(self):

        pygame.display.flip()
        # redraw screen output on render stage

    def on_cleanup(self):
        pygame.quit()
        quit()
        # data cleanup and backup here

    def on_execute(self):
        self.on_init()
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        # on_execute starts and recalls all loop functions


if __name__ == "__main__":
    LuchoJaraShitTesting = App()
    LuchoJaraShitTesting.on_execute()
