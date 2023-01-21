# -*- coding: utf-8 -*-
import redlab as rl
import numpy as np
import matplotlib.pyplot as plt


def record():
    data = rl.cbVInScan(0, 0, 0, 200, 8000, 1)
    np.save("aufgabe_5_8000_s200.npy", data)
    plt.plot(data)


def plot_data():
    freqs = ["2000", "2850", "3700", "4550", "5400", "6250", "7100", "8000_s1000", "8000_s200"]
    for i in freqs:
        data = np.load(f"aufgabe_5_{i}.npy")
        fig, ax = plt.subplots()
        ax.plot(data)
        fig.savefig(f"plots/aufgabe_5_{i}.png")


if __name__ == "__main__":
    # record()
    plot_data()
