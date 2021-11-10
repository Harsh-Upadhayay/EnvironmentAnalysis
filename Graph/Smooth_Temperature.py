
import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import savgol_filter


def Get_Graph_Temperature_India(Dataframe, ax):
    PLt = Dataframe.plot(x='Year', linestyle='dashed', linewidth=2, subplots=True,
                         title='Average Temperatures', ylabel='Temperature', ax=ax)

    Count = 1
    for Plot in PLt:
        Arr = np.array([list(Dataframe['Year']), list(
            Dataframe[Dataframe.columns[Count]])])
        # print(Arr[0])
        # print(Arr[1])
        Mean = Dataframe[Dataframe.columns[Count]].mean()
        # print(Mean)
        y_mean = [Mean]*len(Arr[0])
        Arr[1].astype(np.float)
        Smoothed = savgol_filter(
            Arr[1], window_length=47, polyorder=3, mode='interp')
        # print(Smoothed)
        Plot.plot(Arr[0], Smoothed, color='green', label='Smoothed')
        #y_mean = [np.mean(Arr[1],dtype = float)]*len(Arr[0])
        # print(y_mean)
        Plot.plot(Arr[0], y_mean, label='Mean', color='orange')
        legend = Plot.legend(loc='upper left')
        Count = Count + 1
    plt.show()


def Get_Graph_Temperature_SubTrue(Dataframe, ax):
    #Plot = Dataframe.plot(x = 'Year', subplots=False,linestyle = 'dashed' ,   ylabel='Temperature', ax=ax)
    PLt = Dataframe.plot(x='Date', linestyle='dashed', linewidth=2, subplots=True,
                         title='Average Temperatures', ylabel='Temperature', ax=ax)

    Count = 1
    for Plot in PLt:
        Arr = np.array([list(Dataframe['Date']), list(
            Dataframe[Dataframe.columns[Count]])])
        Smoothed = savgol_filter(
            Arr[1], window_length=47, polyorder=3, mode='interp')

        Plot.plot(Arr[0], Smoothed, color='green', label='Smoothed')
        y_mean = [np.mean(Arr[1])]*len(Arr[0])
        Plot.plot(Arr[0], y_mean, label='Mean', color='orange')
        legend = Plot.legend(loc='upper left')
        Count = Count + 1
    plt.show()


def Get_Graph_Temperature_SubTrue_Global(Dataframe, ax):
    PLt = Dataframe.plot(x='Date', linestyle='dashed', linewidth=2, subplots=True,
                         title='Average Temperatures', ylabel='Temperature', ax=ax)

    Count = 1
    for Plot in PLt:
        Arr = np.array([list(Dataframe['Date']), list(
            Dataframe[Dataframe.columns[Count]])])
        # print(Arr[0])
        # print(Arr[1])
        Mean = Dataframe[Dataframe.columns[Count]].mean()
        # print(Mean)
        y_mean = [Mean]*len(Arr[0])
        Arr[1].astype(np.float)
        Smoothed = savgol_filter(
            Arr[1], window_length=47, polyorder=3, mode='interp')
        # print(Smoothed)
        Plot.plot(Arr[0], Smoothed, color='green', label='Smoothed')
        #y_mean = [np.mean(Arr[1],dtype = float)]*len(Arr[0])
        # print(y_mean)
        Plot.plot(Arr[0], y_mean, label='Mean', color='orange')
        legend = Plot.legend(loc='upper left')
        Count = Count + 1
    plt.show()


def Get_Graph_Temperature_SubTrue_Global_Csv(Dataframe, ax):
    PLt = Dataframe.plot(x='Year', linestyle='dashed', linewidth=2, subplots=True,
                         title='Average Temperatures', ylabel='Temperature', ax=ax)

    Count = 1
    for Plot in PLt:
        Arr = np.array([list(Dataframe['Year']), list(
            Dataframe[Dataframe.columns[Count]])])
        # print(Arr[0])
        # print(Arr[1])
        Mean = Dataframe[Dataframe.columns[Count]].mean()
        # print(Mean)
        y_mean = [Mean]*len(Arr[0])
        Arr[1].astype(np.float)
        Smoothed = savgol_filter(
            Arr[1], window_length=47, polyorder=3, mode='interp')
        # print(Smoothed)
        Plot.plot(Arr[0], Smoothed, color='green', label='Smoothed')
        #y_mean = [np.mean(Arr[1],dtype = float)]*len(Arr[0])
        # print(y_mean)
        Plot.plot(Arr[0], y_mean, label='Mean', color='orange')
        legend = Plot.legend(loc='upper left')
        Count = Count + 1
    plt.show()
