# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:06:47 2017

@author: Anton
"""
from random import random
import math
import matplotlib.pyplot as plt
import numpy

bias = 0.001
def simulate_by_probability(n, probabilities, start_value):
    values = []
    current_value = start_value
    for i in range(n):
        threshold = random()
        if threshold < probabilities[i]:
            values.append(current_value+1)
        if threshold >= probabilities[i]:
            values.append(current_value-1)
        current_value = values[i]
        
    return values

def martingale(values, probabilities,omega,gamma):
    x = []
    s = 0
    end_value = 0
    for i in range(len(probabilities)):
        s = s + ((gamma+1)*probabilities[i]-1)**2
    
    s = math.sqrt(s)
    for i in range(len(values)):
        x.append(omega*((gamma+1)*probabilities[i]-1)/(s))
    
    for i in range(1,len(x)):
        if values[i]<values[i-1]:
            end_value -= x[i-1]
        else:
            end_value += x[i-1]*(gamma-1)
    return end_value,x

def get_probabilities(n):
    probabilities = []
    for i in range(n):
       probabilities.append(random()+bias)
    return probabilities

n = 100000
k = 100
z = 0
for i in range(k):
    probs = get_probabilities(n)
    values = simulate_by_probability(n,probs,0)
    end_value,x= martingale(values,probs,1000,2)
    z += end_value 
print(z)

#print(x)
#print(values)