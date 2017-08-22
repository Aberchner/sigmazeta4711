# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:56:28 2017

@author: Alex
"""
import datetime
# This programm reformats the data from date-time-start-lowest-highest-end
# to tuples like (date, time, start, end, lowest, highest)
#The TradeData class represents one Trade
class TradeData:
    
    def __init__(self, type, time, startValue, endValue, highestValue,
                 lowestValue, numberTrades):
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
    file.close    
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
        
#data = read_comex_GC("..\..\data\original data\comex.GC_160101_170101.csv")
#write_trade_data("..\..\data\goldprize 2007-2017.txt", "a", data)
#print("process complete")

