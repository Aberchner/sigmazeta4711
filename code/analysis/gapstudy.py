# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 2017

@author: Jascha
"""

# This programm looks for gaps in the data and analyses how and how frequently they appear
from datetime import timedelta
import matplotlib.pyplot as plt
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
amountOfPrevVolume = {}
gapsByPostVolume = {}
amountOfPostVolume = {}
gapLengths = {}


def check_trade_data(trade_data, prev_trade_data):
    global existingData
    global missingData
    global gapsByYear
    global gapsByMonth
    global gapsByDay
    global gapsByTime
    global gapsByPrevVolume
    global amountOfPrevVolume
    global gapsByPostVolume
    global amountOfPostVolume
    global gapLengths
    existingData += 1

    # calculate gap size
    gap_size = int(((trade_data.time - prev_trade_data.time) / timedelta(minutes=1)) - 1)
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
    prev_volume = prev_trade_data.numberTrades
    try:
        amountOfPrevVolume[prev_volume] += 1
        gapsByPrevVolume[prev_volume] += gap_size
    except KeyError:
        amountOfPrevVolume[prev_volume] = 1
        gapsByPrevVolume[prev_volume] = gap_size
    # count gaps by the trade volume of the following trade
    post_volume = trade_data.numberTrades
    try:
        amountOfPrevVolume[post_volume] += 1
        gapsByPrevVolume[post_volume] += gap_size
    except KeyError:
        amountOfPrevVolume[post_volume] = 1
        gapsByPrevVolume[post_volume] = gap_size
    # count the Amount of gaps of each size
    if(gap_size > 0):
        try:
            gapLengths[gap_size] += 1
        except KeyError:
            gapLengths[gap_size] = 1


def print_results():
    print("Number of TradeData: {0} Number of Gaps: {1} Percentage of missing Trades: {2}"
          .format(str(existingData), str(missingData), str(missingData / (missingData + existingData)*100)))

    lists = sorted(gapLengths.items())  # sorted by key, return a list of tuples
    x, y = zip(*lists)  # unpack a list of pairs into two tuples
    #plt.bar(range(len(y)), y)
    #plt.xticks(range(len(x)), x, rotation=90)
    plt.plot(x,y, "b-")
    plt.yscale("log")
    plt.xscale("log")
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.tick_params(axis='both', which='minor', labelsize=6)
    plt.show()

    #plt.xticks(range(len(gapLengths)), gapLengths.keys())
    # plt.show()
    # TODO


def write_results():
    output_file = open("../../textdocuments/gapStudyResults.txt", "w")

    output_file.write("Amount of existing Trade data vs. Amount of gaps")
    output_file.write("existing: {0}; gaps: {1}; {2} % missing"
                      .format(str(existingData), str(missingData), str(missingData / (missingData + existingData)*100)))
    # TODO


def gap_study():
    # setup
    #all_data = dataformatting.read_comex_GC("../../data/comex.GC_070101_080101.csv")
    all_data = dataformatting.read_trade_data("../../data/goldprize 2007-2017.txt")

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
