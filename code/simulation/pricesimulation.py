# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:24:54 2017

@author: Alex
"""
import sys
sys.path.insert(0, '../analysis')
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import dataformatting as df
import random as rd

#Interpolating 
rootvalues_comexGC = "../simulation/rootvalues_comexGC.txt"
rootdensity_comexGC = "../simulation/rootdensity_comexGC.txt"

rootvalues_interpolated = "../simulation/rootvalues_interpolated.txt"
rootdensity_interpolated = "../simulation/rootdensity_interpolated.txt"

#values_comexGC = df.read_simulation_root(rootvalues_comexGC)
#density_comexGC = df.read_simulation_root(rootdensity_comexGC)

#a = np.amax([abs(np.amin(values_comexGC)), abs(np.amax(values_comexGC))])
#tck = sp.interpolate.splrep(values_comexGC, density_comexGC)
#values_interpolated = np.arange(-a, a, 0.1)
#density_interpolated = sp.interpolate.splev(values_interpolated, tck, der = 0)

#df.write_simulation_root(rootvalues_interpolated, 'w', np.around(values_interpolated, 1))
#df.write_simulation_root(rootdensity_interpolated, 'w', density_interpolated)

#plt.figure(figsize=(15, 15))
#plt.plot(values_interpolated, density_interpolated)
#plt.scatter(values_comexGC, density_comexGC)

#The creation of the root
values = df.read_simulation_root(rootvalues_interpolated)
density = df.read_simulation_root(rootdensity_interpolated)

x = np.amin(density)
for i in range(len(density)):
    density[i] = int(round(density[i]/x))

priceroot = []
for i in range(len(density)):
    for j in range(density[i]):
        priceroot.append(values[i])

#The creation of the price
N = 10
start_price = 1000
start_values = [start_price]
end_values = []

for i in range(N):
    random = rd.randint(0, len(priceroot))
    end_values.append(start_values[i] + priceroot[random])
    start_values.append(end_values[i])

x = np.arange(len(start_values))
plt.plot(x, start_values)






