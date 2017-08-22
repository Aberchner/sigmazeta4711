# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 2017

@author: Jascha
"""

# This programm looks for gaps in the data and analyses how and how frequently they appear
import datetime
import matplotlib.pyplot as plotter

allDatapoints = []

def convertTimeStamp (date, time):
    """contains a single price value with the corresponding timestamp
    the timestamp is converted into a Datetime object"""
    dateIn = date
    timeIn = time
    #create date
    #datetime(year, month, day
    dt = datetime.datetime(int(int(dateIn)/10000), int(int(dateIn)/100)%100, int(dateIn)%100,
                             #hour, minute)
                            int(int(timeIn)/ 10000), int(int(timeIn)/100)%int(100))

    return dt

class time_price_pair:

    @property
    def next_pair(self):
        """returns the next time_price_pair"""
        return self.time

    @next_pair.setter
    def next_pair(self, next_pair):
        """sets the next pair"""
        self.next_pair=next_pair()

    def __init__(self, date, time, price):
        self.time = convertTimeStamp(date, time)
        self.price = price


def readdata():
    """reads the datafile and builds a list of time_price_pairs"""
    file = open("../data/goldprize 2007-2017.txt")
    first = None
    prev = None
    for line in file:
        if(line[:1] == "("):
            line = line[1:]
            line = line[:-2]
        temp = time_price_pair(line.split(", ")[0], line.split(", ")[1], line.split(", ")[3])
        if not prev is None:
            prev.next = temp
        prev = temp;
        allDatapoints.append(temp)
        if first is None:
            first = temp
    return first

readdata()
print("reading finished")
t = []
d = []
exist = 0
missing = 0
for pair in allDatapoints:
    try:
        temp = pair.next
    except AttributeError:
        temp = None
    exist += 1
    if not temp is None:
        dif = temp.time-pair.time
        missing += ((dif)/datetime.timedelta(minutes=1))-1
        # print(str(missing) + " " + str(((dif)/datetime.timedelta(minutes=1))-1))
        # print(str(pair.time) + " " + str(temp.time))
print(str(exist) + "Datapoints with " + str(missing) + " gaps. " + str(missing/(exist+missing)*100) + "% missing")
