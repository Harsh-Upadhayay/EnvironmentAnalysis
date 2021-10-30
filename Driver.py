import Climate.Temperature.GlobalWBD  as globalWBD
import Climate.Temperature.Global  as golbalKaggle
import Climate.Temperature.USA as USA
import Climate.Temperature.India as India

import matplotlib.pyplot as plt




df = golbalKaggle.TemperaturesByState('Uttar Pradesh', 'January')
df.plot('dt')

plt.show()
print(df)


'''
import Climate.Temperature.India as Analyze
import Climate.Precipitation.Rainfall_Analysis as B
import matplotlib.pyplot as Plt

import Climate.Temperature.Global as C
'''


#df = Analyze.Temperature_Analysis_India()
#df1 = B.Analyse_Rain_Countries()
#df2 = B.Analyse_Rain_State()

#df3 = C.TemperatureByCountry()
#df4 = C.TemperaturesByCity()

#df5 = C.TemperaturesBySpecificCity()
#df6 = C.TemperaturesByState()

#df7 = C.TemperaturesGlobally()

#Year , Temp = C.get_City_Graph_By_CSV()
#Year , Temp = C.get_Temperature_Graph_By_CSV()

#Plt.plot(Year , Temp)

#df1.plot(x = 'Year')
#df.plot(x = 'Year')
#Plt.show()