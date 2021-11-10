import Climate.Temperature.Global as globalKaggle

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
from tkinter import ttk
from tkinter import messagebox as msg

import Graph.Smooth_Temperature as Smooth


def _msg():
    msg.showerror("Error", "Enter correct name!")


def kaggle_TA_Country(placeHolder, countries, month, s_year, e_year):

    countries = countries.get().split(',')
    s = s_year.get()
    e = e_year.get()
    idx = 0
    for country in countries:
        countries[idx] = country.strip()
        idx += 1
    try:
        month = month.get()
    except:
        month = 'May'

    df = globalKaggle.TemperatureByCountry(
        countries, month, str(s)+'-01-01', str(e)+'-01-01')
    figure = plt.Figure(figsize=(12, 5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    #df.plot(x = 'Date', subplots=False,  ylabel='Temperature in degree celsius', ax=ax)
    Smooth.Get_Graph_Temperature_SubTrue_Global(df, ax)


def kaggle_TA_CountryCSV(placeHolder, countries, month):

    countries = countries.get().split(',')
    idx = 0
    for country in countries:
        countries[idx] = country.strip()
        idx += 1
    try:
        month = month.get()
    except:
        month = 'May'

    Df = globalKaggle.get_Temperature_Graph_By_CSV(
        countries, month)
    figure = plt.Figure(figsize=(12, 5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    #Df.plot( x = 'Year',linewidth = 2, markersize = 8)
    Smooth.Get_Graph_Temperature_SubTrue_Global_Csv(Df, ax)


def kaggle_TA_State(placeHolder, states, month, s_year, e_year):

    states = states.get().split(',')
    s = s_year.get()
    e = e_year.get()
    idx = 0
    for state in states:
        states[idx] = state.strip()
        idx += 1

    try:
        month = month.get()
    except:
        month = "May"

    df = globalKaggle.TemperaturesByState(
        states, month, str(s)+'-01-01', str(e)+'-01-01')
    figure = plt.Figure(figsize=(12, 5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    #df.plot(x = 'Date', subplots=True,  ylabel='Temperature in degree celsius', ax=ax)
    Smooth.Get_Graph_Temperature_SubTrue_Global(df, ax)


def kaggle_TA_Cities(placeHolder, cities, month, s_year, e_year):

    cities = cities.get().split(',')
    s = s_year.get()
    e = e_year.get()
    idx = 0
    for city in cities:
        cities[idx] = city.strip()
        idx += 1

    try:
        month = month.get()
    except:
        month = "May"

    df = globalKaggle.TemperaturesByCity(
        cities, month, str(s)+'-01-01', str(e)+'-01-01')
    figure = plt.Figure(figsize=(12, 5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    #df.plot(x = 'Date', subplots=True,  ylabel='Temperature in degree celsius', ax=ax)
    Smooth.Get_Graph_Temperature_SubTrue_Global(df, ax)


def kaggle_TA_CitiesCSV(placeHolder, cities, month):

    cities = cities.get().split(',')
    idx = 0
    for city in cities:
        cities[idx] = city.strip()
        idx += 1

    try:
        month = month.get()
    except:
        month = "May"

    Df = globalKaggle.get_City_Graph_By_CSV(cities, month)
    # print(Df)
    figure = plt.Figure(figsize=(12, 5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)
    #Df.plot(x = 'Year', linewidth = 2, markersize = 8,ax = ax)
    Smooth.Get_Graph_Temperature_SubTrue_Global_Csv(Df, ax)


def countryBox(placeHolder, firstMessage, secondMessage, firstPos=0):
    try:
        countryName = tkinter.StringVar()
        month = tkinter.StringVar()
        s_year = tkinter.IntVar()
        e_year = tkinter.IntVar()
        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage, font=(
            "Courier", 14), bg='honeydew2')
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text=secondMessage, bg='honeydew2', font=("dongle", 10)).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=countryName).grid(
            column=1, row=0, padx=8, pady=4)

        l2 = tkinter.Label(f1, text="Enter Month (required)", bg='honeydew2', font=("dongle", 10)).grid(
            column=0, row=1, padx=8, pady=4)

        e2 = tkinter.Entry(f1, textvariable=month).grid(
            column=1, row=1, padx=8, pady=4)
        scale1_label = tkinter.Label(
            f1, text="From Year").grid(row=2, column=0)
        s2 = tkinter.Scale(f1, from_=1743, to=2013, orient=tkinter.HORIZONTAL,
                           variable=s_year).grid(row=3, column=0)
        scale1_label_2 = tkinter.Label(
            f1, text="To Year").grid(row=2, column=1)
        s2_2 = tkinter.Scale(f1, from_=1840, to=2013, orient=tkinter.HORIZONTAL,
                             variable=e_year).grid(row=3, column=1)
        b1 = tkinter.Button(f1, text="show using Pandas", command=lambda: kaggle_TA_Country(placeHolder, countryName, month, s_year, e_year), bg='goldenrod1').grid(
            column=0, row=4, columnspan=2, pady=2)

        b2 = tkinter.Button(f1, text="show using csv", command=lambda: kaggle_TA_CountryCSV(placeHolder, countryName, month), bg='goldenrod1').grid(
            column=1, row=4, columnspan=2, pady=2)

    except:
        _msg()


def stateBox(placeHolder, firstMessage, secondMessage, firstPos=0):
    try:
        stateName = tkinter.StringVar()
        month = tkinter.StringVar()
        s_year = tkinter.IntVar()
        e_year = tkinter.IntVar()
        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage, font=(
            "Courier", 14), bg='honeydew2')
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text=secondMessage, bg='honeydew2', font=("dongle", 10)).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=stateName).grid(
            column=1, row=0, padx=8, pady=4)

        l2 = tkinter.Label(f1, text="Enter Month (required)", bg='honeydew2', font=("dongle", 10)).grid(
            column=0, row=1, padx=8, pady=4)

        e2 = tkinter.Entry(f1, textvariable=month).grid(
            column=1, row=1, padx=8, pady=4)
        scale1_label = tkinter.Label(
            f1, text="From Year").grid(row=2, column=0)
        s2 = tkinter.Scale(f1, from_=1800, to=2010, orient=tkinter.HORIZONTAL,
                           variable=s_year).grid(row=3, column=0)
        scale1_label_2 = tkinter.Label(
            f1, text="To Year").grid(row=2, column=1)
        s2_2 = tkinter.Scale(f1, from_=1854, to=2010, orient=tkinter.HORIZONTAL,
                             variable=e_year).grid(row=3, column=1)
        b1 = tkinter.Button(f1, text="show", command=lambda: kaggle_TA_State(placeHolder, stateName, month, s_year, e_year), bg='goldenrod1').grid(
            row=4, columnspan=2, pady=2)
    except:
        _msg()


def cityBox(placeHolder, firstMessage, secondMessage, firstPos=0):
    try:
        cityName = tkinter.StringVar()
        month = tkinter.StringVar()
        s_year = tkinter.IntVar()
        e_year = tkinter.IntVar()
        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage, font=(
            "Courier", 14), bg='honeydew2')
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text=secondMessage, bg='honeydew2', font=("dongle", 10)).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=cityName).grid(
            column=1, row=0, padx=8, pady=4)

        l2 = tkinter.Label(f1, text="Enter Month (required)", bg='honeydew2', font=("dongle", 10)).grid(
            column=0, row=1, padx=8, pady=4)

        e2 = tkinter.Entry(f1, textvariable=month).grid(
            column=1, row=1, padx=8, pady=4)
        scale1_label = tkinter.Label(
            f1, text="From Year").grid(row=2, column=0)
        s2 = tkinter.Scale(f1, from_=1800, to=2010, orient=tkinter.HORIZONTAL,
                           variable=s_year).grid(row=3, column=0)
        scale1_label_2 = tkinter.Label(
            f1, text="To Year").grid(row=2, column=1)
        s2_2 = tkinter.Scale(f1, from_=1854, to=2010, orient=tkinter.HORIZONTAL,
                             variable=e_year).grid(row=3, column=1)
        b1 = tkinter.Button(f1, text="show using Pandas", command=lambda: kaggle_TA_Cities(placeHolder, cityName, month, s_year, e_year), bg='goldenrod1').grid(
            column=0, row=4, columnspan=2, pady=2)

        b2 = tkinter.Button(f1, text="show using csv", command=lambda: kaggle_TA_CitiesCSV(placeHolder, cityName, month), bg='goldenrod1').grid(
            column=1, row=4, columnspan=2, pady=2)

    except:
        _msg()


def main():
    win = tkinter.Tk()
    win.title("Python Mini Project")

    tabcontrol = ttk.Notebook(win)
    about = ttk.Frame(tabcontrol)
    tabcontrol.add(about, text="About")

    Tmp_analysis = ttk.Frame(tabcontrol)
    tabcontrol.add(Tmp_analysis, text="Temperature Analysis")

    tabcontrol.pack(expand=1, fill="both")

    countryBox(Tmp_analysis, "Countries Comparision",
               "Enter Countries Name (Comma Seperated)", 0)
    stateBox(Tmp_analysis, "States Comparision",
             "Enter States Name (Comma Seperated)", 1)
    cityBox(Tmp_analysis, "Cities Comparision",
            "Enter Cities Name (Comma Seperated)", 2)

    win.mainloop()


if __name__ == "__main__":
    main()
