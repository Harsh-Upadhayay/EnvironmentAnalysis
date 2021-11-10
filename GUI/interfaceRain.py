import Climate.Precipitation.Rainfall_Analysis as RainAnalysis

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
from tkinter import messagebox as msg
import Graph.Smooth_Rainfall as PLOT


def _msg():
    msg.showerror("Error", "Enter correct name!")


def rainfall_by_country(Frame, country_name, st_year, en_year):
    try:
        country = []
        country = country_name.get().split(",")
        start_year = st_year.get()
        End_year = en_year.get()
        df = RainAnalysis.Analyse_Rain_Countries(country, start_year, End_year)
        figure = plt.Figure(figsize=(12, 5), facecolor='white')
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, Frame)
        chart_type.get_tk_widget().grid(
            column=0, row=1, columnspan=4)
        #df.plot(x='Year', title='Annual Rainfall in MM',ylabel='Rainfall in MM', ax=ax)
        PLOT.Get_Graph_Rainfall(df, ax)

    except:
        _msg()
        return 0


def rainfall_by_state(Frame, Country_for_state, state_name, year1, year2):
    try:
        state = []
        state = state_name.get().split(",")
        country_for_state = Country_for_state.get()
        y1 = year1.get()
        y2 = year2.get()
        df = RainAnalysis.Analyse_Rain_State(country_for_state, state, y1, y2)
        figure = plt.Figure(figsize=(12, 5), facecolor='white')
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, Frame)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        #df.plot(x='Year', title='Annual Rainfall in MM',ylabel='Rainfall in MM', ax=ax)
        PLOT.Get_Graph_Rainfall(df, ax)

    except:
        _msg()
        return 0


def rainfall_by_country_comparison(Frame, country_name1, country_name2, s_year, e_year):
    try:
        country_1 = country_name1.get()
        country_2 = country_name2.get()
        y1 = s_year.get()
        y2 = e_year.get()
        df = RainAnalysis.Analyse_Rain_Countries(
            [country_1, country_2], y1, y2)
        figure = plt.Figure(figsize=(12, 5), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, Frame)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        # df.plot(x='Year', color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=12,
        # subplots=True, title='Annual Rainfall in MM',  ylabel='Rainfall in MM', ax=ax)
        PLOT.Get_Graph_Rainfall_SubTrue(df, ax)
    except:
        _msg()
        return 0


def rainfall_by_state_comparison(Frame, country_for_states, state_name1, state_name2, Y1, Y2):
    try:
        country_f_s = country_for_states.get()
        state_1 = state_name1.get()
        state_2 = state_name2.get()
        y1 = Y1.get()
        y2 = Y2.get()
        df = RainAnalysis.Analyse_Rain_State(
            country_f_s, [state_1, state_2], y1, y2)
        figure = plt.Figure(figsize=(12, 5), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, Frame)
        chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

        # df.plot(x='Year', color='blue', marker='o', linestyle='dashed', linewidth=2,
        # markersize=12,subplots=True, title='Annual Rainfall in MM',  ylabel='Rainfall in MM', ax=ax)
        PLOT.Get_Graph_Rainfall_SubTrue(df, ax)
    except:
        _msg()
        return 0


# Single Country
def countryBox(Frame):
    country_name = tkinter.StringVar()
    st_year = tkinter.IntVar()
    f1 = tkinter.LabelFrame(Frame, text="Analysis by country",bg='honeydew2',font=("Courier",14))
    f1.grid(column=0, row=0, padx=8, pady=2)

    l1 = tkinter.Label(f1, text="Enter Country Name :",bg='honeydew2',font=("dongle", 10)).grid(
        column=0, row=0, padx=8, pady=4)

    e1 = tkinter.Entry(f1, textvariable=country_name).grid(
        column=1, row=0, padx=8, pady=4)
    scale_label = tkinter.Label(f1, text="Select Year ",bg='honeydew2',font=("dongle", 10)).grid(
        row=1, column=0, columnspan=3)
    s1 = tkinter.Scale(f1, from_=1901, to=2020, orient=tkinter.HORIZONTAL, variable=st_year).grid(
        row=2, columnspan=3)
    b1 = tkinter.Button(f1, text="show", command=lambda: rainfall_by_country(Frame, country_name, st_year),bg='goldenrod1').grid(
        row=3, columnspan=3, pady=2)


