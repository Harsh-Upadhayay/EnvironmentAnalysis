from Climate.Temperature.USA import TemperatureAnalysisUS as US_Temp_analysis
from Climate.Temperature.India import *
from Climate.Temperature.Global import *
from Climate.Temperature.GlobalWBD import *
from Climate.Precipitation.Rainfall_Analysis import *

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg


# Basic Setup
win = Tk()
win.title("Python Mini Project")


tabcontrol = ttk.Notebook(win)
about = ttk.Frame(tabcontrol)
tabcontrol.add(about, text="About")

Tmp_analysis = ttk.Frame(tabcontrol)
tabcontrol.add(Tmp_analysis, text="Temprature Analysis")

rain_analysis = ttk.Frame(tabcontrol)
tabcontrol.add(rain_analysis, text="Rain Fall Analysis")

tabcontrol.pack(expand=1, fill="both")


# About

frame1 = LabelFrame(about, text="Analysis of Climate Change")
frame1.grid(column=0, row=0, padx=8, pady=4)

para = Label(frame1, text="The program will analyze changes in the climate over an interval . It will also generate the distribution curve of the data. ")
para.grid(column=0, row=0, sticky=W, padx=10, pady=10)

frame2 = LabelFrame(about, text="Tech stack")
frame2.grid(column=0, row=1, padx=8, pady=4)

para2_1 = Label(frame2, text="Numpy").grid(
    column=0, row=0, sticky=W, padx=10, pady=10)
para2_2 = Label(frame2, text="Pandas").grid(
    column=0, row=1, sticky=W, padx=10, pady=10)
para2_3 = Label(frame2, text="Matplotlib").grid(
    column=0, row=2, sticky=W, padx=10, pady=10)
para2_4 = Label(frame2, text="Python GUI (Tkinter)").grid(
    column=0, row=2, sticky=W, padx=10, pady=10)


frame3 = LabelFrame(about, text="Participants or Group info")
frame3.grid(column=0, row=2, padx=8, pady=4)

list_el_1 = Label(frame3, text="1.Harsh Upadhyay").grid(
    column=0, row=0, sticky=W, padx=10, pady=5)
list_el_2 = Label(frame3, text="2.Harsh tripathi").grid(
    column=0, row=1, sticky=W, padx=10, pady=5)
list_el_3 = Label(frame3, text="3.Prathamesh Patil").grid(
    column=0, row=2, sticky=W, padx=10, pady=5)
list_el_4 = Label(frame3, text="4.Niraj Matre").grid(
    column=0, row=3, sticky=W, padx=10, pady=5)
list_el_5 = Label(frame3, text="5.Ayush chaurasia").grid(
    column=0, row=4, sticky=W, padx=10, pady=5)


# RAINFALL ANALYSIS
def _msg():
    msg.showerror("Error", "Enter correct name!")


def raifall_by_country():
    try:
        country = country_name.get()
        df = Analyse_Rain_Countries([country])
        figure = plt.Figure(figsize=(10, 6), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, rain_analysis)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        df.plot(x='Year', color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=12,
                subplots=True, title='Annual Rainfall in MM',  ylabel='Rainfall in MM', ax=ax)
    except:
        _msg()
        return 0


def rainfall_by_state():
    try:
        state = state_name.get()
        country_for_state = Country_for_state.get()
        df = Analyse_Rain_State(country_for_state, [state])
        figure = plt.Figure(figsize=(10, 6), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, rain_analysis)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        df.plot(x='Year', color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=12,
                subplots=True, title='Annual Rainfall in MM',  ylabel='Rainfall in MM', ax=ax)
    except:
        _msg()
        return 0


def raifall_by_country_comparison():
    try:
        country_1 = country_name1.get()
        country_2 = country_name2.get()
        df = Analyse_Rain_Countries([country_1, country_2])
        figure = plt.Figure(figsize=(10, 6), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, rain_analysis)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        df.plot(x='Year', color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=12,
                subplots=True, title='Annual Rainfall in MM',  ylabel='Rainfall in MM', ax=ax)
    except:
        _msg()
        return 0


