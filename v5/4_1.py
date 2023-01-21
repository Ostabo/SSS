# -*- coding: utf-8 -*-
import redlab as rl
import numpy as np
import time

if __name__ == "__main__":
    while True:
        for i in range(0, 30):
            rl.cbVOut(0, 0, 101, np.sin(i / 30 * 2 * np.pi) + 1)  # plus eins da man keine negativen volt anzeigen kann.
            time.sleep(0.01)
