import vector as vec


def get_momentum(df_data):
    total_momentum = vec.Vector(0, 0)
    for i in range(hlp.n):
        total_momentum += m_list[i] * df_data.loc[i, 'vel']
    return total_momentum


def to_momentum_list(df_data_list):
    return list(map(get_momentum, df_data_list))


def get_angular_momentum(df_data):
    total_angular_momentum = 0
    for i in range(hlp.n):
        total_momentum += m_list[i] * (df_data.loc[i, 'vel'][0] * df_data.loc[i, 'loc'][1] -
                                       df_data.loc[i, 'vel'][1] * f_data.loc[i, 'loc'][0])
    return total_angular_momentum


def to_angular_momentum_list(df_data_list):
    return list(map(get_angular_momentum, df_data_list))


def get_energy(df_data):
    for i in range(hlp.n):
        for j in range(hlp.n):
            if i != j:
                
