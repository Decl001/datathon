import pandas as pd
import numpy as np 
import math

def readData():
    '''
    Creates a pandas data frame from the 
    csv files
    '''
    data = pd.read_csv('DataHack 2017 Data/bike-weather-concat.csv')

    return data

def fillNullValues(data):
    for i,row in data.iterrows():
        for col in data:
            if (col != 'Date' and col != 'Bikes'):
                if math.isnan(row[col]):
                    surroundVals = []
                    for ind in range(i-3,i+3):
                        if ind != i:
                            try:
                                surroundVals.append(data.iloc[ind][col])
                            except:
                                pass

                    s = sum(surroundVals)
                    newVal = s/len(surroundVals)
                    data.iloc[i,data.columns.get_loc(col)] = newVal
    
    return data
    

data = fillNullValues(readData())
data.to_csv('DataHack 2017 Data/Null-filled-concat.csv')