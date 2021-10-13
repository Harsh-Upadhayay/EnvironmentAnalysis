import pandas as Pd
import numpy as Nm
import matplotlib.pyplot as Plt

Dict = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06',
        'July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}

def Get_Analysis_Year(Country = 'India', Month = 'May' , From_Year = '1743-11-01' , To_Year = '2013-01-01'):
    # Reading the CSV File and Stoeing in Datafram 'df'
    File = Pd.read_csv(r'datasets/GlobalLandTemperaturesByCountry.csv')

    # Dropping NAN Values from the Dataframe 'df'
    File.dropna(subset = ['AverageTemperature'] , inplace = True)

    # Making Dataframe of Praticular Country 
    File = File[File['Country'] == Country]

    

    print(File)

Get_Analysis_Year()

#File = Pd.read_csv(r'datasets/GlobalLandTemperaturesByCountry.csv')
#print(File[:3])
#dt1 = '1743-11-01'
#dt2 = '1744-11-01'
#print(File.between_time(dt1,dt2))

