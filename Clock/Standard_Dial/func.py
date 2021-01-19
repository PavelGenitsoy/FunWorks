import pygame as pg
from datetime import datetime
from random import randint
from math import cos, sin, radians, pi


Radius = 380
Time_Dict = {'pointer': Radius - 27, 'hour': Radius - 150, 'minute': Radius - 70, 'second': Radius - 90}


def get_position(tuple_size, clock_, segment_time, time_key):
    """

    :param tuple_size: Width // 2, Height // 2 , its a center of a window
    :param clock_: dictionary for minutes and seconds
    :param segment_time: specific unit of time
    :param time_key: key with which we can identify radius of hands on the clock
    :return: int(x), int(y)    (coordinates of new point)

    >>> get_position((600, 400),{0 : 0, 1 : 6, 2 : 12},0,'second')
    (600, 110)

    """
    x = tuple_size[0] + Time_Dict[time_key] * cos(radians(clock_[segment_time]) - pi / 2)
    y = tuple_size[1] + Time_Dict[time_key] * sin(radians(clock_[segment_time]) - pi / 2)
    return int(x), int(y)


def product_function(tuple_size, fps, size, screen):
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
        dx *= -1 if circle_background_rect.left > 0 or circle_background_rect.right < size[0] else 1
        dy *= -1 if circle_background_rect.top > 0 or circle_background_rect.bottom < size[1] else 1
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
                rect = text_info.get_rect(center=get_position(tuple_size, clock_min_and_sec, i, 'pointer'))
                screen.blit(text_info, rect)
                pg.draw.circle(screen, pg.Color('red'), get_position(tuple_size, clock_min_and_sec, i, 'pointer'),
                               radius_, 5)
            else:
                radius_ = 3
                pg.draw.circle(screen, pg.Color('black'), get_position(tuple_size, clock_min_and_sec, i, 'pointer'),
                               radius_, 3)

        pg.draw.line(screen, pg.Color('blue'), tuple_size,
                     get_position(tuple_size, clock_min_and_sec, indicator_h, 'hour'), 15)
        pg.draw.line(screen, pg.Color('magenta'), tuple_size,
                     get_position(tuple_size, clock_min_and_sec, indicator_m, 'minute'), 10)
        pg.draw.line(screen, pg.Color('lawngreen'), tuple_size,
                     get_position(tuple_size, clock_min_and_sec, indicator_s, 'second'), 5)

        # after drawing everything, flip the screen
        pg.display.flip()

        # cycle speed
        clock.tick(fps)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
