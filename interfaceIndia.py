import Climate.Temperature.India as India

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


def India_TA(placeHolder, month):
    try :
        month = month.get()
    except :
        month = 'May'

    df = India.Temperature_Analysis_India(month)
    figure = plt.Figure(figsize=(10, 6), dpi=100)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, placeHolder)
    chart_type.get_tk_widget().grid(column=0, row=1, columnspan=4)
    
    df.plot(x = 'Year', subplots=False,  ylabel='Temperature in degree celsius', ax=ax)
    

def IndiaBox(placeHolder, firstMessage, secondMessage, firstPos = 0):
    try :    
        month = tkinter.StringVar()

        f1 = tkinter.LabelFrame(placeHolder, text=firstMessage)
        f1.grid(column=firstPos, row=0, padx=8, pady=2)

        l1 = tkinter.Label(f1, text=secondMessage).grid(
            column=0, row=0, padx=8, pady=4)

        e1 = tkinter.Entry(f1, textvariable=month).grid(
            column=1, row=0, padx=8, pady=4)

        b1 = tkinter.Button(f1, text="show", command=lambda : India_TA(placeHolder, month)).grid(
            row=2, columnspan=2, pady=2)
    except :
        _msg()


IndiaBox(Tmp_analysis, "India Analysis", "Enter Month (required)", 0)
win.mainloop()
