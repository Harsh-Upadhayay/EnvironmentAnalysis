

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

countriesMap = {}
dataPath = 'datasets/WorldBankData/tas_timeseries_annual_cru_1901-2020_'
months = {'January':'-01-', 'February':'-02-', 'March'    :'-03-',
          'April'  :'-04-', 'May'     :'-05-', 'June'     :'-06-',
          'July'   :'-07-', 'August'  :'-08-', 'September':'-09-',
          'October':'-10-', 'November':'-11-', 'December' :'-12-'}


def __setCountriesMap():
    """
    Call only once
    
    Reads the file countriesCode.txt and creates a map between countries
    name and their code used in the datasets. 
    
    The map is stored in countriesMap global variable.
    """
    global CountriesMap
    with open("datasets/WorldBankData/countriesCode.txt", "r") as file:
        data = file.readlines()
        for line in data:
                word = line.split('^^^^^')
  
    for pair in word:
        x, y = pair.split('**')
        countriesMap[y] = x


def TemperatureByCountryWBD(country, dateStart = 1700, dateEnd = 2100):
    """
    Parameter 
    * country (REQUIRED) : Country who's data's to be fetched
    * dateStart       : Starting date, if not specified then full data
                        will be included.
    * dateEnd         : Ending date, if not specified then last aviliable 
                        date will be used.

    Return value      : Dataframe containing temperature data of specified 
                        country and it's states, within the specified bounds.
    """
    global countriesMap
    if not countriesMap:
        __setCountriesMap()

    try:
        country = countriesMap[country]
        df = pd.read_csv(dataPath + country + '.csv', header=1)
    except:
        return pd.DataFrame()
    
    df.rename(columns={'Unnamed: 0': 'Date'},inplace=True)

    if 'Administrative unit not available' in df.columns:
        df.drop(['Administrative unit not available'], axis=1, inplace=True)
    
    df = df[df['Date'].between(dateStart, dateEnd)]    
    df.reset_index(drop=True , inplace=True)
    return df


def TemperatureByCountriesWBD(countryTuple, dateStart = 1700, dateEnd = 2100):
    """
    Parameter 
    * countryTuple (REQUIRED) : Countries who's data's to be fetched
    * dateStart               : Starting date, if not specified then full data
                                will be included.
    * dateEnd                 : Ending date, if not specified then last aviliable 
                                date will be used.
    
    This function internally calls the TemperatureByCountryWBD() function to fetch
    data of each country in a dataframe. Then it drops all the column of dataframe
    except for the country's temperature column, and then it merges the dataframes 
    of all countries and returns it.

    Return value              : Dataframe containing temperature data of specified 
                                countries, within the specified bounds.
    """    
    if isinstance(countryTuple, str):
        return TemperatureByCountryWBD(countryTuple, dateStart, dateEnd)
    
    retdf = pd.DataFrame
    firstIter = True

 
    for country in countryTuple:
        cur_df = TemperatureByCountryWBD(country, dateStart, dateEnd)
        if cur_df.empty:
            continue
        cur_df.drop(cur_df.iloc[:, 2:], inplace = True, axis = 1)

        if firstIter:
            retdf = cur_df
            firstIter = False
        else:
            retdf = retdf.merge(cur_df)
    
    return retdf


def TemperatureByStateWBD(country, stateTuple, dateStart = 1700, dateEnd = 2100):
    """
    Parameter 
    * country    (REQUIRED) : Country who's States are needed.
    * stateTuple (REQUIRED) : States who's data is to be fetched.
    * dateStart             : Starting date, if not specified then full data
                              will be included.
    * dateEnd               : Ending date, if not specified then last aviliable 
                              date will be used.
      
    Return value            : Dataframe containing temperature data of specified 
                              states, within the specified bounds.
    """
    if isinstance(stateTuple, str):
        stateTuple = (stateTuple,)
    df = TemperatureByCountryWBD(country, dateStart, dateEnd)
    
    for state in df.columns:
        if state not in stateTuple and state != 'Date':
            df.drop(columns=state, inplace=True)

    return df

