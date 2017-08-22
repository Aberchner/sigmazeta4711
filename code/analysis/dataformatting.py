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
    
    def __init__(self,type, time, startValue, endValue, highestValue,
                 lowestValue, numberTrades):
        if type == "real":
            self.time = (int) time
            self.startValue = (int) startValue
            self.endValue = (int) endValue
            self.highestValue = (int) highestValue
            self.lowestValue = (int) lowestValue
            self.numberTrades = (int) numberTrades
        if type == "sim":
            self.startValue = (int) startValue
            self.endValue = (int) endValue
            
def read_comex_GC(path):
    file = open(path)
    tradeData = []
    file.readline
    
    for line in file:
        tmp = line.split(",")
        time = datetime.datetime((int(int(tmp[2])/10000),
                                  int(int(tmp[2])/100)%100,
                                  int(tmp[2])%100,
                                  int(int(tmp[3])/ 10000),
                                  int(int(tmp[3])/100)%int(100)))
        tradeData.append(TradeData(time,tmp[4],tmp[7],tmp[5],tmp[6],tmp[8]))
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
    