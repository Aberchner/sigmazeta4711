# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:56:28 2017

@author: Alex
"""

# This programm reformats the data from date-time-start-lowest-highest-end
# to tuples like (date, time, start, end, lowest, highest)

data = []

#file1 = open("comex.GC_140101_150101.csv")
for line in file1:
    tmp = line.split(",")
    data.append((int(tmp[2]), int(tmp[3]), float(tmp[4]), float(tmp[7]), 
                     float(tmp[5]), float(tmp[6])))

#file2 = open("comex.GC_150101_160101.csv")
for line in file2:
    tmp = line.split(",")
    data.append((int(tmp[2]), int(tmp[3]), float(tmp[4]), float(tmp[7]), 
                     float(tmp[5]), float(tmp[6])))

#file3 = open("comex.GC_160101_170101.csv")
for line in file3:
    tmp = line.split(",")
    data.append((int(tmp[2]), int(tmp[3]), float(tmp[4]), float(tmp[7]), 
                     float(tmp[5]), float(tmp[6])))

#file4 = open("goldprize 2014-2017.txt", "w")
for i in range(len(data)):
    file4.write(str(data[i]) + "\n")
file4.close()
