import Climate.Temperature.GlobalWBD  as globalWBD
import Climate.Temperature.Global  as globalKaggle
import Climate.Temperature.USA as USA
import Climate.Temperature.India as India

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

# print("GlobalWBD : ")

# globalWBD.TemperatureByCountriesWBD(['India', 'China', 'Russia', 'United Kingdom'], dateEnd=1950).plot(x = 'Date')
# globalWBD.TemperatureByCountryWBD('United Kingdom', dateEnd=1950).plot(x = 'Date')
# globalWBD.TemperatureByStateWBD('India', ['Goa', 'Delhi'], dateEnd=1950).plot(x = 'Date')
# plt.show()

# print("USA : ")

# USA.TemperatureAnalysisUS().cityAnalysis('NewYork', 'June', '01', dateEnd='2001').plot(x = 'Date')
# USA.TemperatureAnalysisUS().citiesAnalysis(['NewYork', 'Seattle'], 'June', '01', dateEnd='2001').plot(x = 'Date')
# plt.show()

# print("Global : ")

#Df = globalKaggle.TemperatureByCountry(['Russia', 'United Kingdom'], Month='February', To_Date='1989')
# globalKaggle.TemperaturesByCity(["Delhi", "Bombay"], 'January', dateStart='1900').plot(x = 'Date')
# globalKaggle.TemperaturesByState(["Delhi", 'Bihar'],).plot(x = 'Date')
# plt.show()

# print("India : ")

Df = India.Temperature_Analysis_India('January')
#Df = globalKaggle.get_City_Graph_By_CSV(['Delhi','Nagpur','Bombay'],'June')
#Df = globalKaggle.get_Temperature_Graph_By_CSV()
#print(Df)
#print(globalKaggle.TemperatureByCountry())
#plt.show()

print(Df)
PLt = Df.plot( x = 'Year', linestyle = 'dashed',linewidth = 2, subplots = True,
                        title = 'Average Temperatures' ,ylabel = 'Temperature in Degree celsius')

Count = 1
for Plot in PLt:
    Arr = np.array([list(Df['Year']) , list(Df[Df.columns[Count]])])
    #print(Arr[0])
    #print(Arr[1])
    Mean = Df[Df.columns[Count]].mean()
    #print(Mean)
    y_mean = [Mean]*len(Arr[0])
    Arr[1].astype(np.float)
    Smoothed = savgol_filter(Arr[1] , window_length= 47 , polyorder = 2 , mode = 'interp')
    #print(Smoothed)
    Plot.plot(Arr[0], Smoothed , color='green',label = 'Smoothed')
    #y_mean = [np.mean(Arr[1],dtype = float)]*len(Arr[0])
    #print(y_mean)
    Plot.plot(Arr[0] , y_mean , label = 'Mean', color = 'orange')
    legend = Plot.legend(loc='upper right')
    Count = Count + 1
plt.show()