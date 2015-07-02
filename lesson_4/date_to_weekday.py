#!/usr/bin/env python

import sys
import os
import datetime


def date_to_weekday(input_date):
    year, month, day = input_date.split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    
    datetime_obj = datetime.datetime(year, month, day)
    return datetime_obj.weekday()

def main():
    test_date = "2015-07-2"
    print(date_to_weekday(test_date))

if __name__ == "__main__":
    main()