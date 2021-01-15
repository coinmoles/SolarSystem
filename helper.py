import pygame as pg
import pandas as pd
import vector as vec

BLACK = (0, 0, 0)
RED = (255, 0, 0)
MARS = (150, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

data = pd.read_excel('./SolarSystem.xlsx')
G = 1.48802e-34  # TODO: 값 대입 (AU, day 단위로 맞추려면 어떻게 해야하지 아몰랑)
n = len(data)
planets = data['name']
m_list = data['m']
start_values = pd.DataFrame(
    {'loc': list(map(lambda k: vec.Vector(k[0], k[1]), zip(data['x'], data['y']))),
     'vel': list(map(lambda k: vec.Vector(k[0], k[1]), zip(data['vx'], data['vy'])))}
)

t = 0
t_num = 0
screen = None
clock = None
planet_list = []

PADWIDTH, PADHEIGHT = 1200, 800


def init():
    global screen, clock
    screen = pg.display.set_mode((PADWIDTH, PADHEIGHT))
    clock = pg.time.Clock()


def circle_surface(radius, color):  # 동그라미 surface
    radius = int(radius)
    my_circle = pg.Surface((radius * 2, radius * 2), flags=pg.SRCALPHA)
    pg.draw.circle(my_circle, color, (radius, radius), radius, 0)
    return my_circle
