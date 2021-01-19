import pygame as pg
from datetime import datetime
from random import randint
from math import cos, sin, radians, pi

Width, Height = 1200, 800

Initial_Values = C_Width, C_Height = Width // 2, Height // 2
Radius = 380
Time_Dict = {'hour': Radius - 150, 'minute': Radius - 60, 'second': Radius - 90}

FPS = 30
black, red, green, blue, white = [0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]  # rgb [0..255]
random_color = [randint(0, 255) for _ in range(3)]


def get_position(clock_hour, segment_time, time_key):
    x = C_Width + Time_Dict[time_key] * cos(radians(clock_hour[segment_time]) - pi / 2)
    y = C_Height + Time_Dict[time_key] * sin(radians(clock_hour[segment_time]) - pi / 2)
    return x, y


def product_function(width, height, fps, rand_col):
    background_colour, font_text_info_colour = rand_col
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("My CLOCK")
    clock = pg.time.Clock()

    clock_hour = dict(zip(range(12), range(0, 360, 30)))
    clock_min_and_sec = dict(zip(range(60), range(0, 360, 6)))

    # font_ = pg.font.SysFont('Comic Sans MS', 200)

    # surf = pg.Surface((720, 35))
    # surf.fill('white')
    # font_add_info = pg.font.SysFont('serif', 30)
    # text_info = font_add_info.render("You can also use this buttons: LEFT, RIGHT, UP, DOWN", True,
    #                                  font_text_info_colour)
    # place_for_text_info = pg.Rect(230, 20, 500, 100)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        time_now = datetime.now()
        indicator_h, indicator_m, indicator_s = time_now.hour % 12, time_now.minute, time_now.second

        # t_render = font_.render(f'{time_now:%H:%M:%S}', True, [randint(0, 255) for _ in range(3)], pg.Color('orange'))

        # place = t_render.get_rect(center=(width / 2, height / 2))
        #
        # pressed = pg.key.get_pressed()
        # if pressed[pg.K_LEFT]:
        #     place.x -= 150
        # elif pressed[pg.K_RIGHT]:
        #     place.x += 150
        # elif pressed[pg.K_UP]:
        #     place.y -= 150
        # elif pressed[pg.K_DOWN]:
        #     place.y += 150

        # rendering
        screen.fill(background_colour)
        # surf.blit(text_info, pg.Rect(10, 0, 0, 0))
        # screen.blit(surf, place_for_text_info)
        # screen.blit(t_render, place)

        pg.draw.circle(screen, pg.Color('yellow'), Initial_Values, Radius)
        pg.draw.line(screen, pg.Color('blue'), Initial_Values, get_position(clock_hour, indicator_h, 'hour'), 15)
        pg.draw.line(screen, pg.Color('magenta'), Initial_Values,
                     get_position(clock_min_and_sec, indicator_m, 'minute'), 10)
        pg.draw.line(screen, pg.Color('black'), Initial_Values, get_position(clock_min_and_sec, indicator_s, 'second'),
                     5)

        # after drawing everything, flip the screen
        pg.display.flip()

        # cycle speed
        clock.tick(fps)


ans = input(
    "What color of background would you like? (black, red, green, blue, white), if you don't care about the "
    "color, then enter 'r': ")
if ans == "black":
    product_function(Width, Height, FPS, (black, black))
# elif ans == "red":
#     product_function(Width, Height, FPS, (red, black))
# elif ans == "green":
#     product_function(Width, Height, FPS, (green, black))
# elif ans == "white":
#     product_function(Width, Height, FPS, (white, black))
# elif ans == "blue":
#     product_function(Width, Height, FPS, (blue, black))
elif ans == "r":
    product_function(Width, Height, FPS, (random_color, black))
