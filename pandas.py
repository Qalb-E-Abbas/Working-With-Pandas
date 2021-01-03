# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:03:52 2021

@author: Qalbe
"""


# you can find pandas operations by searching pandas series operations in your favourite browser.
# I will go through some of them


import pandas as pd

file = pd.read_csv('weather.csv')
file

file['outlook'][file['temperature'] == 'hot']
file['temperature'][file['humidity'] == 'high']

#file['temperature'].max()
#file['temperature'].min()
#file['temperature'].std() standard deviation
#file['temperature'].describe(), it will print every calculation
#file['temperature'].mean()  etc, if we have integers


# fill.fillna(0)   it will fill your dateset with O if there is any nan value/missing value

file.head() # it will print some of the rows/columns from dataset

file.head(2) #accessing two rows only


file.tail() # it will print some of the rows from dataset but the last ones

file.tail(2) #accessing two rows only from the last


file[2:4] # accessing second and third row



file.columns #accessing all columns

file.outlook #accessing outlook column only 



file[['outlook', 'temperature']] #accessing outlook and temperature columns only




# If operations

# give me all those temperatures greater than or equal to 30
#file[file.temperature >= 30]

#file[file.temperature == file.temperature.max()]

#file['outlook'][file.temperature == file.temperature.max()]

#file[['outlook', 'humidity']][file.temperature == file.temperature.max()]
