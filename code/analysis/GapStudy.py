# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 2017

@author: Jascha
"""

# This programm looks for gaps in the data and analyses how and how frequently they appear
from datetime import datetime as time
from datetime import timedelta
import matplotlib.pyplot as plotter
import dataformatting

# beware of Magic numbers
minYear = 2007
maxYear = 2017

existingData = 0
missingData = 0
# all variables that base gaps on time use the time from the previous TradeData
gapsByYear = [0]*(maxYear-minYear)
gapsByMonth = [0]*12
gapsByDay = [0]*7
gapsByTime = [0]*(24*60)
gapsByPrevVolume = {}
amountByPrevVolume = {}
gapsByPostVolume = {}
amountByPostVolume = {}
gapLengths = {}


def check_trade_data(tradeData, prevTradeData):
    global existingData
    global missingData
    global gapsByYear
    global gapsByMonth
    global gapsByDay
    global gapsByTime
    global gapsByPrevVolume
    global amountByPrevVolume
    global gapsByPostVolume
    global amountByPostVolume
    global gapLengths
    existingData += 1

    # calculate gap size
    gapSize = ((tradeData.time - prevTradeData.time) / timedelta(minutes=1)) - 1
    # count the number of gaps
    missingData += gapSize
    # count gaps by year
    gapsByYear[(prevTradeData.time.year) - minYear] += gapSize
    # count gaps by month
    gapsByMonth[(prevTradeData.time.month)-1] += gapSize
    # count Gaps by Weekday (Monday to Sunday)
    gapsByDay[(prevTradeData.time.weekday())] += gapSize
    # count gaps by hours*60+minutes
    gapsByTime[(prevTradeData.time.hour*60
                + prevTradeData.time.minute)] += gapSize
    # count gaps by the trade volume of the previous trade
    #TODO
    # count gaps by the trade volume of the following trade
    #TODO
    # count the Amount of gaps of each size
    #TODO

def print_results():
    print("Number of TradeData: {0} Number of Gaps: {1} Percentage of missing Trades: {2}"
          .format(str(existingData), str(missingData), str(missingData / (missingData + existingData))))
    #TODO


def write_results():
    outputFile = open("../../textdocuments/gapStudyResults.txt", "w")
    outputFile.write("existing: {0}; missing: {1}; {2}"
                     .format(str(existingData), str(missingData), str(missingData / (missingData + existingData))))
    #TODO

def gap_study():
    #setup
    allData = dataformatting.read_comex_GC("../../data/comex.GC_070101_080101.csv")

    print("reading finished - read " + str(len(allData)) + " lines")

    # iterate over all TradeData and analyse Gaps
    prev = None
    for currentTradeData in allData:
        if not prev is None:
            check_trade_data(currentTradeData, prev)
        prev = currentTradeData

    print_results()
    write_results()

gap_study()
