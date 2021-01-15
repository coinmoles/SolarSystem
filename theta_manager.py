import vector as vec
import math
import helper as hlp


def to_theta_r_list(td_data, p_num):
    theta_list = list(map(lambda td: math.atan2(*(td.loc[p_num, 'loc'] - td.loc[0, 'loc'])), td_data))
    r_list = list(map(lambda td: abs(td.loc[p_num, 'loc'] - td.loc[0, 'loc']), td_data))
    return theta_list, r_list


def get_t(theta_list):
    theta_0 = theta_list[0]

    i = 40
    while abs(theta_list[i] - theta_0) > 0.0005:
        i += 1

    return hlp.t_list[i]
