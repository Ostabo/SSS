import numpy as np
import matplotlib.pyplot as plt


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


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

plt.plot(frequency_s, b_peak_to_peak_s, 'b')
plt.plot(frequency, b_peak_to_peak, 'r')
plt.title('Amplitude vs. Frequency')
plt.legend(['small', 'big'])
plt.ylabel('Amplitude in mV')
plt.xlabel('Frequenz in Hz')
plt.grid(True)
plt.savefig('img/sound_amplitude.png')
plt.show()

# Amplitude in dB
b_peak_to_peak_db_s = 20 * np.log10(b_peak_to_peak_s)
b_peak_to_peak_db = 20 * np.log10(b_peak_to_peak)
# Phase in degree
phase_degree_s = (np.array(phase_s) * -1) * np.array(frequency_s) * 360 / 1e6 * 360
phase_degree = (np.array(phase) * -1) * np.array(frequency) * 360 / 1e6 * 360
# TODO understand why 2 * 360 and scale is 1e6

# Plot Amplitude and Phase - Bode Diagramm
plt.plot(frequency_s, b_peak_to_peak_db_s, 'b')
plt.plot(frequency, b_peak_to_peak_db, 'r')
plt.title('Frequency vs. Amplitude - Bode Diagram')
plt.legend(['small', 'big'])
plt.ylabel('Amplitude in dB')
plt.xlabel('Frequency in Hz')
plt.grid(True)
plt.semilogx()
plt.savefig('img/sound_bode_amplitude.png')
plt.show()

plt.plot(frequency_s, phase_degree_s, 'b')
plt.plot(frequency, phase_degree, 'r')
plt.title('Frequency vs. Phase - Bode Diagram')
plt.legend(['small', 'big'])
plt.ylabel('Phase in °')
plt.xlabel('Frequenz in Hz')
plt.grid(True)
plt.semilogx()
plt.savefig('img/sound_bode_phase.png')
plt.show()
