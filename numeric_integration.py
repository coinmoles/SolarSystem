import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('./SolarSystem.xlsx')
G = 1  # TODO: 값 대입 (AU, day 단위로 맞추려면 어떻게 해야하지 아몰랑)
n = len(data)
planets = data['name']
start_values = data[['x', 'y', 'vx', 'vy']]
m_list = data['m']


def f(df_prev: pd.DataFrame, t):
    df_new = pd.DataFrame(np.zeros((n, 4)), columns=df_prev.columns)

    for i in range(n):
        df_new.loc[i, 'x'] = df_prev.loc[i, 'vx']
        df_new.loc[i, 'y'] = df_prev.loc[i, 'vy']
        for j in range(n):
            if i == j:
                continue
            r = ((df_prev.loc[i, 'x'] - df_prev.loc[j, 'x']) ** 2 + (df_prev.loc[i, 'y'] - df_prev.loc[j, 'y']) ** 2) ** 0.5
            df_new.loc[i, 'vx'] += - G * m_list[j] / r ** 3 * (df_prev.loc[i, 'x'] - df_prev.loc[j, 'x'])
            df_new.loc[i, 'vy'] += - G * m_list[j] / r ** 3 * (df_prev.loc[i, 'y'] - df_prev.loc[j, 'y'])

    return df_new


def forward_euler(t0, tf, dt):
    t_num = int((tf - t0) / dt)
    t_list = [None for _ in range(t_num)]
    data_list = [None for _ in range(t_num)]

    t_list[0] = t0
    data_list[0] = start_values

    for i in range(1, t_num):
        t_list[i] = t_list[i-1] + dt
        data_list[i] = data_list[i-1] + dt * f(data_list[i-1], t_list[i-1])
        # print(t_list[i], data_list[i])

    return t_list, data_list


def rk4(t0, tf, dt):
    t_num = int((tf - t0) / dt)
    t_list = [None for _ in range(t_num)]
    data_list = [None for _ in range(t_num)]

    t_list[0] = t0
    data_list[0] = start_values

    for i in range(1, t_num):
        t_list[i] = t_list[i - 1] + dt

        k1 = dt * f(data_list[i - 1], t_list[i - 1])
        k2 = dt * f(data_list[i - 1] + k1 / 2, t_list[i - 1] + dt / 2)
        k3 = dt * f(data_list[i - 1] + k2 / 2, t_list[i - 1] + dt / 2)
        k4 = dt * f(data_list[i - 1] + k3, t_list[i - 1] + dt)
        data_list[i] = data_list[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t_list, data_list


def to_list(td_data, p_num, key):
    output = []

    for td in td_data:
        output.append(td.loc[p_num, key])

    return output
