from matplotlib import pyplot as plt
import numpy as np

dis = np.arange(10, 71, 3)
log_dis = dict()
for x in dis:
    log_dis[x] = np.log(x)

log_data = dict()
for x in dis:
    raw_data = np.genfromtxt('./data/' + str(x) + 'cm.csv',
                             delimiter=';',
                             skip_header=1000,
                             converters={1: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                             usecols=1,
                             dtype=str)
    log_data[log_dis[x]] = np.log(np.mean(raw_data))

log_x_arr = np.array(list(log_data.keys()))
log_y_arr = np.array(list(log_data.values()))

def get_mean(data):
    return np.mean(data)


def calc_a(x, y):
    global A
    top_term = 0
    bot_term = 0

    for num in range(len(x)):
        top_term += (x[num] - get_mean(x)) * (y[num] - get_mean(y))

    for num in range(len(y)):
        bot_term += (x[num] - get_mean(x)) ** 2

    A = top_term / bot_term
    return A


def calc_b(x, y, a):
    global B
    B = get_mean(y) - a * get_mean(x)
    return B
    

def plot_lin_reg():
    a = calc_a(log_x_arr, log_y_arr)
    b = calc_b(log_x_arr, log_y_arr, a)

    y = []
    for num in range(len(log_x_arr)):
        y.append(a * log_x_arr[num] + b)
    
    plt.plot(log_x_arr, y, 'r', label='Linear regression')
    plt.show()


plot_lin_reg()
#plt.plot(log_data.keys(), log_data.values(), 'ob', label='Log')
#plt.show()