# Single Country
def countryBox(Frame):
    country_name = tkinter.StringVar()
    st_year = tkinter.IntVar()
    en_year = tkinter.IntVar()
    f1 = tkinter.LabelFrame(
        Frame, text="Analysis by country",bg='honeydew2',font=("Courier",14))
    f1.grid(column=0, row=0, padx=8, pady=4)

    l1 = tkinter.Label(f1, text="Enter Country Name :",bg='honeydew2',font=("dongle", 10)).grid(
        column=0, row=0, padx=8, pady=4)

    e1 = tkinter.Entry(f1, textvariable=country_name).grid(
        column=1, row=0, padx=8, pady=4)
    scale_label = tkinter.Label(f1, text="From Year ",bg='honeydew2',font=("dongle", 10)).grid(
        row=1, column=0)
    s1 = tkinter.Scale(f1, from_=1901, to=2020, orient=tkinter.HORIZONTAL, variable=st_year).grid(
        row=2, column=0)
    scale_label_2 = tkinter.Label(f1, text="To Year ",bg='honeydew2',font=("dongle", 10)).grid(
        row=1, column=1)
    s1_2 = tkinter.Scale(f1, from_=1950, to=2020, orient=tkinter.HORIZONTAL, variable=en_year).grid(
        row=2, column=1)
    b1 = tkinter.Button(f1, text="show", command=lambda: rainfall_by_country(Frame, country_name, st_year, en_year),bg='goldenrod1').grid(
        row=3, columnspan=3, pady=2)


# Compare Countries
def countriesBox(Frame):
    country_name1 = tkinter.StringVar()
    country_name2 = tkinter.StringVar()
    s_year = tkinter.IntVar()
    e_year = tkinter.IntVar()
    f2 = tkinter.LabelFrame(
        Frame, text="Compare countries",bg='honeydew2',font=("Courier",14))
    f2.grid(column=1, row=0, padx=8, pady=4)

    l1_1 = tkinter.Label(f2, text="Enter First Country Name :",bg='honeydew2',font=("dongle", 10)).grid(
        column=0, row=0, padx=8, pady=4)

    e1_1 = tkinter.Entry(f2, textvariable=country_name1).grid(
        column=1, row=0, padx=8, pady=4)

    l2_1 = tkinter.Label(f2, text="Enter Second Country Name :",bg='honeydew2',font=("dongle", 10)).grid(
        column=0, row=1, padx=8, pady=4)

    e2_1 = tkinter.Entry(f2, textvariable=country_name2).grid(
        column=1, row=1, padx=8, pady=4)
    scale1_label = tkinter.Label(
        f2, text="From Year",bg='honeydew2').grid(row=2, column=0)
    s2 = tkinter.Scale(f2, from_=1901, to=2020, orient=tkinter.HORIZONTAL,
                       variable=s_year).grid(row=3, column=0)
    scale1_label_2 = tkinter.Label(
        f2, text="To Year",bg='honeydew2').grid(row=2, column=1)
    s2_2 = tkinter.Scale(f2, from_=1950, to=2020, orient=tkinter.HORIZONTAL,
                         variable=e_year).grid(row=3, column=1)
    b2 = tkinter.Button(f2, text="show", command=lambda: rainfall_by_country_comparison(Frame, country_name1, country_name2, s_year, e_year),bg='goldenrod1').grid(
        row=4, columnspan=2, pady=2)


