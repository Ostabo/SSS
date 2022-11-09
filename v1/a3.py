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

# Funktionen zur Berechnung
VtoCm = np.log(21) / np.log(np.mean(raw_data_width))  # Faktor von V zu cm
zero = np.log(21) - (VtoCm * np.log(np.mean(raw_data_width)))  # -> 0
z1 = (np.exp(zero) * VtoCm * np.mean(raw_data_width) ** (VtoCm - 1))  # exp(0) = 1, ableitung von e^b * x^a

# e^b * x^a  -  Umkehrung der doppelten Logarithmierung
y1 = np.exp(zero) * np.power(np.mean(raw_data_width), VtoCm)

# Berechnung von 21 cm Messfehler #
a2 = np.log(29.7) / np.log(np.mean(raw_data_length))
b2 = np.log(29.7) - (a2 * np.log(np.mean(raw_data_length)))
z2 = (np.exp(b2) * a2 * np.mean(raw_data_length) ** (a2 - 1))

# e^b * x^a  -  Umkehrung der doppelten Logarithmierung
y2 = np.exp(b2) * np.power(np.mean(raw_data_length), a2)

# Errechnung des Flächeninhalts
flache = round(y2, 2) * round(y1, 2)
# Ausgeben der errechneten Messkorrekturen für die jeweilige Gaußverteilung
print()
print("Width(68%) = " + str(round(y1, 2)) + " cm +- " + str(np.abs(perc_68_w)) + " cm")
print("Width(95%) = " + str(round(y1, 2)) + " cm +- " + str(np.abs(perc_95_w)) + " cm")
print()
print("Length(68%) = " + str(round(y2, 2)) + " cm +- " + str(np.abs(perc_68_l)) + " cm")
print("Length(95%) = " + str(round(y2, 2)) + " cm +- " + str(np.abs(perc_95_l)) + " cm")
print()
print("Ein DinA4 Blatt hat ein Flächeninhalt von " + str(round(flache, 2)) + " cm^2")
print("68% hat bei einem Flächeninhalt von " + str(round(flache, 2)) + "cm^2 einen Messfehler von +" + str(
    (perc_68_l + perc_68_w)) + "cm")
print("95% hat bei einem Flächeninhalt von " + str(round(flache, 2)) + "cm^2 einen Messfehler von +" + str(
    (perc_95_l + perc_95_w)) + "cm")
