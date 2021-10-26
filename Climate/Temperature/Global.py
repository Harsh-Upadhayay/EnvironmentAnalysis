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



def TemperaturesByState(stateTuple, month, dateStart = '1800-01-01', dateEnd = '2010-01-01'):

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


def TemperaturesByCity(cityTuple, month, dateStart = '1800-01-01', dateEnd = '2010-01-01'):

    if isinstance(cityTuple, str):
        cityTuple = (cityTuple,)

    df = pd.read_csv('datasets/GlobalLandTemperaturesByMajorCity.csv')
    
    df.dropna(inplace=True)
    df.sort_values(by=['dt'], inplace=True)
    df = df[df['dt'].between(dateStart, dateEnd)]

    for city in cityTuple:
        dftemp = df[df['City'].str.contains(city)]
        if dftemp.empty :
            return TemperaturesBySpecificCity(cityTuple, month, dateStart, dateEnd)    

    retdf = pd.DataFrame
    firstIter = True

    for city in cityTuple:
        cur_df = df[df['City'].str.contains(city)]
        cur_df = cur_df[cur_df['dt'].str.contains(months[month])]
        
        cur_df.drop(cur_df.columns[[2, 3, 4, 5, 6]], axis=1, inplace=True)
        cur_df.rename(columns={'AverageTemperature' : city}, inplace=True)

        if firstIter:
            retdf = cur_df
            firstIter = False
        else:
            retdf = retdf.merge(cur_df)

    return retdf


def TemperaturesBySpecificCity(cityTuple, month, dateStart = '1800-01-01', dateEnd = '2010-01-01'):

    if isinstance(cityTuple, str):
        cityTuple = (cityTuple,)

    df = pd.read_csv('datasets/GlobalLandTemperaturesByCity.csv')
    df.dropna(inplace=True)
    df.sort_values(by=['dt'], inplace=True)

    retdf = pd.DataFrame
    firstIter = True

    for city in cityTuple:
        cur_df = df[df['City'].str.contains(city)]
        cur_df = cur_df[cur_df['dt'].str.contains(months[month])]
        
        cur_df.drop(cur_df.columns[[2, 3, 4, 5, 6]], axis=1, inplace=True)
        cur_df.rename(columns={'AverageTemperature' : city}, inplace=True)

        if firstIter:
            retdf = cur_df
            firstIter = False
        else:
            retdf = retdf.merge(cur_df)

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


Dict = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06',
        'July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}


def TemperatureByCountry(Country ,  Month = 'May' , From_Date = '1743-11-01' , To_Date = '2013-01-01'):

   
    if isinstance(Country , str):
        Country = [Country,]
    
    File = pd.read_csv(r'datasets/GlobalLandTemperaturesByCountry.csv')

    File.columns = ['Date' , 'Avg_Temperature' , 'Avg_Uncertainity','Country']

    File.dropna(subset = ['Avg_Temperature'] , inplace = True)

    File = File[File['Date'].between(From_Date,To_Date)]

    File = File[File['Date'].str.contains(Dict[Month])]

    File.reset_index(drop = True , inplace = True)
    
    New = pd.DataFrame
    Flag = 1

    for Ptr in Country:
        NewFile = File[File['Country'] == Ptr]

        NewFile = NewFile.drop(['Avg_Uncertainity','Country'],axis = 1)
        NewFile = NewFile.rename(columns = {'Avg_Temperature':Ptr})
        
        if(Flag == 1):
            New = NewFile
            Flag = 0
        else:
            #New = New.merge(NewFile)
            New = New.merge(NewFile)
    return New


def get_City_Graph_By_CSV():
    City = input("Enter the City : ")
    print()
    Month = input("Enter the Month : ")
    Dict = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06',
            'July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
    with open('datasets/GlobalLandTemperaturesByMajorCity.csv') as File:
        File_Ptr = csv.reader(File)
        Flag,Citycount,monthCount = 0,0,0
        Year,Temp = [],[]
        for Lst in File_Ptr:
            if Flag == 0:
                print("Data for City ",City,"for Month ",Month,'is Give below')
                Flag = 1
            else:
                if(City == Lst[3]):
                    Str = Lst[0]
                    Str1 = Dict[Month]
                    if(Str1 == Str[5:7]):
                        if(Lst[1] != ""):
                            Year.append(int(Str[:4]))
                            Temp.append(float(Lst[1]))
                            print("Date = ",Lst[0], "Avg_Temperature = ",Lst[1])
                            monthCount = monthCount + 1
                    Citycount = Citycount + 1
                    print(1)
    File.close()
    print("Total Data of ",City , "is ",Citycount)
    print("Total Data for ",Month , "is",monthCount)
    Plt.plot(Year , Temp ,linewidth = 2,markersize = 12)
    Plt.show()


def get_Temperature_Graph_By_CSV():
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
                            print("Date = ",Lst[0]," : Average_Temperature = ",Lst[1]," : Uncertainty = ",Lst[2]," : Country = ",Lst[3])
                            Cmonth = Cmonth + 1
                    Count = Count + 1
        print("Total Data of Month ",Month, "is ",Cmonth)
        print("Total Data of ",Country,"is ",Count)
    File.close()

    plt.plot(Year, Avg_Temperature, 'go--', linewidth = 2, markersize = 8)
    plt.show()








