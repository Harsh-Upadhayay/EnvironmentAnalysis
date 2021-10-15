This README.txt file was generated on <20210104> by <Yuchuan Lai>


-------------------
GENERAL INFORMATION
-------------------


1. Title of Dataset:

Compiled historical daily temperature and precipitation data for selected 210 U.S. cities



2. Author Information

  First Author Contact Information
        Name: Yuchuan Lai
           Institution: Carnegie Mellon University
           Address: 5000 Forbes Avenue, Pittsburgh PA 15213
           Email: ylai1@andrew.cmu.edu


  Corresponding Author Contact Information
        Name: Yuchuan Lai
           Institution: Carnegie Mellon University
           Address: 5000 Forbes Avenue, Pittsburgh PA 15213
           Email: ylai1@andrew.cmu.edu


  Author Contact Information
           Name: David A. Dzombak
           Institution: Carnegie Mellon University
           Address: 5000 Forbes Avenue, Pittsburgh PA 15213
           Email: dzombak@cmu.edu



---------------------
DATA & FILE OVERVIEW
---------------------

Directory of Files
   A. Filename:        city_info.csv
      Short description:        Names, latitude, longitude, ID (GHCN ID), utilized stations and their periods of records for each city are provided in this file. The ID, latitude, and longitude of each city correspond to its current active weather forecasting station's information. The names of other stations can be found in the Stn.Name column.

        
   B. Filename:        <CITY_ID>.csv
      Short description:       Filenames correspond to the assigned ID for each city for calculation purposes. Daily maximum and minimum temperature (°F) and daily precipitation (in) are provided in each file. NA indicates the data are not available. Note that the daily record may not be a continuous time series - missing values in the Date column -  from the starting of record to the end of record (currently at end of 2019). This is due to the missing data in the station's original records or due to the quality assurance during the production of GHCN-D. Note that the M indicators from original GHCN-D were transferred to NA, T indicators (for traceable amount of precipitation) were transferred to 0, and S indicators were transferred to NA. Jan 2020 update: in the current version of <CITY_ID>.csv files all missing dates with NA values for all climate variables.

       


-----------------------------------------
DATA DESCRIPTION FOR: city_info.csv
-----------------------------------------



1. Number of variables: Date; tmax; tmin; prcp


2. Number of cases/rows: 461


3. Variable List


    A. Name: Name
       Description: names of the cities
Names of the cities may appear multiple times because of different stations and different periods of records from these stations were combined

    B. Name: ID
       Description: GHCN ID
Current active weather forecasting station GHCN ID was assigned to each city

    C. Name: Lat
       Description: latitude
Represents the latitude from the current active weather forecasting station for each city

    D. Name: Lon
       Description: longitude
Represents the longitude from the current active weather forecasting station for each city

    E. Name: stn.name
       Description: the names of each stations
The names of some stations may appear multiple times because the different periods of records may be used for each city

    F. Name: Stn.stDate
       Description: first date of utilized record from the station

    G. Name: Stn.edDate
       Description: last date of utilized record from the station



-----------------------------------------
DATA DESCRIPTION FOR: <CITY_ID>.csv AND <CITY_ID>.fill.csv
-----------------------------------------



1. Number of variables: Date; tmax; tmin; prcp


2. Number of cases/rows: variable


3. Missing data codes: 
        NA       not available


4. Variable List


    A. Name: Date
       Description: dates
		YYYY-MM-DD

    B. Name: tmax
       Description: daily maximum temperature
		Unit: °F

    C. Name: tmin
       Description: daily minimum temperature
		Unit: °F

    D. Name: prcp
       Description: daily precipitation amount
		Unit: in




--------------------------
METHODOLOGICAL INFORMATION
--------------------------

1. The raw daily date were acquired from Applied Climate Information System (ACIS), developed by the NOAA Northeast Regional Climate Center (NRCC). The provided historical daily data in ACIS belongs to Global Historical Climatological Network - daily (GHCN-D) datasets.

2. Historical observations at ACIS can be accessed at: http://scacis.rcc-acis.org/

3. GHCN-D datasets can also be accessed at: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/

4. Selected stations for each city were based on NRCC’s “ThreadEx” project, which combined daily temperature and precipitation extremes at 255 NOAA Local Climatological Locations, representing all large and medium size cities in U.S.

5. Station information for each city can also be accessed at: http://threadex.rcc-acis.org/

6. Date of data collection (approximate range) <20181201 - 20210104>:




