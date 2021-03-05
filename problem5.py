# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:39:25 2021

@author: USER
"""
import datetime
year = datetime.datetime.now().year
fed_day_number = 0
if(year%4==0 and year%100!=0 or year%400==0):
    fed_day_number = 29
else:
    fed_day_number = 28
mounths = {
    "January": 31,
    "February":fed_day_number,
    "March":31,
    "April":30,
    "May":31,
    "june":30,
    "july":31,
    "August":31,
    "September":30,
    "Outober":31,
    "November":30,
    "December":31
    }
for i in mounths.keys():
    print(f"{i}:{mounths[i]}")
    
