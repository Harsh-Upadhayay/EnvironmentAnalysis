import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

countriesMap = {}
dataPath = 'datasets/WhoDataBank/tas_timeseries_annual_cru_1901-2020_'
months = {'January':'-01-', 'February':'-02-', 'March'    :'-03-',
          'April'  :'-04-', 'May'     :'-05-', 'June'     :'-06-',
          'July'   :'-07-', 'August'  :'-08-', 'September':'-09-',
          'October':'-10-', 'November':'-11-', 'December' :'-12-'}


def __setCountriesMap():
    """
    Call only once
    """
    global CountriesMap
    with open("datasets\WhoDataBank\countriesCode.txt", "r") as file:
        data = file.readlines()
        for line in data:
                word = line.split('^^^^^')
  
    for pair in word:
        x, y = pair.split('**')
        countriesMap[y] = x


def TemperaturesWhoCountries(country, dateStart = '1700', dateEnd = '2100'):

    global citiesMap
    if not countriesMap:
        __setCountriesMap()

    try:
        df = pd.read_csv(dataPath + countriesMap[country] + '.csv')
    except:
        return 0
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df['Date'] = df.index
    df = df.reset_index(drop=True)
    return df


# def TemperaturesByUScities(cityTuple, month, day = 0, dateStart = '1700-01-01', dateEnd = '2010-01-01'):
    
#     if isinstance(cityTuple, str):
#         return TemperaturesByUScity(cityTuple, month, day, dateStart, dateEnd)
    
#     retdf = pd.DataFrame
#     firstIter = True

 
#     for city in cityTuple:
#         cur_df = TemperaturesByUScity(city, month, day, dateStart, dateEnd)
#         cur_df[city] = cur_df[['tmin', 'tmax']].mean(axis=1)
#         cur_df.drop(cur_df.columns[[1,2,3]], axis=1, inplace=True)
           
#         if firstIter:
#             retdf = cur_df
#             firstIter = False
#         else:
#             retdf = retdf.merge(cur_df, how='outer')
    
#     return retdf


df = TemperaturesWhoCountries('Aruba')
df.plot( x = 'Date')
plt.show()
print(df)