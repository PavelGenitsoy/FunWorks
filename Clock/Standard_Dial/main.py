from func import product_function
import pygame as pg

pg.init()
size = Width, Height = 1200, 800
screen = pg.display.set_mode(size)

Initial_Values = C_Width, C_Height = Width // 2, Height // 2
FPS = 30

product_function(Initial_Values, FPS, size, screen)
