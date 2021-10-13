import pandas as Pd
import numpy as Nm
import matplotlib.pyplot as Plt

Dict = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06',
        'July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}

def Get_Analysis_Country(Country ,  Month = 'May' , From_Date = '1743-11-01' , To_Date = '2013-01-01'):

   
    if isinstance(Country , str):
        Country = [Country,]
    
    File = Pd.read_csv(r'datasets/GlobalLandTemperaturesByCountry.csv')

    File.columns = ['Date' , 'Avg_Temperature' , 'Avg_Uncertainity','Country']

    File.dropna(subset = ['Avg_Temperature'] , inplace = True)

    File = File[File['Date'].between(From_Date,To_Date)]

    File = File[File['Date'].str.contains(Dict[Month])]

    File.reset_index(drop = True , inplace = True)
    
    New = Pd.DataFrame
    Flag = 1

    for Ptr in Country:
        NewFile = File[File['Country'] == Ptr]

        NewFile = NewFile.drop(['Avg_Uncertainity','Country'],axis = 1)
        NewFile = NewFile.rename(columns = {'Avg_Temperature':Ptr})
        
        if(Flag == 1):
            New = NewFile
            Flag = 0
        else:
            New = New.merge(NewFile)
    return New



    
File1 = Get_Analysis_Country(['India','China','Russia'])
print(File1)

x = list(File1['Date'].str[:4])
print(x)

File1.plot(x = File1['Date'],subplots = True)
Plt.show()
