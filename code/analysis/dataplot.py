# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import matplotlib.pyplot as plt
import numpy as np

src = open("goldprize 2007-2017.txt")

# The method read_and_format gets the adress from a datafile, casts the
# entries to ints/floats and groups them into an array, which is returned.

def read_and_format(sourcefile, N=np.Inf):
    array = []
    i = 0
    for line in sourcefile:
        tmp = line[1:-2].split(", ")
        array.append((int(tmp[0]), int(tmp[1]), float(tmp[2]), float(tmp[3]), 
                      float(tmp[4]), float(tmp[5])))
        i = i + 1
        if i == N:
            break
    return array

N = 3077284
data = read_and_format(src, N)

time = np.arange(0, N)
value = []
for i in range(len(data)):
    value.append(data[i][2])

fig, axes = plt.subplots(figsize = (18, 9))
axes.plot(time, value)
