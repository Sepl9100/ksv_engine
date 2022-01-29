from GLOBAL import *
from engine.TEXT_BOX import *


class Window:
    def __init__(self, game):
        self.window = self
        self.game = game
        self.xoff = 0
        self.yoff = 0
        self.width = 1000
        self.height = 500
        self.flags = pg.DOUBLEBUF | pg.HWSURFACE
        self.screen = pg.display.set_mode((self.width, self.height), self.flags, 32)
        self.intro = TextBox(0, 0, "Powered by the KSV Engine", self, APP_["FONT_1"], COLS["WHITE"])
        self.intro.sprite.x = self.width//2 - self.intro.sprite.width // 2
        self.intro.sprite.y = self.height//2 - self.intro.sprite.height // 2
        self.intro.sprite.draw()
        self.update()
        sleep(0.1)
        self.intro.remove()
        self.update()

    def update(self):
        for layer in RENDERLAYERS:
            for sprite in layer:
                sprite.draw()
        pg.display.set_caption(f"FPS: {round(self.game.DRAW_CLOCK.get_fps(), 1)} - {GAMENAME} {VERSION} by {AUTHOR}")
        pg.display.flip()

