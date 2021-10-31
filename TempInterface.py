import Climate.Temperature.GlobalWBD  as globalWBD
import Climate.Temperature.Global  as globalKaggle
import Climate.Temperature.USA as USA
import Climate.Temperature.India as India

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

win = Tk()
win.title("Python Mini Project")


tabcontrol = ttk.Notebook(win)
about = ttk.Frame(tabcontrol)
tabcontrol.add(about, text="About")

Tmp_analysis = ttk.Frame(tabcontrol)
tabcontrol.add(Tmp_analysis, text="Temperature Analysis")

tabcontrol.pack(expand=1, fill="both")


def _msg():
    msg.showerror("Error", "Enter correct name!")


def WBD_TA_Country(country_name, rainAnalysis):
    
    country = country_name.get()
    df = globalWBD.TemperatureByCountriesWBD([country])
    figure = plt.Figure(figsize=(10, 6), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, rainAnalysis)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    df.plot(x = 'Date', subplots=True, title=country,  ylabel='Temperature in degree celsius', ax=ax)
    

def countryBox():
    countryName = StringVar()

    f1 = LabelFrame(Tmp_analysis, text="Analysis by country")
    f1.grid(column=0, row=0, padx=8, pady=2)

    l1 = Label(f1, text="Enter Country Name :").grid(
        column=0, row=0, padx=8, pady=4)

    e1 = Entry(f1, textvariable=countryName).grid(
        column=1, row=0, padx=8, pady=4)

    b1 = Button(f1, text="show", command=lambda : WBD_TA_Country(countryName, Tmp_analysis)).grid(
        row=1, columnspan=2, pady=2)


def countryComparisonBox():
    countriesName = StringVar()

    f1 = LabelFrame(Tmp_analysis, text="Analysis by country")
    f1.grid(column=0, row=0, padx=8, pady=2)

    l1 = Label(f1, text="Enter Country Name :").grid(
        column=0, row=0, padx=8, pady=4)

    e1 = Entry(f1, textvariable=countriesName).grid(
        column=1, row=0, padx=8, pady=4)

    b1 = Button(f1, text="show", command=lambda : WBD_TA_Country(countryName, Tmp_analysis)).grid(
        row=1, columnspan=2, pady=2)

countryBox()
win.mainloop()
