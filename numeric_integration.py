import numpy as np
import pandas as pd
import vector as vec
import helper as hlp


def f_vel(df_prev: pd.DataFrame, t: float) -> pd.DataFrame:
    return df_prev['vel']


def f_acc(df_prev: pd.DataFrame, t: float, part3=False) -> pd.DataFrame:
    df_acc = pd.Series([vec.Vector(0, 0) for _ in range(hlp.n)])

    for i in range(hlp.n):
        if part3:
            if i == 0:
                for j in range(hlp.n):
                    if i == j:
                        continue
                    r = abs(df_prev.loc[i, 'loc'] - df_prev.loc[j, 'loc'])
                    df_acc[i] += (df_prev.loc[i, 'loc'] - df_prev.loc[j, 'loc']) * (-hlp.G * hlp.m_list[j] / r ** 3)
            else:
                j = 0
                r = abs(df_prev.loc[i, 'loc'] - df_prev.loc[j, 'loc'])
                df_acc[i] += (df_prev.loc[i, 'loc'] - df_prev.loc[j, 'loc']) * (-hlp.G * hlp.m_list[j] / r ** 3)
        else:
            for j in range(hlp.n):
                if i == j:
                    continue
                r = abs(df_prev.loc[i, 'loc'] - df_prev.loc[j, 'loc'])
                df_acc[i] += (df_prev.loc[i, 'loc'] - df_prev.loc[j, 'loc']) * (-hlp.G * hlp.m_list[j] / r ** 3)

    return df_acc


def forward_euler(t0, tf, dt, part3=False):
    t_num = int((tf - t0) / dt)
    hlp.t_num = t_num
    t_list: list[float] = [0 for _ in range(t_num)]
    data_list: list[pd.DataFrame] = [None for _ in range(t_num)]

    t_list[0] = t0
    data_list[0] = hlp.start_values

    for i in range(1, t_num):
        t_list[i] = t_list[i-1] + dt
        k0 = pd.DataFrame(
            {'loc': f_vel(data_list[i-1], t_list[i-1]) * dt,
             'vel': f_acc(data_list[i-1], t_list[i-1], part3) * dt}
        )
        data_list[i] = data_list[i-1] + k0

    return t_list, data_list


def rk4(t0, tf, dt, part3=False):
    t_num = int((tf - t0) / dt)
    hlp.t_num = t_num
    t_list: list[float] = [0 for _ in range(t_num)]
    data_list: list[pd.DataFrame] = [None for _ in range(t_num)]

    t_list[0] = t0
    data_list[0] = hlp.start_values

    for i in range(1, t_num):
        t_list[i] = t_list[i-1] + dt

        k1 = pd.DataFrame(
            {'loc': f_vel(data_list[i-1], t_list[i-1]) * dt,
             'vel': f_acc(data_list[i-1], t_list[i-1], part3) * dt}
        )
        k2 = pd.DataFrame(
            {'loc': f_vel(data_list[i-1] + k1/2, t_list[i-1] + dt/2) * dt,
             'vel': f_acc(data_list[i-1] + k1/2, t_list[i-1] + dt/2, part3) * dt}
        )
        k3 = pd.DataFrame(
            {'loc': f_vel(data_list[i-1] + k2/2, t_list[i-1] + dt/2) * dt,
             'vel': f_acc(data_list[i-1] + k2/2, t_list[i-1] + dt/2, part3) * dt}
        )
        k4 = pd.DataFrame(
            {'loc': f_vel(data_list[i-1] + k3, t_list[i-1] + dt) * dt,
             'vel': f_acc(data_list[i-1] + k3, t_list[i-1] + dt, part3) * dt}
        )
        data_list[i] = data_list[i-1] + (k1 + k2*2 + k3*2 + k4) / 6

    return t_list, data_list


def verlet(t0, tf, dt, part3=False):
    t_num = int((tf - t0) / dt)
    hlp.t_num = t_num
    t_list: list[float] = [0 for _ in range(t_num)]
    data_list: list[pd.DataFrame] = [None for _ in range(t_num)]

    t_list[0] = t0
    data_list[0] = hlp.start_values

    for i in range(1, t_num):
        t_list[i] = t_list[i-1] + dt
        k0 = pd.DataFrame(
            {'loc': f_vel(data_list[i-1], t_list[i-1]) * dt + f_acc(data_list[i-1], t_list[i-1]) * 1/2 * dt**2,
             'vel': f_acc(data_list[i-1], t_list[i-1], part3) * 1/2 *dt}
        )
        k1 = pd.DataFrame(
            {'loc': [vec.Vector(0, 0) for _ in range(hlp.n)],
             'vel': f_acc(data_list[i-1] + k0, t_list[i-1], part3) * 1/2 * dt}
        )
        data_list[i] = data_list[i-1] + (k0 + k1) / 2

    return t_list, data_list


def leapfrog(t0, tf, dt, part3=False):
    t_num = int((tf - t0) / dt)
    hlp.t_num = t_num
    t_list: list[float] = [0 for _ in range(t_num)]
    data_list: list[pd.DataFrame] = [None for _ in range(t_num)]

    t_list[0] = t0
    data_list[0] = hlp.start_values

    for i in range(1, t_num):
        t_list[i] = t_list[i - 1] + dt
        k0 = pd.DataFrame(
            {'loc': [vec.Vector(0, 0) for _ in range(hlp.n)],
             'vel': f_acc(data_list[i-1], t_list[i-1], part3) * dt}
        )
        data_list[i] = data_list[i-1] + k0
        k1 = pd.DataFrame(
            {'loc': f_vel(data_list[i], t_list[i-1]) * dt,
             'vel': [vec.Vector(0, 0) for _ in range(hlp.n)]}
        )
        data_list[i] += k1

    return t_list, data_list


def to_loc_list(td_data, p_num):
    return list(map(lambda td: td.loc[p_num, 'loc'], td_data))
