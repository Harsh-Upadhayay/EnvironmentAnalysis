import Climate.Temperature.GlobalWBD  as globalWBD
import Climate.Temperature.Global  as globalKaggle
import Climate.Temperature.USA as USA
import Climate.Temperature.India as India

import matplotlib.pyplot as plt


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

# globalKaggle.TemperatureByCountry(['Russia', 'United Kingdom'], Month='February', To_Date='1989').plot(x = 'Date')
# globalKaggle.TemperaturesByCity(["Delhi", "Bombay"], 'January', dateStart='1900').plot(x = 'Date')
# globalKaggle.TemperaturesByState(["Delhi", 'Bihar'],).plot(x = 'Date')
# plt.show()

# print("India : ")

#India.Temperature_Analysis_India('January').plot(x = 'Year')
#Df = globalKaggle.get_City_Graph_By_CSV(['Delhi','Nagpur','Bombay'],'June')
#Df = globalKaggle.get_Temperature_Graph_By_CSV()
#print(Df)
#print(globalKaggle.TemperatureByCountry())
#plt.show()