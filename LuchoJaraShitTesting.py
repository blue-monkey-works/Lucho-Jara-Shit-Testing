import pygame
from pygame.locals import *




class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
        #constructor

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        #init stage

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        #read data input on event stage

    def on_loop(self):
        pass
        # refactor data on loop stage

    def on_render(self):
        pass
        # redraw screen output on render stage

    def on_cleanup(self):
        pygame.quit()
        # data cleanup and backup here

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        #on_execute starts and recalls all loop functions


if __name__ == "__main__":
    LuchoJaraShitTesting = App();
    LuchoJaraShitTesting.on_execute();
