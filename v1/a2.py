import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Array from 10 to 70 with step 3
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

# Casting to array
data = log_data.items()
listOfDict = list(data)
arr = np.array(listOfDict)

# Linear regression
slope, intercept, r, p, std_err = stats.linregress(arr[:, 0], arr[:, 1])

model = list(map((lambda z: slope * z + intercept), arr[:, 0]))

# Plotting
plt.plot(log_data.keys(), log_data.values(), 'ob', label='Log')
plt.plot(arr[:, 0], model, 'r', label='Linear regression')
plt.grid(True)

plt.title('Linear regression')
# x label
plt.xlabel('Distance (cm)')
# y label
plt.ylabel('Voltage (V)')

plt.show()
