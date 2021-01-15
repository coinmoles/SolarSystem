import helper as hlp
import pygame as pg
import sys


def game_loop():
    k = True
    while k:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                k = False

    while hlp.t < hlp.t_num:
        hlp.screen.fill(hlp.WHITE)

        my_font = pg.font.Font(None, 50)
        text = my_font.render("t: %.2f day" % hlp.t_list[hlp.t], False, hlp.BLACK)
        hlp.screen.blit(text, (0, 0))

        for planet in hlp.planet_list:
            planet.act()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()

        hlp.t += 10
        hlp.clock.tick(30)
