# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

datei = open("comex.GC_140101_150101.csv")
y = []
for line in datei:
    tmp = line.split(",")
    y.append(float(tmp[4]))

x = np.arange(len(y))

fig, axes = plt.subplots(figsize = (18, 9))
axes.plot(x, y)