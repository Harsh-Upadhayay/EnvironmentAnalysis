---
marp: true
theme: gaia
paginate: true
---

# Hello
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
└── Precipaitation
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

# Function of Global Module
```py
global.TemperatureByCountry()
```
* Function Description : 

        This Function Takes Tuple of one or more States.\n
        Function takes Particular Month as input.\n
        Function takes Timeframe from given year to given year.\n
        Returns Average Temeperature of States as Pandas Dataframe.


---

```py
global.TemperaturesGlobally()
```
```py
global.TemperaturesByState()
```
```py

```  




