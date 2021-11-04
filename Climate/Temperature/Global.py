from typing import DefaultDict
import pandas as pd
import numpy as np
import time
import csv
import matplotlib.pyplot as plt


months = {'January':'-01-', 'February':'-02-', 'March'    :'-03-',
          'April'  :'-04-', 'May'     :'-05-', 'June'     :'-06-',
          'July'   :'-07-', 'August'  :'-08-', 'September':'-09-',
          'October':'-10-', 'November':'-11-', 'December' :'-12-'}



def TemperaturesByState(stateTuple = ('Uttar Pradesh','Bihar'), month = 'May', dateStart = '1800-01-01', dateEnd = '2010-01-01'):
    """
    # Function Description : 

        This Function Takes Tuple of one or more States.\n
        Function takes Particular Month as input.\n
        Function takes Timeframe from given year to given year.\n
        Returns Average Temeperature of States as Pandas Dataframe.

    # Function Parameters : 

            # stateTuple : 

                    This Parameter takes Tuple of States as Input.\n
                    Default is ('Uttar Pradesh' , 'Bihar').

            # month : 

                    This Parameter takes Full Name of Month.\n
                    Default is 'May'.

            # dateStart : 

                    This Parameter takes Starting date of Dataset.\n
                    Default is '1800-01-01'.

            # dateEnd : 

                    This Parameter takes Ending date of Dataset.\n
                    Default is '2010-01-01'.

    """

    if isinstance(stateTuple, str):
        stateTuple = (stateTuple,)

    df = pd.read_csv('datasets/GlobalLandTemperaturesByState.csv')
    df.dropna(inplace=True)
    df.sort_values(by=['dt'], inplace=True)
    df = df[df['dt'].between(dateStart, dateEnd)]

    retdf = pd.DataFrame
    firstIter = True

    for state in stateTuple:
        cur_df = df[df['State'].str.contains(state)]
        cur_df = cur_df[cur_df['dt'].str.contains(months[month])]
        
        cur_df.drop(cur_df.columns[[2, 3, 4]], axis=1, inplace=True)
        cur_df.rename(columns={'AverageTemperature' : state}, inplace=True)

        if firstIter:
            retdf = cur_df
            firstIter = False
        else:
            retdf = retdf.merge(cur_df)

    retdf.rename(columns={'dt' : 'Date'}, inplace=True)
    return retdf


def TemperaturesByCity(cityTuple = ('Delhi' , 'Nagpur'), month = 'May', dateStart = '1800-01-01', dateEnd = '2010-01-01'):

    """
    # Function Description : 
        
        **Dataset used is of 22 mb so execution is faster.**
        This Function will take Tuple of City Names.  
        Function will take month Name as Input.  
        Function will take starting date of Dataset.  
        Function will take ending date of Dataset.  
        Returns Average Temperature of Cities as Pandas Dataframe.  

    # Function Parameters : 

            # cityTuple : 

                    This Parameter takes tuple of one or more cities.  
                    Default is 

            # month : 

                    This Parameter takes Full Name of Month.  
                    Default is 'May'.
            
            # dateStart : 

                    This Parameter takes Starting date of Dataset.  
                    Default is '1800-01-01'.

            # dateEnd : 

                    This Parameter takes Ending date of Dataset.  
                    Default is '2010-01-01'.
    """

    if isinstance(cityTuple, str):
        cityTuple = (cityTuple,)

    df = pd.read_csv('datasets/GlobalLandTemperaturesByMajorCity.csv')
    
    df.dropna(inplace=True)
    df.sort_values(by=['dt'], inplace=True)
    df = df[df['dt'].between(dateStart, dateEnd)]

    for city in cityTuple:
        dftemp = df[df['City'].str.contains(city)]
        if dftemp.empty :
            return TemperaturesBySpecificCity(cityTuple, month, dateStart, dateEnd)    

    retdf = pd.DataFrame
    firstIter = True

    for city in cityTuple:
        cur_df = df[df['City'].str.contains(city)]
        cur_df = cur_df[cur_df['dt'].str.contains(months[month])]
        
        cur_df.drop(cur_df.columns[[2, 3, 4, 5, 6]], axis=1, inplace=True)
        cur_df.rename(columns={'AverageTemperature' : city}, inplace=True)

        if firstIter:
            retdf = cur_df
            firstIter = False
        else:
            retdf = retdf.merge(cur_df)

    retdf.rename(columns={'dt' : 'Date'}, inplace=True)
    return retdf


