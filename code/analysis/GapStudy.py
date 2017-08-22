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
gapsByYear = [0] * (maxYear - minYear)
gapsByMonth = [0] * 12
gapsByDay = [0] * 7
gapsByTime = [0] * (24 * 60)
gapsByPrevVolume = {}
amountByPrevVolume = {}
gapsByPostVolume = {}
amountByPostVolume = {}
gapLengths = {}


def check_trade_data(trade_data, prev_trade_data):
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
    gap_size = ((trade_data.time - prev_trade_data.time) / timedelta(minutes=1)) - 1
    # count the number of gaps
    missingData += gap_size
    # count gaps by year
    gapsByYear[prev_trade_data.time.year - minYear] += gap_size
    # count gaps by month
    gapsByMonth[prev_trade_data.time.month - 1] += gap_size
    # count Gaps by Weekday (Monday to Sunday)
    gapsByDay[prev_trade_data.time.weekday()] += gap_size
    # count gaps by hours*60+minutes
    gapsByTime[(prev_trade_data.time.hour * 60
                + prev_trade_data.time.minute)] += gap_size
    # count gaps by the trade volume of the previous trade
    # TODO
    # count gaps by the trade volume of the following trade
    # TODO
    # count the Amount of gaps of each size
    # TODO


def print_results():
    print("Number of TradeData: {0} Number of Gaps: {1} Percentage of missing Trades: {2}"
          .format(str(existingData), str(missingData), str(missingData / (missingData + existingData))))
    # TODO


def write_results():
    output_file = open("../../textdocuments/gapStudyResults.txt", "w")
    output_file.write("existing: {0}; missing: {1}; {2}"
                      .format(str(existingData), str(missingData), str(missingData / (missingData + existingData))))
    # TODO


def gap_study():
    # setup
    all_data = dataformatting.read_comex_GC("../../data/comex.GC_070101_080101.csv")

    print("reading finished - read " + str(len(all_data)) + " lines")

    # iterate over all TradeData and analyse Gaps
    prev = None
    for currentTradeData in all_data:
        if prev is not None:
            check_trade_data(currentTradeData, prev)
        prev = currentTradeData

    print_results()
    write_results()


gap_study()
