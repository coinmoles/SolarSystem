import helper as hlp
import pygame as pg
import sys


def game_loop():

    while hlp.t < hlp.t_num:
        hlp.screen.fill(hlp.BLACK)

        for planet in hlp.planet_list:
            planet.act()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()

        hlp.t += 50
        hlp.clock.tick(30)
