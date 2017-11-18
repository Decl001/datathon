import pandas as pd
import numpy as np 

def readData():
    '''
    Creates a pandas data frame from the 
    csv files
    '''
    bikesData = pd.read_csv('Datahack 2017 Data/bikes.csv', names=['Date', 'Count'])
    holidaysData = pd.read_csv('Datahack 2017 Data/holidays.csv')
    weatherData = pd.read_csv('Datahack 2017 Data/weather.csv')
    return bikesData,holidaysData,weatherData


def countMatches(bikesData,weatherData):
    weatherDates = list(weatherData.Date)
    bikesDates = list(bikesData.Date)
    count = 0
    for date in weatherDates:
        if date in bikesDates:
            count += 1
    print(weatherData)
    print(count)


bd,hd,wd = readData()
dateW = list(wd.Date)
dateB = list(bd.Date)
for d in dateB:
    if d not in dateW:
        print(d)



