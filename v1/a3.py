import numpy as np

raw_data_width = np.genfromtxt('./data/dina4_breite.csv',
                                delimiter=';',
                                skip_header=1000,
                                converters={1: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                                usecols=1,
                                dtype=str)

raw_data_length = np.genfromtxt('./data/dina4_länge.csv',
                                delimiter=';',
                                skip_header=1000,
                                converters={1: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                                usecols=1,
                                dtype=str)

mean_width = np.mean(raw_data_width, dtype=float)
std_width = np.std(raw_data_width, dtype=float)
mean_length = np.mean(raw_data_length, dtype=float)
std_length = np.std(raw_data_length, dtype=float)


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

# TODO understand stuff and get cm

