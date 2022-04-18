#!/usr/bin/env python3

import matplotlib.pyplot as plt

with open('soubor-ux.txt', 'r') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
plt.plot(x ,y)
plt.show()

