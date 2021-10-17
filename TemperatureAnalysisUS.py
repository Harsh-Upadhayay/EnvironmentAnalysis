import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months = {'January':'-01-', 'February':'-02-', 'March'    :'-03-',
          'April'  :'-04-', 'May'     :'-05-', 'June'     :'-06-',
          'July'   :'-07-', 'August'  :'-08-', 'September':'-09-',
          'October':'-10-', 'November':'-11-', 'December' :'-12-'}

dataPath = 'datasets/USdata/'
citiesMap = 0


def __setcitiesMap():
    """
    Call only Once
    """
    global citiesMap
    df = pd.read_csv(dataPath+'city_info.csv')
    df.drop(columns=['Stn.Name', 'Stn.stDate', 'Stn.edDate', 'Unnamed: 0'], inplace=True)
    citiesMap = df.set_index('Name')['ID'].to_dict()


def TemperaturesByUScity(city, month = 0, day = 0, dateStart = '1700-01-01', dateEnd = '2010-01-01'):

    global citiesMap
    
    if 0 == citiesMap:
        __setcitiesMap()

    df = pd.read_csv(dataPath + citiesMap[city] + '.csv')
    df.drop(columns='Unnamed: 0', inplace=True)
    df = df[df['Date'].between(dateStart, dateEnd)]
    
    if month:
        df = df[df['Date'].str.contains(months[month])]
    
    if day:
        df = df[df['Date'].str.contains('.-'+str(day),  regex=True)]
    
    return df


def TemperaturesByUScities(cityTuple, month, day = 0, dateStart = '1700-01-01', dateEnd = '2010-01-01'):
    
    if isinstance(cityTuple, str):
        return TemperaturesByUScity(cityTuple, month, day, dateStart, dateEnd)
    
    retdf = pd.DataFrame
    firstIter = True

 
    for city in cityTuple:
        cur_df = TemperaturesByUScity(city, month, day, dateStart, dateEnd)
        cur_df[city] = cur_df[['tmin', 'tmax']].mean(axis=1)
        cur_df.drop(cur_df.columns[[1,2,3]], axis=1, inplace=True)
           
        if firstIter:
            retdf = cur_df
            firstIter = False
        else:
            retdf = retdf.merge(cur_df, how='outer')
    
    return retdf




df = TemperaturesByUScities(['NewYork', 'Wausau'], 'June', '01')

df.plot(x='Date')
plt.show()
print(df)