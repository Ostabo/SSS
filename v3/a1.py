import numpy as np
import matplotlib.pyplot as plt


sound_1_data = np.genfromtxt('./data/sound1.csv',
                              delimiter=';',
                              skip_header=3800,
                              skip_footer=3800,
                              converters={0: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                          1: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                              dtype=str)
tuple0 = [seq[0] for seq in sound_1_data]
tuple1 = [seq[1] for seq in sound_1_data]

# Darstellung des Signals unserer Mundharmonikaaufnahme
plt.plot(tuple0, tuple1, 'b')
plt.ylabel('Spannung in mV')
plt.xlabel('Zeit in ms')
plt.grid(True)
plt.savefig('img/sound1.png')
plt.show()

# Gundperiode 1,5 ms
# Grundfrequenz 666,6 Hz
# Signaldauer 50 ms
# Abtastrate 0,005 ms => 200 kHz
# Signallänge 50 ms / 0,005 ms => 10.000 Samples
# Abtastinterval 0,005 ms => 0,000005 s

difference = np.abs(tuple0[1] - tuple0[0])

fourier = np.fft.fft(tuple1)

spektrum = np.abs(fourier)

freq = range(0, len(tuple1), 1) / (difference * len(tuple1))

plt.plot(freq, spektrum, 'b')
plt.ylabel('Amplitude')
plt.xlabel('Frequenz in kHz')
plt.grid(True)
plt.savefig('img/sound1_fft.png')
plt.show()

find_max = np.max(spektrum)
find_index_max = np.where(spektrum == find_max)
print('Frequenz mit größter Amplitude : ' + str(find_index_max[0][0]) + ' Hz' + ' at ' + str(find_max))


