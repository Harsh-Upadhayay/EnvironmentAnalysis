import Climate.Precipitation.Rainfall_Analysis as RainAnalysis

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
from tkinter import messagebox as msg



def _msg():
    msg.showerror("Error", "Enter correct name!")


def rainfall_by_country(Frame, country_name, st_year):
    try:
        country = []
        country = country_name.get().split(",")
        start_year = st_year.get()
        df = RainAnalysis.Analyse_Rain_Countries(country, start_year)
        figure = plt.Figure(figsize=(10, 6), facecolor='white')
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, Frame)
        chart_type.get_tk_widget().grid(
            column=0, row=1, columnspan=4)
        df.plot(x='Year', title='Annual Rainfall in MM',
                ylabel='Rainfall in MM', ax=ax)
    except:
        _msg()

        return 0


def rainfall_by_state(Frame,Country_for_state, state_name, year):
    try:
        state = []
        state = state_name.get().split(",")
        country_for_state = Country_for_state.get()
        y1 = year.get()
        df = RainAnalysis.Analyse_Rain_State(country_for_state, state, y1)
        figure = plt.Figure(figsize=(10, 6), facecolor='white')
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, Frame)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        df.plot(x='Year', title='Annual Rainfall in MM',
                ylabel='Rainfall in MM', ax=ax)
    except:
        _msg()
        return 0


def rainfall_by_country_comparison(Frame, country_name1, country_name2, s_year):
    try:
        country_1 = country_name1.get()
        country_2 = country_name2.get()
        y2 = s_year.get()
        df = RainAnalysis.Analyse_Rain_Countries([country_1, country_2], y2)
        figure = plt.Figure(figsize=(10, 6), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, Frame)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        df.plot(x='Year', color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=12,
                subplots=True, title='Annual Rainfall in MM',  ylabel='Rainfall in MM', ax=ax)
    except:
        _msg()
        return 0


def rainfall_by_state_comparison(Frame,country_for_states, state_name1, state_name2, Y_for_state):
    try:
        country_f_s = country_for_states.get()
        state_1 = state_name1.get()
        state_2 = state_name2.get()
        y3 = Y_for_state.get()
        df = RainAnalysis.Analyse_Rain_State(country_f_s, [state_1, state_2], y3)
        figure = plt.Figure(figsize=(10, 6), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, Frame)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        df.plot(x='Year', color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=12,
                subplots=True, title='Annual Rainfall in MM',  ylabel='Rainfall in MM', ax=ax)
    except:
        _msg()
        return 0


# Single Country
def countryBox(Frame):
    country_name = tkinter.StringVar()
    st_year = tkinter.IntVar()
    f1 = tkinter.LabelFrame(Frame, text="Analysis by country")
    f1.grid(column=0, row=0, padx=8, pady=2)

    l1 = tkinter.Label(f1, text="Enter Country Name :").grid(
        column=0, row=0, padx=8, pady=4)

    e1 = tkinter.Entry(f1, textvariable=country_name).grid(
        column=1, row=0, padx=8, pady=4)
    scale_label = tkinter.Label(f1, text="Select Year ").grid(
        row=1, column=0, columnspan=3)
    s1 = tkinter.Scale(f1, from_=1901, to=2020, orient=tkinter.HORIZONTAL, variable=st_year).grid(
        row=2, columnspan=3)
    b1 = tkinter.Button(f1, text="show", command=lambda : rainfall_by_country(Frame, country_name, st_year)).grid(
        row=3, columnspan=3, pady=2)


