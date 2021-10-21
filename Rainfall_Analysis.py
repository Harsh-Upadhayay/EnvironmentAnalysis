from numpy.core.fromnumeric import cumsum
import pandas as Pd
import numpy as np
import matplotlib.pyplot as Plt

Dict = {}

def __setCountriesMap():
    """
    Call only once
    """
    global Dict
    with open("datasets\WorldBankData\countriesCode.txt", "r") as file:
        data = file.readlines()
        for line in data:
                word = line.split('^^^^^')
  
    for pair in word:
        x, y = pair.split('**')
        Dict[y] = x



def Analyse_Rain_Countries(Country = ['India','China'],Start_Year = 1901 , End_Year = 2020):
    
    global citiesMap
    if not Dict:
        __setCountriesMap()

    Flag = 0
    Frame = Pd.DataFrame
    for country in Country:

        # Reading the Csv File
        File = Pd.read_csv(r'datasets/Precipitation_Datasets/pr_timeseries_annual_cru_1901-2020_' + str(Dict[country])  + '.csv',header= 1)
        
        #File.drop(labels = 'Variable:',axis = 0,inplace= True)
        #File = File.truncate(before = 1901 , after=2020)
        #File = File.drop(columns=File.index[0])
        File.rename(columns={'Unnamed: 0':'Year'},inplace=True)  # Setting unnamed column as Year
        
        File = File[(File['Year'] >= Start_Year) & (File['Year'] <= End_Year)]   # Taking data between given years
        File = File[['Year',country]]   # Dataframe for country along year
        File.reset_index(drop=True , inplace=True)

        if(Flag == 0):
            Frame = File
            Flag = 1
        else:
            Frame = Frame.merge(File)

    return Frame



File = Analyse_Rain_Countries(['India','China'],1901 ,2020)

#print(File.columns)


File.plot( x = 'Year', color='blue', marker = 'o', linestyle = 'dashed',linewidth = 2,markersize = 12,
            subplots = True ,title = 'Annual Rainfall in MM',figsize = (15,15),ylabel = 'Rainfall in MM')

#Avg = File[File.columns[1]].mean()
#Plt.axhline(y = Avg)
#Avg1 = File[File.columns[2]].mean()
#Plt.axhline(y = Avg1)
#Plt.title('Annual Rainfall in MM')

Plt.show()