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

N = 3077284
data = read_and_format(src, N)

time = np.arange(0, N)
value = []
for i in range(len(data)):
    value.append(data[i][2])

fig, axes = plt.subplots(figsize = (18, 9))
axes.plot(time, value)
