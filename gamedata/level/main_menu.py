from GLOBAL import *
from engine.ENTITY import *
from engine.BUTTON import *


class MainMenu:
    def __init__(self, host):
        print("initialising MainMenu")
        self.host = host
        self.items = []

        # Test Objects
        self.test_sprite = Entity(0, 0, 100, 100, self.host.window, 0)
        self.test_sprite.sprite.fill_color(COLS["CYAN"])
        self.items.append(self.test_sprite)

        self.test_button = Button(200, 200, 200, 70, "Test", self.host.window, lambda: print("button click"))
        self.items.append(self.test_button)

    def load(self):
        for item in self.items:
            item.load()
        self.host.game_loop_queue[0].append(lambda: self.update(self.host.mx, self.host.my))

    def update(self, mx, my):
        self.test_sprite.move(2, 2)
        self.test_button.draw_button(mx, my)
