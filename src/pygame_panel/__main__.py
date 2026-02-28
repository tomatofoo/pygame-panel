import time
import pygame as pg

from panel import Surface
from panel import Label
from panel import Button
from panel import Toggle
from panel import Input
from panel import Panel


pg.init()
SCREEN_SIZE = (640, 480)
SCREEN_FLAGS = pg.RESIZABLE | pg.SCALED
VSYNC = 0
FONTS = {
    'main': pg.font.SysFont('Arial', 16),
    'title': pg.font.SysFont('Arial', 16),
}
FONTS['title'].underline = 1

screen = pg.display.set_mode(SCREEN_SIZE, SCREEN_FLAGS, vsync=VSYNC)


running = 1
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = 0

    pg.display.flip()

pg.quit()

