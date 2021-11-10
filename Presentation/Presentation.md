---
marp: true
theme: uncover
paginate: true
image :
---
# Climate Analysis portal

+ This Portal Analyzes the Change in Tmeperture and Rainfall Patterns of World , Countries , States , Cities.Also Compare them.

---
# Github
One Can Use Portal on Your system . Program is uploaded in github

You can go to Github [Github_Repository](https://github.com/Harsh-Upadhayay/EnviornmentAnalysis)

---
# Datsets 

+ Data is Taken from different Sources 
    * [Climate_KnoledePorta_Dataset](https://climateknowledgeportal.worldbank.org/watershed/161/climate-data-historical)
    * [Kaggle_Dataset](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalLandTemperaturesByCity.csv)
    * [Data_GOI](https://data.gov.in/catalog/rainfall-india?filters%5Bfield_catalog_reference%5D=1090541&format=json&offset=0&limit=6&sort%5Bcreated%5D=desc)
    * [USA_Dataset](https://kilthub.cmu.edu/articles/dataset/Compiled_daily_temperature_and_precipitation_data_for_the_U_S_cities/7890488?file=25951292)




---

# Module Climate
## Hierarchy is as  shown 

```
Climate
├── Temperature
│   ├── Global.py
│   ├── GlobalWBD.py
│   ├── India.py
│   └── USA.py
└── Precipitation
    └── Rainfall_Analysis
```

---

# Calling Module

```py
import Climate
```
+ Climate Module Contains
    * Temperature module
    * Precipitation Module
---

# Calling Temperature module from Climate

```py
import Climate.Temperature
```
+ Temperature module contains 
    * Global Module 
    * GlobalWBD Module
    * India Module
    * USA Module
---

# From Temperature Module Importing Global Module
```py
import Climate.Temperature.Global as global
```
+ This Module contains 6 Functions

---



* Function of Global Module
```py
import Climate.Temperature.Global as global
global.TemperatureByCountry()
```
![width:1100px height:420px](2021-11-09-23-23-07.png)


---

* Function of Global Module
```py
import Climate.Temperature.Global as global
global.TemperaturesGlobally()
```
![width:1100px height:420px](2021-11-10-08-01-38.png)




---

* Function of Global Module
```py
import Climate.Temperature.Global as global
global.TemperaturesByState()
```
![width:1100px height:400px](2021-11-10-08-04-16.png)




---

* Function of Global Module

```py
import Climate.Temperature.Global as global
global.TemperaturesByCity()
```  
![width:1100px height:420px](2021-11-10-08-16-05.png)


---



* Function of Global Module
```py
import Climate.Temperature.Global as global
global.TemperaturesBySpecificCity()
```
![width:1100px height:420px](2021-11-10-08-36-08.png)

---




* Function of Global Module
```py
import Climate.Temperature.Global as global
global.get_City_Graph_By_CSV()
```
![width:1100px height:420px](2021-11-10-08-37-57.png)

---




* Function of Global Module
```py
import Climate.Temperature.Global as global
global.get_Temperature_Graph_By_CSV()
```
![width:1100px height:420px](2021-11-10-08-40-25.png)

---




# From Temperature importing GlobalWBD

```py
import Climate.Temperature.GlobalWBD as globaWBD
```

* This Module Contains 3 Functions

---




* Function of GlobalWBD Module
```py
import Climate.Temperature.GlobalWBD as globaWBD
globalWBD.TemperatureByCountryWBD()
```
![width:1100px height:420px](2021-11-10-08-48-20.png)

---




* Function of GlobalWBD Module
```py
import Climate.Temperature.GlobalWBD as globaWBD
globalWBD.TemperatureByCountriesWBD()
```
![width:1100px height:420px](2021-11-10-08-51-28.png)

---




* Function of GlobalWBD Module
```py
import Climate.Temperature.GlobalWBD as globaWBD
globalWBD.TemperatureByStateWBD()
```
![width:1100px height:420px](2021-11-10-08-54-33.png)

---




# From Temperature importing India Module

```py
import Climate.Temperature.India as india
```
* This Module contains 1 Function

---

* Function of India
```py
import Climate.Temperature.India as india
india.Temperature_Analysis_India()
```

![width:1100px height:420px](2021-11-10-08-59-51.png)

---




# From Temperature Importing USA Module

```py
import Climate.Temperature.USA as usa
```

* This Module Conatins 2 Functions

---





* Function of USA

```py
import Climate.Temperature.USA as usa
usa.cityAnalysis()
```
![width:1100px height:420px](2021-11-10-09-36-13.png)

---



* Function of USA 

```py
import Climate.Temperature.USA as usa
usa.citiesAnalysis()
```

![width:1100px height:420px](2021-11-10-09-38-17.png)

---



# Calling Precipitation Module from Temperature

```py
import Climate.Precipitation
```
+ This Module Contains 
    * Rainfall_Analyisis Module

---



* Function of Precipitation

```py
import Climate.Precipitation.Rainfall_Analysis as Rain
Rain.Analyse_Rain_Countries()
```

![width:1100px height:420px](2021-11-10-09-46-26.png)

---




* Function of Precipitation

```py
import Climate.Precipitation.Rainfall_Analysis as Rain
Rain.Analyse_Rain_State()
```
![width:1100px height:420px](2021-11-10-09-49-10.png)





---
# Module GUI

+ Interface of Climate Portal is Hosted by Tkinter
+ Module GUI Contains
    + Interface of Modules of Temperature
    + Interface of Modules of Precipitation

---

# Hierarchy of GUI Module

```
GUI
├── interfaceGlobal.py
├── interfaceIndai.py
├── interfaceRain/py
├── interfaceUSA.py
├── interfaceWBD.py
├── Smooth_Rainfall.py
└── Smooth_Temperature.py

```

---

# Working with tkinter

+ Function interface.py




