import Climate.Temperature.Global as globalKaggle

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
from tkinter import ttk
from tkinter import messagebox as msg

win = tkinter.Tk()
win.title("Python Mini Project")


tabcontrol = ttk.Notebook(win)
about = ttk.Frame(tabcontrol)
tabcontrol.add(about, text="About")

Tmp_analysis = ttk.Frame(tabcontrol)
tabcontrol.add(Tmp_analysis, text="Temperature Analysis")

tabcontrol.pack(expand=1, fill="both")


def _msg():
    msg.showerror("Error", "Enter correct name!")


def kaggle_TA_Country(placeHolder, countries, month):
    
    countries = countries.get().split(',')
    idx = 0
    for country in countries:
        countries[idx] = country.strip()
        idx += 1
    try :
        month = month.get()
    except :
        month = 'May'

    df = globalKaggle.TemperatureByCountry(countries, month)
    figure = plt.Figure(figsize=(10, 6), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)
    
    df.plot(x = 'Date', subplots=False,  ylabel='Temperature in degree celsius', ax=ax)
    

def kaggle_TA_State(placeHolder, states, month):
    
    states = states.get().split(',')
    idx = 0
    for state in states:
        states[idx] = state.strip()
        idx += 1

    try : 
        month = month.get()
    except : 
        month = "May"

    df = globalKaggle.TemperaturesByState(states, month)
    figure = plt.Figure(figsize=(10, 6), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    df.plot(x = 'Date', subplots=True,  ylabel='Temperature in degree celsius', ax=ax)
    

def kaggle_TA_Cities(placeHolder, cities, month):
    
    cities = cities.get().split(',')
    idx = 0
    for city in cities:
        cities[idx] = city.strip()
        idx += 1

    try : 
        month = month.get()
    except : 
        month = "May"

    df = globalKaggle.TemperaturesByCity(cities, month)
    figure = plt.Figure(figsize=(10, 6), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    df.plot(x = 'Date', subplots=True,  ylabel='Temperature in degree celsius', ax=ax)
    

def countryBox(placeHolder, firstMessage, secondMessage, firstPos = 0):
    try :    
        countryName = tkinter.StringVar()
        month = tkinter.StringVar()

        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage)
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text=secondMessage).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=countryName).grid(
            column=1, row=0, padx=8, pady=4)

        l2 = tkinter.Label(f1, text="Enter Month (required)").grid(
            column=0, row=1, padx=8, pady=4)

        e2 = tkinter.Entry(f1, textvariable=month).grid(
            column=1, row=1, padx=8, pady=4)

        b1 = tkinter.Button(f1, text="show", command=lambda : kaggle_TA_Country(placeHolder, countryName, month)).grid(
            row=2, columnspan=2, pady=2)
    except :
        _msg()


def stateBox(placeHolder, firstMessage, secondMessage, firstPos = 0):
    try :    
        stateName = tkinter.StringVar()
        month = tkinter.StringVar()

        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage)
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text=secondMessage).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=stateName).grid(
            column=1, row=0, padx=8, pady=4)

        l2 = tkinter.Label(f1, text="Enter Month (required)").grid(
            column=0, row=1, padx=8, pady=4)

        e2 = tkinter.Entry(f1, textvariable=month).grid(
            column=1, row=1, padx=8, pady=4)

        b1 = tkinter.Button(f1, text="show", command=lambda : kaggle_TA_State(placeHolder, stateName, month)).grid(
            row=2, columnspan=2, pady=2)
    except :
        _msg()


def cityBox(placeHolder, firstMessage, secondMessage, firstPos = 0):
    try :    
        cityName = tkinter.StringVar()
        month = tkinter.StringVar()

        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage)
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text=secondMessage).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=cityName).grid(
            column=1, row=0, padx=8, pady=4)

        l2 = tkinter.Label(f1, text="Enter Month (required)").grid(
            column=0, row=1, padx=8, pady=4)

        e2 = tkinter.Entry(f1, textvariable=month).grid(
            column=1, row=1, padx=8, pady=4)

        b1 = tkinter.Button(f1, text="show", command=lambda : kaggle_TA_Cities(placeHolder, cityName, month)).grid(
            row=2, columnspan=2, pady=2)
    except :
        _msg()



countryBox(Tmp_analysis, "Countries Comparision", "Enter Countries Name (Comma Seperated)", 0)
stateBox(Tmp_analysis, "States Comparision", "Enter States Name (Comma Seperated)", 1)
cityBox(Tmp_analysis, "Cities Comparision", "Enter Cities Name (Comma Seperated)", 2)

win.mainloop()
