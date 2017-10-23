## Import CSV and retrieve lat/long/elev as floating points
## open CSV as pandas dataframe and add the date/lat/long/elev as new columns
## save the pandas dataframe as a csv


#####
import csv
import pandas as pd
import datetime
import glob
import time
import os
start_time = time.time()


##### Loop through csvs
path = 'C:\Users\matt9014\Climate_geoanalytics\csvinfolder\*.csv'   ## Change this to be the path to the folder with the *.csv files, keep the file extension
for fname in glob.glob(path):
    outpath = os.path.join('C:\Users\matt9014\Climate_geoanalytics\csvoutfolder', os.path.basename(fname))  ## Change this to be the path to the out folder 


##### Retrieve lat/lon/elev
    with open(fname, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        rowstring = (next(reader)[0]).split(" ")
        latitude = float(rowstring[1])
        longitude = float(rowstring[4])
        next(reader)
        next(reader)
        elevation = float(next(reader)[0].split(" ")[1])


##### Create pd dataframe, create dates, add lat/lon/elev, rename columns, delete year/yday, save as csv
    dataframe = pd.read_csv(fname, sep=',', header=6)
    dateSelect = "'2016-11-06'"
    dataframe[9] = dateSelect
    for index, row in dataframe.iterrows():
        ifor_val = datetime.date(int(row[0]), 1, 1) + datetime.timedelta(int(row[1]) - 1)
        dataframe.set_value(index,9,ifor_val)
        dataframe.set_value(index,10,latitude)
        dataframe.set_value(index,11,longitude)
        dataframe.set_value(index,12,elevation)

    dataframe.columns = ['year', 'yday', 'tmax_c', 'tmin_c', 'dayl_s', 'prcp_mm', 'srad_wm2', 'swe_kgm2', 'vp_pa', 'date', 'lat', 'lon', 'elev_m']
    del dataframe['year']
    del dataframe['yday']

    dataframe.to_csv(path_or_buf=outpath, index = False)


##### Execution time
print("--- %s seconds ---" % (time.time() - start_time))
