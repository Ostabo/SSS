import numpy as np
import matplotlib.pyplot as plt

data_big = np.genfromtxt('./data/data_big.csv',
                         delimiter=';',
                         skip_header=1,
                         converters={0: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                     1: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                     2: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                     3: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                     4: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                         dtype=str)

frequency = [seq[0] for seq in data_big]
a_peak_to_peak = [seq[1] for seq in data_big]
b_peak_to_peak = [seq[2] for seq in data_big]
a_cycle_time = [seq[3] for seq in data_big]
phase = [seq[4] for seq in data_big]

data_small = np.genfromtxt('./data/data_small.csv',
                           delimiter=';',
                           skip_header=1,
                           converters={0: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                       1: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                       2: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                       3: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                       4: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                           dtype=str)

frequency_s = [seq[0] for seq in data_small]
a_peak_to_peak_s = [seq[1] for seq in data_small]
b_peak_to_peak_s = [seq[2] for seq in data_small]
a_cycle_time_s = [seq[3] for seq in data_small]
phase_s = [seq[4] for seq in data_small]

# Plot Frequency and Phase
plt.plot(frequency_s, phase_s, 'b')
plt.plot(frequency, phase, 'r')
plt.title('Phase vs. Frequency')
plt.legend(['small', 'big'])
plt.ylabel('Phase in ms')
plt.xlabel('Frequenz in Hz')
plt.grid(True)
plt.savefig('img/sound_phase.png')
plt.show()

# Amplitude in dB
a_peak_to_peak_db = 20 * np.log10(a_peak_to_peak)
b_peak_to_peak_db = 20 * np.log10(b_peak_to_peak)
# Phase in degree
phase_degree_s = np.array(phase_s) * 360 * np.array(a_cycle_time_s)
phase_degree = np.array(phase) * 360 * np.array(a_cycle_time)

# Plot Amplitude and Phase - Bode Diagramm
plt.plot(a_peak_to_peak_db, phase_degree_s, 'b')
plt.plot(a_peak_to_peak_db, phase_degree, 'r')
plt.title('Phase vs. Amplitude')
plt.legend(['small', 'big'])
plt.ylabel('Phase in degree')
plt.xlabel('Amplitude in dB')
plt.grid(True)
plt.semilogx()
plt.savefig('img/sound_bode.png')
plt.show()
