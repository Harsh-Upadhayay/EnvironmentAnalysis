import pandas as Pd
import numpy as np
import csv
import matplotlib.pyplot as Plt


def get_City_Graph():
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

get_City_Graph()

