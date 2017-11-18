import pandas as pd
import numpy as np 

def readData():
    '''
    Creates a pandas data frame from the 
    csv files
    '''
    bikesData = pd.read_csv('Datahack 2017 Data/bikes.csv')
    holidaysData = pd.read_csv('Datahack 2017 Data/holidays.csv')
    weatherData = pd.read_csv('Datahack 2017 Data/weather.csv')