# Compare Countries
def countriesBox(Frame):
    country_name1 = tkinter.StringVar()
    country_name2 = tkinter.StringVar()
    s_year = tkinter.IntVar()

    f2 = tkinter.LabelFrame(Frame, text="Compare countries")
    f2.grid(column=1, row=0, padx=8, pady=2)

    l1_1 = tkinter.Label(f2, text="Enter First Country Name :").grid(
        column=0, row=0, padx=8, pady=4)

    e1_1 = tkinter.Entry(f2, textvariable=country_name1).grid(
        column=1, row=0, padx=8, pady=4)

    l2_1 = tkinter.Label(f2, text="Enter Second Country Name :").grid(
        column=0, row=1, padx=8, pady=4)

    e2_1 = tkinter.Entry(f2, textvariable=country_name2).grid(
        column=1, row=1, padx=8, pady=4)
    scale1_label = tkinter.Label(f2, text="Start Year").grid(row=2, columnspan=2)
    s2 = tkinter.Scale(f2, from_=1901, to=2020, orient=tkinter.HORIZONTAL,
                variable=s_year).grid(row=3, columnspan=2)
    b2 = tkinter.Button(f2, text="show", command=lambda : rainfall_by_country_comparison(Frame, country_name1, country_name2, s_year)).grid(
        row=4, columnspan=2, pady=2)


# Single State
def stateBox(Frame):
    state_name =tkinter.StringVar()
    Country_for_state = tkinter.StringVar()
    year = tkinter.IntVar()

    f3 = tkinter.LabelFrame(Frame, text="Analysis by State")
    f3.grid(column=2, row=0, padx=8, pady=2)

    l_c = tkinter.Label(f3, text="Enter Country Name:").grid(
        column=0, row=0, padx=8, pady=4)

    e_c = tkinter.Entry(f3, textvariable=Country_for_state).grid(
        column=1, row=0, padx=8, pady=4)

    l3 = tkinter.Label(f3, text="Enter State Name :").grid(
        column=0, row=1, padx=8, pady=4)

    e3 = tkinter.Entry(f3, textvariable=state_name).grid(
        column=1, row=1, padx=8, pady=4)

    y_label = tkinter.Label(f3, text="Start Year").grid(row=2, columnspan=2)

    Y_scale = tkinter.Scale(f3, from_=1901, to=2020, orient=tkinter.HORIZONTAL,
                    variable=year).grid(row=3, columnspan=2)

    b3 = tkinter.Button(f3, text="show", command=lambda: rainfall_by_state(Frame,Country_for_state, state_name, year)).grid(
        row=4, columnspan=2, pady=2)


# Compare states
def statesBox(Frame):
    country_for_states = tkinter.StringVar()
    state_name1 = tkinter.StringVar()
    state_name2 = tkinter.StringVar()
    Y_for_state = tkinter.IntVar()

    f4 = tkinter.LabelFrame(Frame, text="Compare states")
    f4.grid(column=3, row=0, padx=8, pady=2)

    l_c_1 = tkinter.Label(f4, text="Enter Country Name:").grid(
        column=0, row=0, padx=8, pady=4)

    e_c_1 = tkinter.Entry(f4, textvariable=country_for_states).grid(
        column=1, row=0, padx=8, pady=4)

    l3_1 = tkinter.Label(f4, text="Enter First State Name :").grid(
        column=0, row=1, padx=8, pady=4)

    e3_1 = tkinter.Entry(f4, textvariable=state_name1).grid(
        column=1, row=1, padx=8, pady=4)

    l3_1 = tkinter.Label(f4, text="Enter Second State Name :").grid(
        column=0, row=2, padx=8, pady=4)

    e3_1 = tkinter.Entry(f4, textvariable=state_name2).grid(
        column=1, row=2, padx=8, pady=4)

    state_s_label = tkinter.Label(f4, text="Start Year").grid(row=3, columnspan=2)
    state_scale = tkinter.Scale(f4, from_=1901, to=2020, orient=tkinter.HORIZONTAL,
                        variable=Y_for_state).grid(row=3, columnspan=2)

    b4 = tkinter.Button(f4, text="show", command=lambda : rainfall_by_state_comparison(Frame,country_for_states, state_name1, state_name2, Y_for_state)).grid(
        row=4, columnspan=2, pady=2)