def TemperaturesBySpecificCity(cityTuple, month, dateStart = '1800-01-01', dateEnd = '2010-01-01'):

    """
    # Function Description : 

        **Dataset used is of 550 mb so execution is significantly slower.**\n  
        This Function will take Tuple of City Names.\n
        Function will take month Name as Input.\n
        Function will take starting date of Dataset.\n
        Function will take ending date of Dataset.\n
        Returns Average Temperatures of Specific Cities as Pandas Dataframe.

    # Function Parameters : 

            # cityTuple : 

                    This Parameter takes tuple of one or more cities.\n
                    Default is 

            # month : 

                    This Parameter takes Full Name of Month.\n
                    Default is 'May'.
            
            # dateStart : 

                    This Parameter takes Starting date of Dataset.\n
                    Default is '1800-01-01'.

            # dateEnd : 

                    This Parameter takes Ending date of Dataset.\n
                    Default is '2010-01-01'.
    """

    if isinstance(cityTuple, str):
        cityTuple = (cityTuple,)

    df = pd.read_csv('datasets/GlobalLandTemperaturesByCity.csv')
    df.dropna(inplace=True)
    df.sort_values(by=['dt'], inplace=True)

    retdf = pd.DataFrame
    firstIter = True

    for city in cityTuple:
        cur_df = df[df['City'].str.contains(city)]
        cur_df = cur_df[cur_df['dt'].str.contains(months[month])]
        
        cur_df.drop(cur_df.columns[[2, 3, 4, 5, 6]], axis=1, inplace=True)
        cur_df.rename(columns={'AverageTemperature' : city}, inplace=True)

        if firstIter:
            retdf = cur_df
            firstIter = False
        else:
            retdf = retdf.merge(cur_df)

    retdf.rename(columns={'dt' : 'Date'}, inplace=True)
    return retdf


def TemperaturesGlobally(month = 'May', dateStart = '1800-01-01', dateEnd = '2010-01-01'):

    """
    # Function Description : 
        
        This Function Takes Particular Month of a Year.\n
        Function takes Timeframe(dateStart , dateEnd).\n
        Returns Global Average Temperature as Pandas Dataframe.

    # Function Parameters : 

            # month : 

                    This Parameter takes Full Name of Month.\n
                    Default is 'May'.
            
            # dateStart : 

                    This Parameter takes Starting date of Dataset.\n
                    Default is '1800-01-01'.

            # dateEnd : 

                    This Parameter takes Ending date of Dataset.\n
                    Default is '2010-01-01'.
    """

    df = pd.read_csv('datasets/GlobalTemperatures.csv')
    df.dropna(inplace=True)
    df.sort_values(by=['dt'], inplace=True)
    
    df = df[df['dt'].between(dateStart, dateEnd)]

    df = df[df['dt'].str.contains(months[month])]

    df.rename(columns={'dt' : 'Date'}, inplace=True)
    return df


Dict = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06',
        'July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}


def TemperatureByCountry(Country = ('India' , 'China'),  Month = 'May' , From_Date = '1743-11-01' , To_Date = '2013-01-01'):

    """"
    # Function Description : 

        This Function Takes tuple of one or more Countries.  
        Function Takes Particular Month of a year.  
        Function takes Timeframe(From_Date , End-Date).  

    # Function Parameters : 

            # Country : 

                    This Parameter takes tuples of Countries as Input.\n
                    Default is ('India' , 'China')
            
            # Month : 

                    This Parameter takes Month Name as Input.\n
                    Default is 'May'.

            # From_Date : 

                    This Parameter is the Starting Date of the Dataset.\n
                    Default is '1743-11-01'

            # To_Date : 

                    This Parameter is the Ending Date of the Dataset.\n
                    Default is 2013-01-01'
            
    """
   
    if isinstance(Country , str):
        Country = [Country,]
    
    File = pd.read_csv(r'datasets/GlobalLandTemperaturesByCountry.csv')

    File.columns = ['Date' , 'Avg_Temperature' , 'Avg_Uncertainity','Country']

    File.dropna(subset = ['Avg_Temperature'] , inplace = True)

    File = File[File['Date'].between(From_Date,To_Date)]

    File = File[File['Date'].str.contains(Dict[Month])]

    File.reset_index(drop = True , inplace = True)
    
    New = pd.DataFrame
    Flag = 1

    for Ptr in Country:
        NewFile = File[File['Country'] == Ptr]

        NewFile = NewFile.drop(['Avg_Uncertainity','Country'],axis = 1)
        NewFile = NewFile.rename(columns = {'Avg_Temperature':Ptr})
        
        if(Flag == 1):
            New = NewFile
            Flag = 0
        else:
            #New = New.merge(NewFile)
            New = New.merge(NewFile)
    return New




