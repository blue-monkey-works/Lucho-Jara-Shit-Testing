from game.grid.Unit import *

from game.grid.Grid import Grid


class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.units = []
        self.size = self.weight, self.height = 800, 600
        # constructor

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.grid = Grid(self._display_surf)
        self.LuchoJaraUnit = Unit("LuchoJaraHeroSprite.png", self._display_surf, self.grid)
        self.units.append(self.LuchoJaraUnit)
        self.LuchoJaraUnit.draw(64-32, 64-32)
        self._running = True

        # init stage

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.button)
                if event.button == 3:
                    mousePos = pygame.mouse.get_pos()
                    self.LuchoJaraUnit.setPathToPoint(mousePos[0],mousePos[1])


    def on_loop(self):
        if self.LuchoJaraUnit.path:
            LuchoJaraStep = self.LuchoJaraUnit.path[0]
            self.LuchoJaraUnit.x = LuchoJaraStep[0]
            self.LuchoJaraUnit.y = LuchoJaraStep[1]
            self.LuchoJaraUnit.path.pop(0)
        # refactor data on loop stage


    def on_render(self):
        self.grid.draw()
        if self.units:

            if self.LuchoJaraUnit.path:
                pygame.draw.line(self._display_surf,(255,0,0), self.LuchoJaraUnit.getPos(), self.LuchoJaraUnit.path[-1])
            self.LuchoJaraUnit.draw(self.LuchoJaraUnit.x - 32, self.LuchoJaraUnit.y - 32)
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
