## Day of year and year to date fromm csv file

import csv
import pandas as pd
import datetime
import glob

##path = 'C:\Users\matt9014\Climate_geoanalytics\*.csv'
##for fname in glob.glob(path):
##    print(type(fname))
##    data = pd.read_csv(fname, sep=',', header=None)
##    data = data[1:]
##    dateSelect = "'2016-11-06'"
##    data[9] = dateSelect
##    for index, row in data.iterrows():
##        date = datetime.date(int(row[0]), 1, 1) + datetime.timedelta(int(row[1]) - 1)
##        row[9] = date
##
##    data.to_csv(path_or_buf=fname)


#####
dataframe = pd.read_csv('C:\Users\matt9014\Climate_geoanalytics\lat_25125lon_-81003.csv', sep=',', header=6)
dateSelect = "'2016-11-06'"
dataframe[9] = dateSelect
for index, row in dataframe.iterrows():
    ifor_val = datetime.date(int(row[0]), 1, 1) + datetime.timedelta(int(row[1]) - 1)
    dataframe.set_value(index,9,ifor_val)
    dataframe.set_value(index,10,'test')
    dataframe.set_value(index,11,'test2')
    dataframe.set_value(index,12,'test3')
print(dataframe)

##    
##    date = datetime.date(int(row[0]), 1, 1) + datetime.timedelta(int(row[1]) - 1)
##    row[9] = date
##    dataframe[9][index] = date
   # dataframe.loc[:,(9,index)] = date
    
##print(dataframe)

dataframe.to_csv(path_or_buf='C:\Users\matt9014\Climate_geoanalytics\lat_25125lon_-81003_2.csv')
############
