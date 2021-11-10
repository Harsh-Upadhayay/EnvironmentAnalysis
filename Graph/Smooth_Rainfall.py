import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import savgol_filter


def Get_Graph_Rainfall(Dataframe, ax):
    Plot = Dataframe.plot(x='Year', linestyle='dashed', linewidth=2,
                          title='Annual Rainfall of ' + Dataframe.columns[1], ylabel='Rainfall in mm', ax=ax)

    Arr = np.array([list(Dataframe['Year']), list(
        Dataframe[Dataframe.columns[1]])])
    Smoothed = savgol_filter(
        Arr[1], window_length=47, polyorder=3, mode='interp')

    Plot.plot(Arr[0], Smoothed, color='green', label='Smoothed')
    y_mean = [np.mean(Arr[1])]*len(Arr[0])
    Plot.plot(Arr[0], y_mean, label='Mean', color='orange')
    legend = Plot.legend(loc='upper left')
    plt.show()


def Get_Graph_Rainfall_SubTrue(Dataframe, ax):
    PLt = Dataframe.plot(x='Year', linestyle='dashed', linewidth=2, subplots=True,
                         title='Annual Rainfall', ylabel='Rainfall in mm', ax=ax)
    #Arr = np.array([list(Dataframe['Year']) , list(Dataframe[Dataframe.columns[1]])])
    #Smoothed = np.ared = savgol_filter(Arr[1] , window_length= 47 , polyorder = 2 , mode = 'interp')
    #PLt.plot(Arr[0], Smoothed , color='green',label = 'Smoothed')
    #y_mean = [np.mean(Arr[1])]*len(Arr[0])
    #PLt.plot(Arr[0] , y_mean , label = 'Mean', color = 'orange')
    #legend = PLt.legend(loc='upper left')

    Count = 1
    for Plot in PLt:
        Arr = np.array([list(Dataframe['Year']), list(
            Dataframe[Dataframe.columns[Count]])])
        Smoothed = np.ared = savgol_filter(
            Arr[1], window_length=47, polyorder=3, mode='interp')

        Plot.plot(Arr[0], Smoothed, color='green', label='Smoothed')
        y_mean = [np.mean(Arr[1])]*len(Arr[0])
        Plot.plot(Arr[0], y_mean, label='Mean', color='orange')
        legend = Plot.legend(loc='upper left')
        Count = Count + 1
    plt.show()
