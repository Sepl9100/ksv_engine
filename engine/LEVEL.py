from GLOBAL import *


class Level:
    def __init__(self, host):
        self.host = host
        self.items = []

    def load(self):
        # load every item of the level
        for item in self.items:
            item.load()
        # execute the Levels update method every game tick
        self.host.game_loop_queue[0].append(lambda:
                                            self.update(self.host.mx, self.host.my, self.host.event, self.host.key))

    def update(self, mx, my, event, key):
        pass
