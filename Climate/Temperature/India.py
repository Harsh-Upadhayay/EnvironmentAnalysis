import pandas as Pd
import numpy
import matplotlib.pyplot


def Temperature_Analysis_India(Month = 'May',Start_Year = 1901 , End_Year = 2020):
    """
    # Function Description : 

            Function returns Pandas Datframe of Average Temperature of India for any Particular Month.\n
            You can Select Timeframe from [1901 , 2020].

    # Function Parameters :

            # Month : 

                Full Name of Month is Required.\n
                Months will be as ['January' , 'February' , 'March' , 'April' , 'May',
                                 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December'].
                Default is 'May'.
        
            # Start_Year : 

                Starting Year Parameter. 
                Default is 1901 , you can take any year in range [1901 , 2020]
        
            # End_Year : 

                Ending Year Parameter. 
                Default is 2020, you can take any Year [Start_Year , 2020].
    """
    
    File = Pd.read_csv(r'datasets/Monthly_Max_Temp_IMD-1901_to_2019_0.csv')
    File1 = Pd.read_csv(r'datasets/Monthly_Mean_Temp_IMD-2901_to_2019_0.csv')
    File = File[File.columns[0:13]]
    File1 = File1[File1.columns[0:13]]
    #print(File)
    File.columns = ['Year','January-Max','February-Max','March-Max','April-Max','May-Max','June-Max','July-Max','August-Max',
                    'September-Max','October-Max','November-Max','December-Max']
    File1.columns = ['Year','January-Mean','February-Mean','March-Mean','April-Mean','May-Mean','June-Mean','July-Mean','August-Mean',
                    'September-Mean','October-Mean','November-Mean','December-Mean']
    #print(File)
    File = File[(File['Year'] >= Start_Year) & (File['Year'] <= End_Year)]
    File1 = File1[(File1['Year'] >= Start_Year) & (File['Year'] <= End_Year)]
    File = File[['Year',Month + '-Max']]
    File1 = File1[['Year' , Month + '-Mean']]

    File = File.merge(File1)
    #print(File)
    return File 


# File = Temperature_Analysis_India('September', 1970)
# Mean = File[File.columns[1]].mean()
# File.plot(x = 'Year', color='blue', marker='o', linestyle='dashed',linewidth=2, markersize=12)
# Plt.axhline(y = Mean)
# Plt.title('Maximum Temperature')
# Plt.show()

