import numpy as np

# 3.1
bits = 10
accuracy = (1 / (np.power(2, bits)))
delta = (5 / (np.power(2, bits)))
print("Genauigkeit des 10-Bit AD-Wandlers: ", accuracy)
print(f"Theoretischer Quantisierungsfehler des 10-Bit AD-Wandlers: {delta} V")
print()

# 3.3
data = np.genfromtxt('./3_2.csv',
                     delimiter=';',
                     skip_header=1,
                     converters={0: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                 1: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                     dtype=str)

zipped_data = list(zip(*data))
volt = zipped_data[0]
pico = zipped_data[1]
diff = [volt[i] - pico[i] for i in range(len(volt))]

std_pico = np.sqrt(np.abs((1 / len(zipped_data) - 1) * np.sum(diff)))
print(f"Standardabweichung Pico: {std_pico}")
