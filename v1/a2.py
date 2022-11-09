from matplotlib import pyplot as plt
import numpy as np

# ---------------------------------------Aufgabe 2------------------------------------------- #

dis = np.arange(10, 71, 3)
log_dis = dict()
for x in dis:
    log_dis[x] = np.log(x)

x_array = []
log_data = dict()
for x in dis:
    raw_data = np.genfromtxt('./data/' + str(x) + 'cm.csv',
                             delimiter=';',
                             skip_header=1000,
                             max_rows=50000,
                             converters={1: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                             usecols=1,
                             dtype=str)
    log_data[log_dis[x]] = np.log(np.mean(raw_data))
    x_array.append(np.mean(raw_data))

log_y_arr = np.array(list(log_data.keys()))
log_x_arr = np.array(list(log_data.values()))


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
    B = np.mean(y) - a * np.mean(x)
    return B


def plot_lin_reg():
    a = calc_a(log_x_arr, log_y_arr)
    b = calc_b(log_x_arr, log_y_arr, a)

    y = []
    for num in range(len(log_x_arr)):
        y.append(a * log_x_arr[num] + b)

    plt.plot(log_x_arr, y, 'r', label='Linear regression')
    plt.plot(log_x_arr, log_y_arr, 'ob', label='Log')
    plt.show()


plot_lin_reg()

# ---------------------------------------Aufgabe 3------------------------------------------- #


raw_data_width = np.genfromtxt('./data/dina4_breite.csv',
                               delimiter=';',
                               skip_header=1000,
                               max_rows=50000,
                               converters={1: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                               usecols=1,
                               dtype=str)

raw_data_length = np.genfromtxt('./data/dina4_länge.csv',
                                delimiter=';',
                                skip_header=1000,
                                max_rows=50000,
                                converters={1: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                                usecols=1,
                                dtype=str)

mean_width = np.mean(raw_data_width, dtype=float)
std_width = np.std(raw_data_width, dtype=float)
mean_length = np.mean(raw_data_length, dtype=float)
std_length = np.std(raw_data_length, dtype=float)
emp_std_width = std_width / np.sqrt(len(raw_data_width))
emp_std_length = std_length / np.sqrt(len(raw_data_length))

perc_68_w = mean_width + 1 * std_width * 2
perc_95_w = mean_width + 1.96 * std_width * 4

perc_68_l = mean_length + 1 * std_length * 2
perc_95_l = mean_length + 1.96 * std_length * 4

print('Mean width: ' + str(mean_width))
print('Std width: ' + str(std_width))
print('Mean length: ' + str(mean_length))
print('Std length: ' + str(std_length))

print('68% Width: ' + str(perc_68_w))
print('95% Width: ' + str(perc_95_w))

print('68% Length: ' + str(perc_95_l))
print('95% Length: ' + str(perc_95_l))


# Funktionen zur Berechnung
# f (x) = e^b * x^a             -> Vorgabe in der Aufgabe
# f'(x) = e^b * a * x^(a-1)     -> Ableitung === Fehlerfortpflanzung da nur 1 Parameter


def kennlinie(x):
    return np.exp(B) * np.power(x, A)


def derivKennlinie(x):
    return np.exp(B) * (A * np.power(x, A - 1))


x1 = np.mean(raw_data_width)
delta_y_width = np.abs(derivKennlinie(x1) * emp_std_width)
y_in_cm_width = kennlinie(x1)

x2 = np.mean(raw_data_length)
delta_y_length = np.abs(derivKennlinie(x2) * emp_std_length)
y_in_cm_length = kennlinie(x2)

print('Width: ' + str(y_in_cm_width) + ' +- ' + str(delta_y_width))
print('Length: ' + str(y_in_cm_length) + ' +- ' + str(delta_y_length))
print()
area = y_in_cm_width * y_in_cm_length
print('Area: ' + str(area) + ' +- ' + str(np.sqrt(delta_y_width ** 2 + delta_y_length ** 2)))
