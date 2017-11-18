import pandas as pd
import numpy as np 
import math

def readData():
    '''
    Creates a pandas data frame from the 
    csv files
    '''
    data = pd.read_csv('DataHack 2017 Data/Null-filled-rem-outliers.csv')

    return data

def add_holidays(data):
    holidays = pd.read_csv('DataHack 2017 Data/holidaysformatted.csv')
    holList = list(holidays.Date)
    listValue = []
    for date in data.Date:
        if date in holList:
            listValue.append(1)
        else:
            listValue.append(0)
    
    series = pd.Series(listValue)
    data['Holiday'] = series
    return data

data = add_holidays(readData())
data.to_csv('DataHack 2017 Data/concat-data-holidays.csv')