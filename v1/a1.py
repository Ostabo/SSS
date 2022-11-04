import numpy as np
import matplotlib.pyplot as plt

# Array from 10 to 70 with step 3
dis = np.arange(10, 71, 3)

analog_data = dict(np.genfromtxt('./data/messungen_v2', delimiter=';', dtype=[int, float]))

avg_data = dict()
sdt_data = dict()
for x in dis:
    raw_data = [float(s.replace(',', '.')) for s in
                np.genfromtxt('./data/' + str(x) + 'cm.csv',
                              delimiter=';',
                              skip_header=1000,
                              usecols=1,
                              dtype=str)]
    avg_data[x] = np.mean(raw_data, dtype=float)
    sdt_data[x] = np.std(raw_data, dtype=float)

# Plotting
fig, axs = plt.subplots(2, sharex=True)
fig.suptitle('Mean and std of the data')
axs[0].plot(avg_data.keys(), avg_data.values(), 'r', label='Mean')
axs[0].plot(analog_data.keys(), analog_data.values(), 'go', label='Analog')
axs[1].plot(sdt_data.keys(), sdt_data.values(), 'b', label='Std')
# x label
plt.xlabel('Distance (cm)')
# y label
axs[0].set(ylabel='Voltage (V)')
axs[1].set(ylabel='Voltage (V)')
fig.legend()

plt.show()
