import numeric_integration as ni
import matplotlib.pyplot as plt
import helper as hlp
import pygame as pg
import planet
import game_loop
import conservation_checker as cc
import theta_manager as tm

hlp.t_list, data_list = ni.rk4(0, 800, 1, False)

'''
theta_list, r_list = tm.to_theta_r_list(data_list, 1)
theta_list_true, r_list_true = tm.to_theta_r_list(data_list_true, 1)

plt.figure(1)
plt.plot(hlp.t_list, tm.get_percent_differece(r_list, r_list_true), label='% error of r(t) of Earth')
plt.title('% Error')
plt.xlabel('time [day]')
plt.ylabel('error [%]')
plt.legend()
plt.show()

plt.figure(2)
plt.plot(hlp.t_list, tm.get_percent_differece(theta_list, theta_list_true), label='% error of theta(t) of Earth')
plt.title('% Error')
plt.xlabel('time [day]')
plt.ylabel('error [%]')
plt.legend()
plt.show()

theta_list, r_list = tm.to_theta_r_list(data_list, 2)
theta_list_true, r_list_true = tm.to_theta_r_list(data_list_true, 2)

plt.figure(3)
plt.plot(hlp.t_list, tm.get_percent_differece(r_list, r_list_true), label='% error of r(t) of Mars')
plt.title('% Error')
plt.xlabel('time [day]')
plt.ylabel('error [%]')
plt.legend()
plt.show()

plt.figure(4)
plt.plot(hlp.t_list, tm.get_percent_differece(theta_list, theta_list_true), label='% error of theta(t) of Mars')
plt.title('% Error')
plt.xlabel('time [day]')
plt.ylabel('error [%]')
plt.legend()
plt.show()
'''
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
planet.Planet(hlp.circle_surface(30, hlp.RED), ni.to_loc_list(data_list, 0))
planet.Planet(hlp.circle_surface(10, (52, 66, 119)), ni.to_loc_list(data_list, 1))
planet.Planet(hlp.circle_surface(10, (226, 123, 88)), ni.to_loc_list(data_list, 2))
planet.Planet(hlp.circle_surface(8, (213, 210, 209)), ni.to_loc_list(data_list, 3))
planet.Planet(hlp.circle_surface(8, (139, 125, 130)), ni.to_loc_list(data_list, 4))
planet.Planet(hlp.circle_surface(10, (200, 139, 58)), ni.to_loc_list(data_list, 5))
planet.Planet(hlp.circle_surface(10, (164, 155, 114)), ni.to_loc_list(data_list, 6))
planet.Planet(hlp.circle_surface(8, (79, 208, 231)), ni.to_loc_list(data_list, 7))
planet.Planet(hlp.circle_surface(8, (37, 128, 159)), ni.to_loc_list(data_list, 8))
planet.Planet(hlp.circle_surface(3, (0, 0, 0)), ni.to_loc_list(data_list, 9))
planet.Planet(hlp.circle_surface(2, (100, 100, 100)), ni.to_loc_list(data_list, 10))
planet.Planet(hlp.circle_surface(2, (0, 0, 0)), ni.to_loc_list(data_list, 11))

game_loop.game_loop()
