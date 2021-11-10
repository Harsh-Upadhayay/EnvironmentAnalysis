from Climate.Temperature.USA import TemperatureAnalysisUS as USA

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
from tkinter import ttk
from tkinter import messagebox as msg
import Graph.Smooth_Temperature as Smooth


def _msg():
    msg.showerror("Error", "Enter correct name!")


def USA_TA_City(placeHolder, cities, month, day, s_year, e_year):

    cities = cities.get().split(',')
    sy = s_year.get()
    ey = e_year.get()
    idx = 0
    subplotsCondition = True
    for city in cities:
        cities[idx] = city.strip()
        idx += 1
    if len(cities) == 1:
        cities = cities[0]
        # subplotsCondition = True

    month = month.get()
    if not month:
        month = 0
    day = day.get()
    if not day:
        day = 0

    df = USA().citiesAnalysis(cities, month, day, str(sy)+'-01-01', str(ey)+'-01-01')
    figure = plt.Figure(figsize=(14, 4.5), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)

    #df.plot(x = 'Date', subplots=subplotsCondition,  ylabel='Temperature in degree celsius', ax=ax)
    Smooth.Get_Graph_Temperature_SubTrue_Global(df, ax)


def cityBox(placeHolder, firstMessage, secondMessage, firstPos=0):
    try:
        cities = tkinter.StringVar()
        month = tkinter.StringVar()
        day = tkinter.IntVar()
        s_year = tkinter.IntVar()
        e_year = tkinter.IntVar()
        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage, font=(
            "Courier", 14), bg='honeydew2')
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text=secondMessage, bg='honeydew2', font=("dongle", 10)).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=cities).grid(
            column=1, row=0, padx=8, pady=4)

        l2 = tkinter.Label(f1, text="Enter month (Leave blank to take all data)", bg='honeydew2', font=("dongle", 10)).grid(
            column=0, row=1, padx=8, pady=4)

        e2 = tkinter.Entry(f1, textvariable=month).grid(
            column=1, row=1, padx=8, pady=4)

        l3 = tkinter.Label(f1, text="Enter day (Leave blank to take all data)", bg='honeydew2', font=("dongle", 10)).grid(
            column=0, row=2, padx=8, pady=4)

        e3 = tkinter.Entry(f1, textvariable=day).grid(
            column=1, row=2, padx=8, pady=4)
        scale1_label = tkinter.Label(
            f1, text="From Year").grid(row=3, column=0)
        s2 = tkinter.Scale(f1, from_=1901, to=2020, orient=tkinter.HORIZONTAL,
                           variable=s_year).grid(row=4, column=0)
        scale1_label_2 = tkinter.Label(
            f1, text="To Year").grid(row=3, column=1)
        s2_2 = tkinter.Scale(f1, from_=1903, to=2020, orient=tkinter.HORIZONTAL,
                             variable=e_year).grid(row=4, column=1)
        b1 = tkinter.Button(f1, text="show", command=lambda: USA_TA_City(placeHolder, cities, month, day, s_year, e_year), bg='goldenrod1').grid(
            row=5, columnspan=2, pady=2)
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
    cityBox(Tmp_analysis, "City Analysis", "Enter city Name", 0)
    cityBox(Tmp_analysis, "Cities Comparision",
            "Enter cities Name (Comma Seperated)", 1)

    win.mainloop()


if __name__ == "__main__":
    main()
