"""
Script for analysis of "USdata" datesets.

In this dataset daily Temperature data of 210 US cites is present from 1850s to 2016
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class TemperatureAnalysisUS:

    months = { 'January':'-01-', 'February':'-02-', 'March'    :'-03-' ,
               'April'  :'-04-', 'May'     :'-05-', 'June'     :'-06-' ,
               'July'   :'-07-', 'August'  :'-08-', 'September':'-09-' ,
               'October':'-10-', 'November':'-11-', 'December' :'-12-' }
    dataPath = ''
    citiesMap = {}


    def __init__(self, dataPath = 'datasets/USdata/'):
        """
        Sets the cities map and datapath if provided.
        """

        if not self.citiesMap :
            df = pd.read_csv(dataPath+'city_info.csv')
            df.drop(columns=['Stn.Name', 'Stn.stDate', 'Stn.edDate', 'Unnamed: 0'], inplace=True)                
            self.citiesMap = df.set_index('Name')['ID'].to_dict()
        
        self.dataPath = dataPath
        

    def cityAnalysis(self, city, month = 0, day = 0, dateStart = '1700-01-01', dateEnd = '2010-01-01'):
        """
        Parameter 
        * city (REQUIRED) : City who's data's to be fetched.
        * month           : If not specified then data of all months 
                            will be included.
        * day             : If not specified then data of all days will 
                            be included.
        * dateStart       : Starting date, if not specified then full data
                            will be included.
        * dateEnd         : Ending date, if not specified then last aviliable 
                            date will be used.

        Return value      : Dataframe containing max, min temperature and precipitation 
                            data of specified city, within the specified bounds.
        """
        try:
            df = pd.read_csv(self.dataPath + self.citiesMap[city] + '.csv')
        except:
            return 0
        
        df.drop(columns='Unnamed: 0', inplace=True)
        df = df[df['Date'].between(dateStart, dateEnd)]
        
        if month:
            df = df[df['Date'].str.contains(self.months[month])]
        
        if day:
            df = df[df['Date'].str.contains('.-'+str(day),  regex=True)]

        df['tmax'] = df.apply(lambda x: (5/9)*(x['tmax'] - 32), axis=1) 
        df['tmin'] = df.apply(lambda x: (5/9)*(x['tmin'] - 32), axis=1)
            
        return df

        
    def citiesAnalysis(self, cityTuple, month, day = 0, dateStart = '1700-01-01', dateEnd = '2010-01-01'):
        """
        Parameter 
        * cityTuple (REQUIRED) : Cities who's data's to be fetched.
        * month     (REQUIRED) : Month in which analysis's to be done.
        * day                  : Day, if not specified then data of all days will 
                                 be included.
        * dateStart            : Starting date, if not specified then full data
                                 will be included.
        * dateEnd              : Ending date, if not specified then last aviliable 
                                 date will be used.
       
        This function merges the dataframe of all the cities passesd as argument after
        dropping the tmax, tmin, prcp columns and creating a new column with cities name
        containing the mean temperature.

        Return value           : Dataframe containing mean temperature data of specified
                                 cities within the specified bounds. cities name would
                                 be the column headings.
        """
        if isinstance(cityTuple, str):
            return self.cityAnalysis(cityTuple, month, day, dateStart, dateEnd)
        
        retdf = pd.DataFrame
        firstIter = True

    
        for city in cityTuple:
            cur_df = self.cityAnalysis(city, month, day, dateStart, dateEnd)
            cur_df[city] = cur_df[['tmin', 'tmax']].mean(axis=1)
            cur_df.drop(cur_df.columns[[1,2,3]], axis=1, inplace=True)
            
            if firstIter:
                retdf = cur_df
                firstIter = False
            else:
                retdf = retdf.merge(cur_df)
        
        return retdf


# TemperatureAnalysisUS().citiesAnalysis(['NewYork', 'Seattle'], 'June', '01').plot(x = 'Date', subplots=True)
# plt.show()