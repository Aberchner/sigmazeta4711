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


# Calculates the numerical difference between the start and the end value of
# a trade.
def end_minus_start(start, end):
    differences = []
    for i in range(len(start)):
        differences.append(end[i] - start[i])
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


def histogram(start, end):
    diff = end_minus_start(start, end)
    hist = []
    for i in range(len(diff)):
        if 
            

data = read_and_format(src)
start, end = [], []
for i in range(len(data)):
    start.append(data[i][2])
    end.append(data[i][3])
d = end_minus_start(start, end)
a = average(d)
s = standard_deviation(d)

print(rise_tie_fall_counter(start, end))
print(a)
print(s)






