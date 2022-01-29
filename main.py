from GLOBAL import *
from engine.GAME import *
import cProfile

c_profile = True


class App:
    def __init__(self):
        self.game = Game()


if c_profile:
    cProfile.run("App()")
else:
    App()
pg.quit()
