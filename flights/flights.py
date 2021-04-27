#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Problem:https://itu.kattis.com/problems/itu.flights

from itu.algs4.searching.red_black_bst import RedBlackBST
from itu.algs4.stdlib.stdio import readLine, readInt
#https://docs.python.org/3/library/time.html
from time import strftime
from time import gmtime

def timeConversion(stingInput):
    hours,minutes,seconds= stingInput.split(":")
    
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    totalSeconds = hours * (60**2) + (minutes*60) + seconds
    return totalSeconds

#convert time in seconds to time in the needed format
def second_toTime(sec):
    #example strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    #convert the time returned by gmtime to a string specified by the format argument
    #%H Hour (24-hour clock) as a decimal number [00,23].
    #%M Minute as a decimal number [00,59].
    #%S Second as a decimal number [00,61].
    return strftime("%H:%M:%S", gmtime(sec))


m, n= readLine().split()
m=int(m)
n=int(n)

redblack = RedBlackBST();

for i in range(m):
    time,place= readLine().split()
    time=timeConversion(time)
    #insert this key value pair.
    redblack.put(time,place)

for i in range(n):
    operations = readLine()

    if operations[:4]=="dest":
        _,time=operations.split()
        time=timeConversion(time)
        #.get() return value associated with key.
        destination=redblack.get(time)
        if destination is None:
            print("-")
        else:
            print(destination)
            
    elif operations[:4]=="canc":
        _,time=operations.split()
        time=timeConversion(time)
        #remove the key and its associated value.
        redblack.delete(time)
        
    elif operations[:4]=="dela":
        _,time,delay=operations.split()
        delay = int(delay)
        if delay > 0:
            time=timeConversion(time)
            time_after_delay= time + delay
            destination=redblack.get(time)
            if destination is not None:
            #shouldn't create new nodes if the destination already exists.
                redblack.delete(time)
                redblack.put(time_after_delay,destination)
            
    elif operations[:4]=="rero":
        _,time,destination=operations.split()
        time=timeConversion(time)
        if redblack.get(time) is not None:
            redblack.delete(time)
            redblack.put(time,destination)
            
    elif operations[:4]=="next":
        _,time=operations.split()
        time_to_seconds=timeConversion(time)
        tnext=redblack.ceiling(time_to_seconds)
        next_departure=str(second_toTime(tnext) +" "+ redblack.get(tnext))
        print(next_departure)
        
    elif operations[:4]=="coun":
        _,time1,time2=operations.split()
        t1=timeConversion(time1)
        t2=timeConversion(time2)
        print(redblack.size_range(t1,t2))

