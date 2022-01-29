import PIL.Image as Image
import PIL
import pygame as pg
import os
import threading
import webbrowser
import random
from time import sleep

AUTHOR = "Sebastian Reichl"
VERSION = 0.1
GAMENAME = "ENGINE BETA"

pg.init()


APP_ = {
    "FONT_1": pg.font.SysFont('Bahnschrift', 30),
    "FONT_2": pg.font.SysFont('Bahnschrift', 17)
}

COLS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "BUTTON": (255, 0, 0),
    "HOVER": (75, 225, 255),
    "CLICK": (50, 150, 255),
    "CYAN": (0, 255, 255)
}

COLLIDERS = []
ENTITIES = []
SPRITES = []
AIS = []
RENDERLAYERS = []
for i in range(200):
    RENDERLAYERS.append([])

SINGLE_LISTS = [COLLIDERS, ENTITIES, SPRITES, AIS]


def clear_lists():
    print("\nclearing lists")
    for layer in RENDERLAYERS:
        for sprite in layer:
            del sprite
        layer.clear()
    for list in SINGLE_LISTS:
        for item in list:
            del item
        list.clear()
