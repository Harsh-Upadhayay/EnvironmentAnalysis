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


def WBD_TA_Country(countries, placeHolder):
    
    countries = countries.get().split(',')
    idx = 0
    for country in countries:
        countries[idx] = country.strip()
        idx += 1

    df = globalWBD.TemperatureByCountriesWBD(countries)
    figure = plt.Figure(figsize=(10, 6), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    df.plot(x = 'Date', subplots=True,  ylabel='Temperature in degree celsius', ax=ax)
    

def countryBox(placeHolder, firstMessage, secondMessage, firstPos = 0):
    try :    
        countryName = StringVar()

        f1 = LabelFrame(placeHolder, text=firstMessage)
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = Label(f1, text=secondMessage).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = Entry(f1, textvariable=countryName).grid(
            column=1, row=0, padx=8, pady=4)

        b1 = Button(f1, text="show", command=lambda : WBD_TA_Country(countryName, placeHolder)).grid(
            row=1, columnspan=2, pady=2)
    except :
        _msg()

countryBox(Tmp_analysis, "Country Analysis", "Enter Contry Name", 0)
countryBox(Tmp_analysis, "Countries Comparision", "Enter Contries Name (Comma Seperated)", 1)
win.mainloop()
