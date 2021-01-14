import numeric_integration as ni
import matplotlib.pyplot as plt
import helper as hlp
import pygame as pg
import planet
import game_loop
import theta_manager as tm

hlp.t_list, data_list = ni.rk4(0, 800, 1e-2)
theta_list_earth, r_list_earth = tm.to_theta_r_list(data_list, 1)
theta_list_mars, r_list_mars = tm.to_theta_r_list(data_list, 2)
print(theta_list_earth)

print('Time Period T of Earth', tm.get_t(theta_list_earth))
print('Time Period T of Mars', tm.get_t(theta_list_mars))

pg.init()
pg.display.set_caption('SolarSystem')
hlp.init()
planet.Planet(hlp.circle_surface(50, hlp.RED), ni.to_loc_list(data_list, 0))
planet.Planet(hlp.circle_surface(20, hlp.BLUE), ni.to_loc_list(data_list, 1))
planet.Planet(hlp.circle_surface(20, hlp.RED), ni.to_loc_list(data_list, 2))
game_loop.game_loop()
