# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 21:37:56 2017

@author: Alex
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


# Calculates the arithmetic average of a given set of data.
def average(array):
    average = 0
    for i in range(0, len(array)):
        average = average + array[i]
    return average/len(array)

# Calculates the standard deviation of a given array.
def standard_deviation(array):
    a = average(array)
    tmp = 0
    for i in range(len(array)):
        tmp = tmp + (a - array[i])**2
    return tmp / (len(array) * (len(array) - 1))

# Calculates the skewness of a given dataset.
def skewness(array):
    a = average(array)
    d = standard_deviation(array)
    g = 0
    for i in range(len(array)):
        g = g + (array[i] - a)**3
    g = g/(len(array)*d**3)
    return g

# Calculates the kurtosis of a given dataset.
def kurtosis(array):
    a = average(array)
    d = standard_deviation(array)
    w = 0
    for i in range(len(array)):
        w = w + (array[i] - a)**4
    w = (w/(len(array)*d**4)) - 3
    return w

# Calculates the numerical difference between the start and the end value of
# a trade.
def end_minus_start(start, end):
    differences = []
    for i in range(len(start)):
        differences.append(end[i] - start[i])
    return differences

# Calculates the absolute numerical difference between the start and the end 
# value of a trade.
def abs_end_minus_start(start, end):
    differences = []
    for i in range(len(start)):
        differences.append(abs(end[i] - start[i]))
    return differences


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
    diff = end_minus_start(start, end)
    values = []
    for i in range(len(diff)):
        inside = False
        for j in range(len(values)):
            if round(diff[i], 1) == values[j]:
                inside = True
            else:
                continue
        if inside == False:
            values.append(round(diff[i], 1))
    values = sorted(values)
    density = [0]*len(values)
    for i in range(len(diff)):
        for j in range(len(values)):
            if round(diff[i], 2) == values[j]:
                density[j] = density[j] + 1
            else:
                continue
    sumdensity = 0
    for i in range(len(density)):
        sumdensity = sumdensity + density[i]
    for i in range(len(density)):
        density[i] = density[i]/sumdensity
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
            

data = read_and_format(src, 10)
start, end = [], []
for i in range(len(data)):
    start.append(data[i][2])
    end.append(data[i][3])
#diff = end_minus_start(start, end)
#diffabs = abs_end_minus_start(start, end)
#a = average(diff)
#aabs = average(diffabs)
#d = standard_deviation(diff)
#dabs = standard_deviation(diffabs)
#g = skewness(diff)
#w = kurtosis(diff)
values, density = histogram(start, end)
#X, Y = normal_distribution(a, d, abs(min(values)), max(values))

#print(rise_tie_fall_counter(start, end))
#print("average:", a)
#print("average absolute:", aabs)
#print("standard deviation:", d)
#print("standard deviation absolute:", dabs)
#print("skewness:", g)
#uiX0kCEF4njF0i
#print("kurtosis:", w)
print(values)
print(density)

#plt.scatter(values, density)
#plt.plot(X, Y)