def get_City_Graph_By_CSV(Cities = ['Delhi','Nagpur'] , Month = 'May'):
    """
    # Function Description : 
        This Function Takes City and Month as Input.  
        Returns List of Year and Temperature.  
        Can be Accessed as Year(List) , Temp(List) = get_City_Graph_By_CSV(City , Month).

    # Function Parameters : 

            # City : 

                    This parameter Takes City Name.  
                    Default is 'Delhi'.  
            
            # Month : 

                    This Parameter takes Month Name as Input.  
                    Default is 'May'.
    """
    New = pd.DataFrame
    Sign = 1
    for City in Cities:
        #City = input("Enter the City : ")
        #print()
        #Month = input("Enter the Month : ")
        Dict = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06',
                'July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
        with open('datasets/GlobalLandTemperaturesByMajorCity.csv') as File:
            File_Ptr = csv.reader(File)
            Flag = 0
            Year,Temp = [],[]
            for Lst in File_Ptr:
                if Flag == 0:
                    #print("Data for City ",City,"for Month ",Month,'is Give below')
                    Flag = 1
                else:
                    if(City == Lst[3]):
                        Str = Lst[0]
                        Str1 = Dict[Month]
                        if(Str1 == Str[5:7]):
                            if(Lst[1] != ""):
                                Year.append(int(Str[:4]))
                                Temp.append(float(Lst[1]))
                                #print("Date = ",Lst[0], "Avg_Temperature = ",Lst[1])
                                #monthCount = monthCount + 1
                        #Citycount = Citycount + 1
                        #print(1)
        File.close()
        Df = pd.DataFrame(np.column_stack([Year , Temp]),columns = ['Year',City])
        if Sign == 1:
            New = Df
            Sign = 0
        else:
            New = New.merge(Df)
        New['Year'] = New['Year'].astype(int)
    return New
        
        #print("Total Data of ",City , "is ",Citycount)
        #print("Total Data for ",Month , "is",monthCount)
        #plt.plot(Year , Temp ,linewidth = 2,markersize = 12)
    #plt.show()


def get_Temperature_Graph_By_CSV(Countries = ['India','China'], Month = 'May'):
    #Country = input("Enter the Country : ")
    #print()
    #Month = input("Enter the Month : ")

    """
    # Function Description : 
        This Function takes Country Name and Month as Input.  
        Returns List of Year and Average Temperatrue.  
        Can be Accessed as Year(List) , Avg_Temperature(List) = get_Temperature_Graph_By_CSV(Country , Month).  

    # Function Parameter : 

            # Country : 

                    This Parameter takes Country Name as Input.  
                    Default is 'India'.  

            # Month : 

                    This Parametre takes Month as Input.  
                    Default is 'May'.  
    """

    New = pd.DataFrame
    Sign = 1
    for Country in Countries:

        Dict = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06',
                'July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
        with open('datasets/GlobalLandTemperaturesByCountry.csv') as File:
            File_Ptr = csv.reader(File)
            Count  = 0
            Year , Avg_Temperature = [],[]
            for Lst in File_Ptr:
                if Count == 0:
                    #print("Data for the Month",Month, "is given below")
                    Count = 1
                else:
                    Str = Lst[0]
                    if(Lst[3] == Country):
                        Month_Code = Dict[Month]
                        if(Str[5:7] == Month_Code):
                            if(Lst[1] != ""):
                                Year.append(int(Str[:4]))
                                Avg_Temperature.append(float(Lst[1]))
                                #print("Date = ",Lst[0]," : Average_Temperature = ",Lst[1]," : Uncertainty = ",Lst[2]," : Country = ",Lst[3])
                                #Cmonth = Cmonth + 1
                        Count = Count + 1
            #print("Total Data of Month ",Month, "is ",Cmonth)
            #print("Total Data of ",Country,"is ",Count)
        File.close()
        Df = pd.DataFrame(np.column_stack([Year , Avg_Temperature]),columns = ['Year',Country])
        if Sign == 1:
            New = Df
            Sign = 0
        else:
            New = New.merge(Df)
        New['Year'] = New['Year'].astype(int)
    return New
        
        #plt.plot(Year, Avg_Temperature, 'go--', linewidth = 2, markersize = 8)
        #plt.show()







