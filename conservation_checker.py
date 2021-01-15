import vector as vec
import helper as hlp


def get_momentum(df_data):
    total_momentum = vec.Vector(0, 0)
    for i in range(hlp.n):
        total_momentum += df_data.loc[i, 'vel'] * hlp.m_list[i]
    return total_momentum


def to_momentum_list(df_data_list):
    return list(map(get_momentum, df_data_list))


def get_angular_momentum(df_data):
    total_angular_momentum = 0
    for i in range(hlp.n):
        total_angular_momentum += (df_data.loc[i, 'vel'][0] * df_data.loc[i, 'loc'][1] -
                           df_data.loc[i, 'vel'][1] * df_data.loc[i, 'loc'][0]) * hlp.m_list[i]
    return total_angular_momentum


def to_angular_momentum_list(df_data_list):
    return list(map(get_angular_momentum, df_data_list))


def get_energy(df_data):
    total_energy = 0
    for i in range(hlp.n):
        for j in range(i+1, hlp.n):
            total_energy += - hlp.G * hlp.m_list[i] * hlp.m_list[j] / \
                            (2 * abs(df_data.loc[i, 'loc'] - df_data.loc[j, 'loc']))
    return total_energy


def to_energy_list(df_data_list):
    return list(map(get_energy, df_data_list))
