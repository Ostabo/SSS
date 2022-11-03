import numpy as np
import matplotlib.pyplot as plt

# Array from 10 to 70 with step 3
dis = np.arange(10, 70, 3)

avg_data = dict()
sdt_data = dict()
for x in dis:
    raw_data = [[s.replace(',', '.') for s in e] for e in np.genfromtxt('./data/' + str(x) + 'cm.csv', delimiter=';', skip_header=1000, dtype=str)]
    avg_data[x] = np.mean(raw_data, dtype=float)
    sdt_data[x] = np.std(raw_data, dtype=float)

# Plotting
plt.errorbar(avg_data.keys(), avg_data.values(), yerr=sdt_data.values(), fmt='o')
plt.xlabel('Distance (cm)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs Distance')
plt.show()
