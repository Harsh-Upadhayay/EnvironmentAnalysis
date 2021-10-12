from typing import DefaultDict
import pandas as pd
import numpy as np
import time
import csv
import matplotlib.pyplot as plt


months = {'January':'-01-', 'February':'-02-', 'March'    :'-03-',
          'April'  :'-04-', 'May'     :'-05-', 'June'     :'-06-',
          'July'   :'-07-', 'August'  :'-08-', 'September':'-09-',
          'October':'-10-', 'November':'-11-', 'December' :'-12-'}



def get_Temperature_Graph():
    Country = input("Enter the Country : ")
    print()
    Month = input("Enter the Month : ")

    Dict = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06',
            'July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
    with open('datasets/GlobalLandTemperaturesByCountry.csv') as File:
        File_Ptr = csv.reader(File)
        Count , Cmonth = 0,0
        Year , Avg_Temperature = [],[]
        for Lst in File_Ptr:
            if Count == 0:
                print("Data for the Month",Month, "is given below")
                Count = 1
            else:
                Str = Lst[0]
                if(Lst[3] == Country):
                    Month_Code = Dict[Month]
                    if(Str[5:7] == Month_Code):
                        if(Lst[1] != ""):
                            Year.append(int(Str[:4]))
                            Avg_Temperature.append(float(Lst[1]))
                            print("Date = ",Lst[0]," : Average_Temerature = ",Lst[1]," : Unceratinity = ",Lst[2]," : Country = ",Lst[3])
                            Cmonth = Cmonth + 1
                    Count = Count + 1
        print("Total Data of Month ",Month, "is ",Cmonth)
        print("Total Data of ",Country,"is ",Count)
    File.close()

    plt.plot(Year, Avg_Temperature, 'go--', linewidth = 2, markersize = 8)
    plt.show()


def TemperaturesByState(month, stateTuple, dateStart = '1800-01-01', dateEnd = '2010-01-01'):

    if isinstance(stateTuple, str):
        stateTuple = (stateTuple,)

    df = pd.read_csv('datasets/GlobalLandTemperaturesByState.csv')
    df.dropna(inplace=True)
    df.sort_values(by=['dt'], inplace=True)
    df = df[df['dt'].between(dateStart, dateEnd)]

    retdf = pd.DataFrame
    firstIter = True

    for state in stateTuple:
        cur_df = df[df['State'].str.contains(state)]
        cur_df = cur_df[cur_df['dt'].str.contains(months[month])]
        
        cur_df.drop(cur_df.columns[[2, 3, 4]], axis=1, inplace=True)
        cur_df.rename(columns={'AverageTemperature' : state}, inplace=True)

        if firstIter:
            retdf = cur_df
            firstIter = False
        else:
            retdf = retdf.merge(cur_df)

    return retdf


def TemperaturesByCity(city, month, dateStart = '1800-01-01', dateEnd = '2010-01-01'):

    df = pd.read_csv('datasets/GlobalLandTemperaturesByMajorCity.csv')
    df.dropna(inplace=True)
    df.sort_values(by=['dt'], inplace=True)

    df = df[df['City'].str.contains(city)]
    df = df[df['dt'].between(dateStart, dateEnd)]

    if df.empty :
        return TemperaturesBySpecificCity(city, month, dateStart, dateEnd)

    df = df[df['dt'].str.contains(months[month])]


    return df


def TemperaturesBySpecificCity(city, month, dateStart = '1800-01-01', dateEnd = '2010-01-01'):

    df = pd.read_csv('datasets/GlobalLandTemperaturesByCity.csv')
    df.dropna(inplace=True)
    df.sort_values(by=['dt'], inplace=True)

    retdf = df[df['City'].str.contains(city)]
    retdf = retdf[retdf['dt'].between(dateStart, dateEnd)]
    retdf = retdf[retdf['dt'].str.contains(months[month])]
    
    return retdf


def TemperaturesGlobally(month, dateStart = '1800-01-01', dateEnd = '2010-01-01'):

    df = pd.read_csv('datasets/GlobalTemperatures.csv')
    df.dropna(inplace=True)
    df.sort_values(by=['dt'], inplace=True)
    
    df = df[df['dt'].between(dateStart, dateEnd)]

    df = df[df['dt'].str.contains(months[month])]
    # df.plot()
    
    # plt.yticks([10,20,30,40,50,60,70])
    # plt.show()
    # print(df)
    return df





start_time = time.time()

# df = pd.read_csv('datasets/GlobalLandTemperaturesByState.csv')
# df = df[df['Country'].str.contains('India')]
# print(df.State.unique())

df = TemperaturesByState('June', ['Rajasthan', 'Uttraanchal'])
df.plot(x = 'dt')
plt.show()
print(df)

print("Load Time : --- %s seconds ---" % (time.time() - start_time))






