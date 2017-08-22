# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 21:37:56 2017

@author: Alex
"""

import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats
import operator as op
import dataformatting as df

src = "..\..\data\goldprize 2007-2017.txt"


# Counts the number of rising, falling and equal price trades.
def rise_tie_fall_counter(start, end):
    r, t, f = 0, 0, 0
    for i in range(len(start)):
        if start[i] < end[i]:
            r = r + 1
        elif start[i] > end[i]:
            f = f + 1
        else:
            t = t + 1
    return r, t, f


# Adds every difference between start and end to an array hist.
def histogram(start, end):
    diff = list(map(op.sub, start, end))

    values = sorted(set(diff), key = diff.index)
    
    numberValues = len(diff)
    
    density = [0]*len(values)
    for i in range(len(values)):
        density[i] = diff.count(values[i])/numberValues
    return values, density


# Calculates a normal distribution.
def normal_distribution(average, deviation, a, b):
    av, de = average, deviation
    de = 0.1
    X = np.linspace(-a, b, 1000)
    Y = []
    for i in range(len(X)):
        Y.append((math.exp(-0.5*((X[i]-av)/de)**2))/(de*(2*math.pi)**0.5))
    return X, Y

#data[0].startValue
data = df.read_trade_data(src, 10)
start, end = [], []
for i in range(len(data)):
    start.append(data[i].startValue)
    end.append(data[i].endValue)
diff = list(map(op.sub, start, end))
diffabs = list(map(op.abs, map(op.sub, start, end)))

print(rise_tie_fall_counter(start, end))
print("average:", np.mean(diff))
print("average absolute of diffabs:", np.mean(diffabs))
print("standard deviation:", np.std(diff))
print("standard deviation of diffabs:", np.std(diffabs))
print("skewness:", sp.stats.skew(diff))
print("kurtosis:", sp.stats.kurtosis(diff))
values, density = histogram(start, end)
print(values)
print(density)

X, Y = normal_distribution(np.mean(diff), np.std(diff), abs(min(values)), max(values))
#plt.scatter(values, density)
#plt.plot(X, Y)