# Single State
def stateBox(Frame):
    state_name = tkinter.StringVar()
    Country_for_state = tkinter.StringVar()
    year1 = tkinter.IntVar()
    year2 = tkinter.IntVar()
    f3 = tkinter.LabelFrame(
        Frame, text="Analysis by State",bg='honeydew2',font=("Courier",14))
    f3.grid(column=2, row=0, padx=8, pady=4)

    l_c = tkinter.Label(f3, text="Enter Country Name:",bg='honeydew2',font=("dongle", 10)).grid(
        column=0, row=0, padx=8, pady=4)

    e_c = tkinter.Entry(f3, textvariable=Country_for_state).grid(
        column=1, row=0, padx=8, pady=4)

    l3 = tkinter.Label(f3, text="Enter State Name :",bg='honeydew2',font=("dongle", 10)).grid(
        column=0, row=1, padx=8, pady=4)

    e3 = tkinter.Entry(f3, textvariable=state_name).grid(
        column=1, row=1, padx=8, pady=4)

    y_label = tkinter.Label(f3, text="From Year",bg='honeydew2',font=("dongle", 10)).grid(row=2, column=0)

    Y_scale = tkinter.Scale(f3, from_=1901, to=2020, orient=tkinter.HORIZONTAL,
                            variable=year1).grid(row=3, column=0)
    y_label = tkinter.Label(f3, text="To Year",bg='honeydew2',font=("dongle", 10)).grid(row=2, column=1)

    Y_scale = tkinter.Scale(f3, from_=1950, to=2020, orient=tkinter.HORIZONTAL,
                            variable=year2).grid(row=3, column=1)

    b3 = tkinter.Button(f3, text="show",  command=lambda: rainfall_by_state(Frame, Country_for_state, state_name, year1, year2),bg='goldenrod1').grid(
        row=4, columnspan=2, pady=2)


# Compare states
def statesBox(Frame):
    country_for_states = tkinter.StringVar()
    state_name1 = tkinter.StringVar()
    state_name2 = tkinter.StringVar()
    Y1 = tkinter.IntVar()
    Y2 = tkinter.IntVar()
    f4 = tkinter.LabelFrame(
        Frame, text="Compare states",bg='honeydew2',font=("Courier",14))
    f4.grid(column=3, row=0, padx=8, pady=4)

    l_c_1 = tkinter.Label(f4, text="Enter Country Name:",bg='honeydew2',font=("dongle", 10)).grid(
        column=0, row=0, padx=8, pady=4)

    e_c_1 = tkinter.Entry(f4, textvariable=country_for_states).grid(
        column=1, row=0, padx=8, pady=4)

    l3_1 = tkinter.Label(f4, text="Enter First State Name :",bg='honeydew2',font=("dongle", 10)).grid(
        column=0, row=1, padx=8, pady=4)

    e3_1 = tkinter.Entry(f4, textvariable=state_name1).grid(
        column=1, row=1, padx=8, pady=4)

    l3_1 = tkinter.Label(f4, text="Enter Second State Name :",bg='honeydew2',font=("dongle", 10)).grid(
        column=0, row=2, padx=8, pady=4)

    e3_1 = tkinter.Entry(f4, textvariable=state_name2).grid(
        column=1, row=2, padx=8, pady=4)

    state_s_label = tkinter.Label(
        f4, text="From Year",bg='honeydew2',font=("dongle", 10)).grid(row=3, column=0)
    state_scale = tkinter.Scale(f4, from_=1901, to=2020, orient=tkinter.HORIZONTAL,
                                variable=Y1).grid(row=4, column=0)
    state_s_label = tkinter.Label(
        f4, text="To Year",bg='honeydew2',font=("dongle", 10)).grid(row=3, column=1)
    state_scale = tkinter.Scale(f4, from_=1950, to=2020, orient=tkinter.HORIZONTAL,
                                variable=Y2).grid(row=4, column=1)
    b4 = tkinter.Button(f4, text="show", command=lambda: rainfall_by_state_comparison(Frame, country_for_states, state_name1, state_name2, Y1, Y2),bg='goldenrod1').grid(
        row=5, columnspan=2, pady=2)
