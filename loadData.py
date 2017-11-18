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

def removeOutliers(data):
    for i,row in data.iterrows():
        for col in data:
            if (col == 'TAVG' or col == 'TMIN' or col == 'TMAX'):
                surroundVals = []
                for ind in range(i-3,i+3):
                    if ind != i:
                        try:
                            surroundVals.append(data.iloc[ind][col])
                        except Exception as e:
                            pass

                s = sum(surroundVals)
                avg = s/len(surroundVals)
                if(avg > 20 + row[col] or row[col] > 20 + avg):
                    data.iloc[i,data.columns.get_loc(col)] = avg
    
    return data
    

data = fillNullValues(readData())
data = removeOutliers(data)
data.to_csv('DataHack 2017 Data/Null-filled-rem-outliers.csv')