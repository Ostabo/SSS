import numpy as np


sound_1_data = np.genfromtxt('./data/sound1.csv',
                              delimiter=';',
                              skip_header=1000,
                              converters={1: lambda s: float(s.decode('utf-8').replace(',', '.'))},
                              usecols=1,
                              dtype=str)

print(sound_1_data)
