import numeric_integration as ni
import matplotlib.pyplot as plt
import helper as hlp
import pygame as pg
import planet
import game_loop
import conservation_checker as cc
import theta_manager as tm

hlp.t_list, data_list = ni.rk4(0, 800, 1e-2)

'''
plt.figure(1)
energy_list = cc.to_energy_list(data_list)
plt.plot(hlp.t_list, energy_list, label='Total Energy')
plt.title('Conservation of Energy')
plt.xlabel('time [day]')
plt.ylabel('energy [kg * AU^2 / s^2]')
plt.ylim(top=0)
plt.legend()
plt.show()
print("Change in Energy", max(energy_list) - min(energy_list))
print('In Percentage', abs((max(energy_list) - min(energy_list))/(sum(energy_list)/hlp.t_num)) * 100)


plt.figure(2)
momentum_list = cc.to_momentum_list(data_list)
plt.plot(hlp.t_list, list(map(lambda k: k[0], momentum_list)), label='Total x Momentum')
plt.plot(hlp.t_list, list(map(lambda k: k[1], momentum_list)), label='Total y Momentum')
plt.title('Conservation of Momentum')
plt.xlabel('time [day]')
plt.ylabel('momentum [kg * AU / s]')
plt.ylim(top=0)
plt.legend()
plt.show()
print("Change in x Momentum", max(list(map(lambda k: k[0], momentum_list))) - min(list(map(lambda k: k[0], momentum_list))))
print("In Percentage", abs((max(list(map(lambda k: k[0], momentum_list))) - min(list(map(lambda k: k[0], momentum_list)))) /
      (sum(list(map(lambda k: k[0], momentum_list)))/hlp.t_num)) * 100)
print("Change in y Momentum", max(list(map(lambda k: k[1], momentum_list))) - min(list(map(lambda k: k[1], momentum_list))))
print("In Percentage", abs((max(list(map(lambda k: k[1], momentum_list))) - min(list(map(lambda k: k[1], momentum_list)))) /
      (sum(list(map(lambda k: k[1], momentum_list)))/hlp.t_num)) * 100)

plt.figure(3)
angular_momentum_list = cc.to_angular_momentum_list(data_list)
plt.plot(hlp.t_list, angular_momentum_list, label='Total Angular Momentum')
plt.title('Conservation of Angular Momentum')
plt.xlabel('time [day]')
plt.ylabel('angular momentum [kg * AU^2 / s]')
plt.ylim(top=0)
plt.legend()
plt.show()
print("Change in Angular Momentum", max(angular_momentum_list) - min(angular_momentum_list))
print('In Percentage', abs((max(angular_momentum_list) - min(angular_momentum_list))/(sum(angular_momentum_list)/hlp.t_num)) * 100)
'''


pg.init()
pg.display.set_caption('SolarSystem')
hlp.init()
planet.Planet(hlp.circle_surface(50, hlp.RED), ni.to_loc_list(data_list, 0))
planet.Planet(hlp.circle_surface(20, hlp.BLUE), ni.to_loc_list(data_list, 1))
planet.Planet(hlp.circle_surface(20, hlp.RED), ni.to_loc_list(data_list, 2))
planet.Planet(hlp.circle_surface(100, hlp.BLACK), ni.to_loc_list(data_list, 3))
game_loop.game_loop()
