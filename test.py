import pandas as pd
import numpy as np
import time
import csv
import matplotlib.pyplot as plt



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


def TemperaturesByState():

    df = pd.read_csv('datasets/GlobalLandTemperaturesByState.csv')
    df.dropna(inplace=True)
    df.sort_values(by=['dt'])

    state = 'West Bengal'
    dateStart = ''
    dateEnd = ''
    month = ['-01-','-02-','-03-','-04-','-05-','-06-','-07-','-08-','-09-','-010-','-011-','-012-']

    df = df[df['State'].str.contains(state)]

    dfJan = df[df['dt'].str.contains(month[0])]
    dfMay = df[df['dt'].str.contains(month[4])]
    dfJan.plot(x = 'dt', y = 'AverageTemperature')
    dfMay.plot(x = 'dt', y = 'AverageTemperature')

    plt.show()
    print(df)



start_time = time.time()

TemperaturesByState()

load_time = time.time() - start_time

print("Load Time : --- %s seconds ---" % (load_time))






