from GLOBAL import *
from engine.COLLIDER import *
from engine.SPRITE import *


class Entity:
    def __init__(self, x, y, width, height, host, layer=10):
        self.x = x
        self.y = y
        self.host = host
        self.layer = layer

        self.sprite = Sprite(self.x, self.y, width, height, host, "ENTITIY_SPRITE1", layer)
        self.rect = self.sprite.rect

        self.collision = False

    def load(self):
        self.sprite.load()
        ENTITIES.append(self)

    def give_collision(self):
        self.collision = True
        self.rect = self.sprite.rect
        self.collider = Collider(self.rect)

    def remove_collision(self):
        self.collision = False
        try:
            COLLIDERS.remove(self.collider)
            del self.collider
        except:
            pass

    def move(self, xadd, yadd):
        if not self.collision:
            self.sprite.x += xadd
            self.sprite.y += yadd
        else:
            self.collider.rect.x += xadd
            self.collider.rect.y += yadd
            if not self.collider.collide_test():
                self.collider.rect.x -= xadd
                self.collider.rect.y -= yadd
                return False
            else:
                self.sprite.x += xadd
                self.sprite.y += yadd
        self.x = self.sprite.x
        self.y = self.sprite.y
        return True

    def place(self, xdest, ydest):
        if not self.collision:
            self.sprite.x = xdest
            self.sprite.y = ydest
        else:
            oldx = self.collider.rect.x
            oldy = self.collider.rect.y

            self.collider.rect.x = xdest
            self.collider.rect.y = ydest

            if not self.collider.collide_test():
                self.collider.rect.x = oldx
                self.collider.rect.y = oldy
            else:
                self.sprite.x = xdest
                self.sprite.y = ydest