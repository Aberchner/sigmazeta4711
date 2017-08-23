# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:56:28 2017

@author: Alex
"""
import datetime
import numpy as np
# This programm reformats the data from date-time-start-lowest-highest-end
# to tuples like (date, time, start, end, lowest, highest)
#The TradeData class represents one Trade
class TradeData:
    
    def __init__(self, type, time, startValue, endValue, highestValue,
                 lowestValue, numberTrades, rise_probability=0):
        if type == "real":
            self.time = time
            self.startValue = float(startValue)
            self.endValue = float(endValue)
            self.highestValue = float(highestValue)
            self.lowestValue = float(lowestValue)
            self.numberTrades = int(numberTrades)
        if type == "sim":
            self.startValue = float(startValue)
            self.endValue = float(endValue)
            self.rise_probability = float(rise_probability)
            
def read_comex_GC(path):
    file = open(path)
    tradeData = []
    file.readline(-1)
    
    for line in file:
        tmp = line.split(",")
        time = datetime.datetime(int(int(tmp[2])/10000),
                                  int(int(tmp[2])/100)%100,
                                  int(tmp[2])%100,
                                  int(int(tmp[3])/ 10000),
                                  int(int(tmp[3])/100)%100)
        tradeData.append(TradeData("real",time,tmp[4],tmp[7],tmp[5],tmp[6],tmp[8]))
    file.close()    
    return tradeData

def read_trade_data(path, maxLines=np.Inf):
    file = open(path)
    tradeData = []
    counter = 0
    
    for line in file:
        tmp = line.split(",")
        time = datetime.datetime.strptime(tmp[0], "%Y-%m-%d %H:%M:%S")
        tradeData.append(TradeData("real",time,tmp[1],tmp[2],tmp[3],tmp[4],tmp[5]))
        counter = counter + 1
        if counter == maxLines:
            break
    file.close()
    return tradeData

#Write the trade data into a file. Flag "a" for append and "w" for write
def write_trade_data(path, flag, data):
    file = open(path, flag)
    
    for i in range(len(data)):
        tradeData = data[i]
        file.write(str(tradeData.time) + ","
                   + str(tradeData.startValue) + ","
                   + str(tradeData.endValue) + ","
                   + str(tradeData.highestValue) + ","
                   + str(tradeData.lowestValue) + ","
                   + str(tradeData.numberTrades) + "\n")
    file.close()

def write_simulation_root(path, flag, array):
    file = open(path, flag)
    for i in range(len(array)):
        file.write(str(array[i]) + "\n")
    file.close()

def read_simulation_root(path):
    array = []
    file = open(path)
    for line in file:
        array.append(float(line))
    file.close()
    return array
     
#data = read_comex_GC("..\..\data\original data\comex.GC_160101_170101.csv")
#write_trade_data("..\..\data\goldprize 2007-2017.txt", "a", data)
#print("process complete")

