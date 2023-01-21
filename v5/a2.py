import numpy as np

# 2.1
bits = 11
accuracy = (1 / (np.power(2, bits)))
delta = ((10 - (-10)) / (np.power(2, bits)))
print("Genauigkeit des 11-Bit AD-Wandlers: ", accuracy)
print(f"Theoretischer Quantisierungsfehler des 11-Bit AD-Wandlers: {delta} V")
print()

# 2.3
data = np.genfromtxt('./2_2.csv',
                     delimiter=';',
                     skip_header=1,
                     converters={0: lambda s: int(s.decode('utf-8').replace(',', '.')),
                                 1: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                 2: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                 3: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                 4: lambda s: float(s.decode('utf-8').replace(',', '.')),
                                 5: lambda s: int(s.decode('utf-8').replace(',', '.'))},
                     dtype=str)
zipped_data = list(zip(*data))
ref = zipped_data[2]  # Feinmessgerät
multi = zipped_data[1]  # Multi
adw = zipped_data[3]  # AD-Wandler

messfehler_multi = []
messfehler_adw = []
for i, el in enumerate(ref):
    messfehler_multi.append(el - multi[i])
    messfehler_adw.append(el - adw[i])

messfehler_multi = np.array(messfehler_multi)
messfehler_adw = np.array(messfehler_adw)
print(f"Messfehler Multi: {np.mean(messfehler_multi)}")
print(f"Messfehler AD-Wandler: {np.mean(messfehler_adw)}")
print()
std_multi = np.sqrt(np.abs((1 / len(zipped_data) - 1) * np.sum(messfehler_multi)))
std_adw = np.sqrt(np.abs((1 / len(zipped_data) - 1) * np.sum(messfehler_adw)))
print(f"Standardabweichung Multi: {std_multi}")
print(f"Standardabweichung AD-Wandler: {std_adw}")
