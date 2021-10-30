import pandas as Pd
import numpy as np
import matplotlib.pyplot as Plt


def Temperature_Analysis_India(Month = 'May',Start_Year = 1901 , End_Year = 2020):
    """
    * Function Description : 

            Function returns Pandas Datframe of India for given Month.
            You can start from year >= 1901 to any year <= 2020.

    * Function Parameters :

            Month : 

                Full Name of Month is Required.
                Months will be as ['January' , 'February' , 'March' , 'April' , 'May',
                                 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December'].
                Default is 'May'.
        
            Start_Year : 

                Starting Year Parameter. 
                Default is 1901 , you can take any year in range [1901 , 2020]
        
            End_Year : 

                Ending Year Parameter. 
                Default is 2020, you can take any Year [Start_Year , 2020].
    """
    File = Pd.read_csv(r'datasets/Monthly_Max_Temp_IMD-1901_to_2019_0.csv')
    File = File[File.columns[0:13]]
    #print(File)
    File.columns = ['Year','January','February','March','April','May','June','July','August',
                    'September','October','November','December']
    #print(File)
    File = File[(File['Year'] >= Start_Year) & (File['Year'] <= End_Year)]
    File = File[['Year',Month]]
    #print(File)
    return File 


# File = Temperature_Analysis_India('September', 1970)
# Mean = File[File.columns[1]].mean()
# File.plot(x = 'Year', color='blue', marker='o', linestyle='dashed',linewidth=2, markersize=12)
# Plt.axhline(y = Mean)
# Plt.title('Maximum Temperature')
# Plt.show()