def raifall_by_state_comparison():
    try:
        country_f_s = country_for_states.get()
        state_1 = state_name1.get()
        state_2 = state_name2.get()
        df = Analyse_Rain_State(country_f_s, [state_1, state_2])
        figure = plt.Figure(figsize=(10, 6), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, rain_analysis)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        df.plot(x='Year', color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=12,
                subplots=True, title='Annual Rainfall in MM',  ylabel='Rainfall in MM', ax=ax)
    except:
        _msg()
        return 0


# Single Country
country_name = StringVar()

f1 = LabelFrame(rain_analysis, text="Analysis by country")
f1.grid(column=0, row=0, padx=8, pady=2)

l1 = Label(f1, text="Enter Country Name :").grid(
    column=0, row=0, padx=8, pady=4)

e1 = Entry(f1, textvariable=country_name).grid(
    column=1, row=0, padx=8, pady=4)

b1 = Button(f1, text="show", command=raifall_by_country).grid(
    row=1, columnspan=2, pady=2)


# Compare Countries
country_name1 = StringVar()
country_name2 = StringVar()

f2 = LabelFrame(rain_analysis, text="Compare countries")
f2.grid(column=1, row=0, padx=8, pady=2)

l1_1 = Label(f2, text="Enter First Country Name :").grid(
    column=0, row=0, padx=8, pady=4)

e1_1 = Entry(f2, textvariable=country_name1).grid(
    column=1, row=0, padx=8, pady=4)

l2_1 = Label(f2, text="Enter Second Country Name :").grid(
    column=0, row=1, padx=8, pady=4)

e2_1 = Entry(f2, textvariable=country_name2).grid(
    column=1, row=1, padx=8, pady=4)

b2 = Button(f2, text="show", command=raifall_by_country_comparison).grid(
    row=2, columnspan=2, pady=2)


# Single State
state_name = StringVar()
Country_for_state = StringVar()

f3 = LabelFrame(rain_analysis, text="Analysis by State")
f3.grid(column=2, row=0, padx=8, pady=2)

l_c = Label(f3, text="Enter Country Name:").grid(
    column=0, row=0, padx=8, pady=4)

e_c = Entry(f3, textvariable=Country_for_state).grid(
    column=1, row=0, padx=8, pady=4)

l3 = Label(f3, text="Enter State Name :").grid(
    column=0, row=1, padx=8, pady=4)

e3 = Entry(f3, textvariable=state_name).grid(
    column=1, row=1, padx=8, pady=4)

b3 = Button(f3, text="show", command=rainfall_by_state).grid(
    row=2, columnspan=2, pady=2)

# Compare states
country_for_states = StringVar()
state_name1 = StringVar()
state_name2 = StringVar()

f4 = LabelFrame(rain_analysis, text="Compare states")
f4.grid(column=3, row=0, padx=8, pady=2)

l_c_1 = Label(f4, text="Enter Country Name:").grid(
    column=0, row=0, padx=8, pady=4)

e_c_1 = Entry(f4, textvariable=country_for_states).grid(
    column=1, row=0, padx=8, pady=4)

l3_1 = Label(f4, text="Enter First State Name :").grid(
    column=0, row=1, padx=8, pady=4)

e3_1 = Entry(f4, textvariable=state_name1).grid(
    column=1, row=1, padx=8, pady=4)

l3_1 = Label(f4, text="Enter Second State Name :").grid(
    column=0, row=2, padx=8, pady=4)

e3_1 = Entry(f4, textvariable=state_name2).grid(
    column=1, row=2, padx=8, pady=4)

b4 = Button(f4, text="show", command=raifall_by_state_comparison).grid(
    row=3, columnspan=2, pady=2)


win.mainloop()
