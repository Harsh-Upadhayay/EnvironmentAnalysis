import pandas as pd
import numpy as np
import time
import csv
import matplotlib.pyplot as Plt

start_time = time.time()

with open('GlobalLandTemperaturesByCountry.csv') as File:
    File_Ptr = csv.reader(File)
    Count = 0
    CMay = 0
    Year = []
    Avg_Temperature = []
    for Lst in File_Ptr:
        if Count == 0:
            print("Data for the Month May is given below")
            Count = 1
        else:
            Str = Lst[0]
            if(Lst[3] == 'India'):
    
                if(Str[5:7] == '05'):
                    if(Lst[1] != ""):
                        Year.append(int(Str[:4]))
                        Avg_Temperature.append(float(Lst[1]))
                        print("Date = ",Lst[0]," : Average_Temerature = ",Lst[1]," : Unceratinity = ",Lst[2]," : Country = ",Lst[3])
                        CMay = CMay + 1
                Count = Count + 1
    print("Total Data of Month May is ",CMay)
    print("Total Data of India is ",Count)
File.close()

Plt.plot(Year,Avg_Temperature,'-g')
Plt.show()
#print(Year)



load_time = time.time() - start_time

print("Load Time : --- %s seconds ---" % (load_time))

