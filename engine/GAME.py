from GLOBAL import *
from engine.WINDOW import *
from gamedata.level.main_menu import *


class Game:
    def __init__(self):
        self.TPS = 30
        self.FPS = 60
        self.GAME_CLOCK = pg.time.Clock()
        self.DRAW_CLOCK = pg.time.Clock()
        self.game_loop_running = True
        self.draw_loop_running = True
        self.game_queue = [[], [], []]
        self.game_loop_queue = [[], [], [], [], [], [], [], [], [], []]
        self.mx, self.my = pg.mouse.get_pos()
        self.event = pg.event.poll()
        self.key = pg.key.get_pressed()

        self.window = Window(self)

        # ---------

        self.load_level(MainMenu(self))

        # ---------

        self.game_thread = threading.Thread(target=self.game_loop)
        self.game_thread.start()
        self.draw_loop()

    def draw_loop(self):
        print("\nstarting draw loop")
        while self.draw_loop_running:
            self.mx, self.my = pg.mouse.get_pos()  # get and handle user inputs
            self.event = pg.event.poll()
            self.key = pg.key.get_pressed()

            if self.event.type == pg.QUIT:
                self.game_loop_running = False
            if not self.game_loop_running:
                self.draw_loop_running = False
                pg.quit()
                exit()

            self.DRAW_CLOCK.tick(self.FPS)
            self.window.screen.fill(COLS["BLACK"])
            self.window.update()

    def game_loop(self):
        print("\nstarting game loop")
        ticks = 0
        while self.game_loop_running:
            self.GAME_CLOCK.tick(self.TPS)

            # Execute the game loop queue in 2**i ticks. i = 0-9
            for i in range(10):
                if ticks % (2**i) == 0:
                    for action in self.game_loop_queue[i]:
                        action()

            # Execute the game queue
            for action in self.game_queue[0]:   # All actions in index[0]
                action()
            self.game_queue[0] = []

            try:
                self.game_queue[1][0]()         # One action after another in index[1]
                self.game_queue[1].pop(0)
            except IndexError:
                pass

            if ticks % 10:
                try:
                    self.game_queue[2][0]()     # One action after another in index[2] every 10 ticks
                    self.game_queue[2].pop(0)
                except IndexError:
                    pass

            ticks += 1

    def load_level(self, level):
        self.unload()
        self.level = level
        self.level.load()

    def unload(self):
        self.game_queue = [[], [], []]
        self.game_loop_queue = [[], [], [], [], [], [], [], [], [], []]
        clear_lists()
