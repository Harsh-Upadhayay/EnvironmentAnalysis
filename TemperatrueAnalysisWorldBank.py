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
    """
    global CountriesMap
    with open("datasets\WorldBankData\countriesCode.txt", "r") as file:
        data = file.readlines()
        for line in data:
                word = line.split('^^^^^')
  
    for pair in word:
        x, y = pair.split('**')
        countriesMap[y] = x


def TemperatureByCountryWBD(country, dateStart = 1700, dateEnd = 2100):

    global countriesMap
    if not countriesMap:
        __setCountriesMap()

    try:
        country = countriesMap[country]
        df = pd.read_csv(dataPath + country + '.csv', header=1)
    except:
        return 0
    
    df.rename(columns={'Unnamed: 0':'Date'},inplace=True)

    if 'Administrative unit not available' in df.columns:
        df.drop(['Administrative unit not available'], axis=1, inplace=True)
    
    df = df[df['Date'].between(dateStart, dateEnd)]    
    df.reset_index(drop=True , inplace=True)
    return df


def TemperatureByCountriesWBD(countryTuple, dateStart = 1700, dateEnd = 2100):
    
    if isinstance(countryTuple, str):
        return TemperatureByCountryWBD(countryTuple, dateStart, dateEnd)
    
    retdf = pd.DataFrame
    firstIter = True

 
    for country in countryTuple:
        cur_df = TemperatureByCountryWBD(country, dateStart, dateEnd)
        cur_df.drop(cur_df.iloc[:, 2:], inplace = True, axis = 1)

        if firstIter:
            retdf = cur_df
            firstIter = False
        else:
            retdf = retdf.merge(cur_df)
    
    return retdf


df = TemperatureByCountriesWBD(['India', 'United States'])
df.plot(x = 'Date', subplots=True)
plt.show()
print(df)