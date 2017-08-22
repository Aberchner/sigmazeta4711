# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:56:28 2017

@author: Alex
"""

# This programm reformats the data from date-time-start-lowest-highest-end
# to tuples like (date, time, start, end, lowest, highest)

sourcefile = open("comex.GC_110101_120101.csv")
destinfile = open("goldprize 2007-2017.txt", "a")

data = []

for line in sourcefile:
    tmp = line.split(",")
    data.append((int(tmp[2]), int(tmp[3]), float(tmp[4]), float(tmp[7]), 
                     float(tmp[5]), float(tmp[6])))

for i in range(len(data)):
    destinfile.write(str(data[i]) + "\n")
destinfile.close()
