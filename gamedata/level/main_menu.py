from GLOBAL import *
from engine.LEVEL import *
from engine.ENTITY import *
from engine.BUTTON import *


class MainMenu(Level):
    def __init__(self, host):
        super().__init__(host)

        self.test_sprite = Entity(0, 0, 100, 100, self.host.window, 0)
        self.test_sprite.sprite.fill_color(COLS["CYAN"])
        self.items.append(self.test_sprite)

        self.test_button = Button(200, 200, 200, 70, "Test", self.host.window, lambda: print("button click"))
        self.items.append(self.test_button)

    def update(self, mx, my, event, key):
        self.test_sprite.move(2, 2)
        self.test_button.draw_button(mx, my)
