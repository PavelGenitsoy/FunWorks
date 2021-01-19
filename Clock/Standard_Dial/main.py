import pygame as pg
from datetime import datetime
from random import randint
from math import cos, sin, radians, pi

pg.init()
size = Width, Height = 1200, 800
screen = pg.display.set_mode(size)

Initial_Values = C_Width, C_Height = Width // 2, Height // 2
Radius = 380
Time_Dict = {'pointer': Radius - 27, 'hour': Radius - 150, 'minute': Radius - 70, 'second': Radius - 90}

FPS = 30
black, red, green, blue, white = [0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]  # rgb [0..255]
random_color = [randint(0, 255) for _ in range(3)]


def get_position(clock_hour, segment_time, time_key):
    x = C_Width + Time_Dict[time_key] * cos(radians(clock_hour[segment_time]) - pi / 2)
    y = C_Height + Time_Dict[time_key] * sin(radians(clock_hour[segment_time]) - pi / 2)
    return int(x), int(y)


def product_function():
    pg.display.set_caption("My CLOCK")
    clock = pg.time.Clock()

    clock_min_and_sec = dict(zip(range(60), range(0, 360, 6)))

    font_add_info = pg.font.SysFont('serif', 25)
    digit_list = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

    img_background = pg.image.load('images/updatedboard_background.png')
    img_circle_background = pg.image.load('images/circle_background.jpg')

    circle_background_rect = img_circle_background.get_rect()
    circle_background_rect.center = size
    dx, dy = 1, 1

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        # for dynamic background
        dx *= -1 if circle_background_rect.left > 0 or circle_background_rect.right < Width else 1
        dy *= -1 if circle_background_rect.top > 0 or circle_background_rect.bottom < Height else 1
        circle_background_rect.centerx += dx
        circle_background_rect.centery += dy

        screen.blit(img_circle_background, circle_background_rect)
        screen.blit(img_background, (0, 0))

        time_now = datetime.now()
        indicator_h = ((time_now.hour % 12) * 5 + time_now.minute // 12) % 60
        indicator_m, indicator_s = time_now.minute, time_now.second

        iterator = 0
        for i in clock_min_and_sec.keys():
            if not i % 5:
                radius_ = 20
                text_info = font_add_info.render(digit_list[iterator], True, pg.Color('snow'))
                iterator += 1
                rect = text_info.get_rect(center=get_position(clock_min_and_sec, i, 'pointer'))
                screen.blit(text_info, rect)
                pg.draw.circle(screen, pg.Color('red'), get_position(clock_min_and_sec, i, 'pointer'), radius_, 5)
            else:
                radius_ = 3
                pg.draw.circle(screen, pg.Color('black'), get_position(clock_min_and_sec, i, 'pointer'), radius_, 3)

        pg.draw.line(screen, pg.Color('blue'), Initial_Values, get_position(clock_min_and_sec, indicator_h, 'hour'), 15)
        pg.draw.line(screen, pg.Color('magenta'), Initial_Values,
                     get_position(clock_min_and_sec, indicator_m, 'minute'), 10)
        pg.draw.line(screen, pg.Color('lawngreen'), Initial_Values, get_position(clock_min_and_sec, indicator_s,
                                                                                 'second'), 5)

        # after drawing everything, flip the screen
        pg.display.flip()

        # cycle speed
        clock.tick(FPS)


product_function()
