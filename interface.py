from ctypes import alignment, sizeof
import tkinter
from tkinter import Canvas, Label, Listbox, Scrollbar, ttk, font
from tkinter.constants import CENTER
from typing import Text

from scipy.ndimage.measurements import label

from GUI import interfaceGlobal
from GUI import interfaceRain
from GUI import interfaceIndia
from GUI import interfaceWBD
from GUI import interfaceUSA

# About Tab


def About(notebook):
    AbtFrame = tkinter.Frame(notebook, bg='skyblue')
    notebook.add(AbtFrame, text='About')
    frame1 = tkinter.LabelFrame(AbtFrame, text="Analysis of Climate Change",font=("Courier", 14),bg='gold')
    frame1.grid(column=0, row=0, padx=20, pady=4)

    para = tkinter.Label(
        frame1, text="The program will analyze changes in the climate over an interval. It will also generate \nthe distribution curve of the data. ", font=("Courier", 17),bg='gold2')
    para.grid(column=0, row=0, sticky=tkinter.W, pady=10)

    frame2 = tkinter.LabelFrame(AbtFrame, text="Tech stack",bg='seagreen3',font=("Courier",14))
    frame2.grid(column=0, columnspan=2, row=1, padx=8, pady=4)

    para2_1 = tkinter.Label(frame2, text="Numpy & Scipy : Data Analysis",font=(17),bg='palegreen').grid(
        column=0, row=0, sticky=tkinter.W, padx=10, pady=10)
    para2_2 = tkinter.Label(frame2, text="Pandas : Data Manipulation",font=(17),bg='palegreen').grid(
        column=0, row=1, sticky=tkinter.W, padx=10, pady=10)
    para2_3 = tkinter.Label(frame2, text="Matplotlib : Data Representation",font=(17),bg='palegreen').grid(
        column=0, row=2, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="CSV : File Handling",font=(17),bg='palegreen').grid(
        column=0, row=3, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Pyautogui : GUI Automation",font=(17),bg='palegreen').grid(
        column=0, row=4, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Selenium : Browser Automation",font=(17),bg='palegreen').grid(
        column=0, row=5, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Tkinter : Python GUI",font=(17),bg='palegreen').grid(
        column=0, row=6, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Exception Handling",font=(17),bg='palegreen').grid(
        column=0, row=7, sticky=tkinter.W, padx=10, pady=10)


# Temperature tab

def Temp(notebook):
    TempFrame = tkinter.Frame(notebook)
    notebook.add(TempFrame, text='Temperature')
    Tempframe = ttk.Notebook(TempFrame)
    TempNotebook(Tempframe)


# Nested Temperature Tab

def TempNotebook(Tempframe):
    Tempframe.pack(expand=True, fill='both')
    GlobalNotebook = tkinter.Frame(Tempframe,border=10,bg='skyblue3')
    Tempframe.add(GlobalNotebook, text="Global_Kaggle_Dataset")

    interfaceGlobal.countryBox(
        GlobalNotebook, "Countries Comparision", "Enter Countries Name (Comma Seperated)", 0)
    interfaceGlobal.stateBox(
        GlobalNotebook, "States Comparision", "Enter States Name (Comma Seperated)", 1)
    interfaceGlobal.cityBox(
        GlobalNotebook, "Cities Comparision", "Enter Cities Name (Comma Seperated)", 2)

    GlobalWBDNoteBook = tkinter.Frame(Tempframe,border=10,bg='skyblue3')
    Tempframe.add(GlobalWBDNoteBook, text="Global_WBD_Dataset")

    interfaceWBD.countryBox(
        GlobalWBDNoteBook, "Country Analysis", "Enter Country Name", 0)
    interfaceWBD.countryBox(GlobalWBDNoteBook, "Countries Comparision",
                            "Enter Countries Name (Comma Seperated)", 1)
    interfaceWBD.stateBox(
        GlobalWBDNoteBook, "State Analysis", "Enter State Name", 2)
    interfaceWBD.stateBox(GlobalWBDNoteBook, "States Comparision",
                          "Enter States Name (Comma Seperated)", 3)

    IndiaNoteBook = tkinter.Frame(Tempframe,border=10,bg='skyblue3')
    Tempframe.add(IndiaNoteBook, text="India_Dataset")

    interfaceIndia.IndiaBox(
        IndiaNoteBook, "India Analysis", "Enter Month (required)", 0)

    USANoteBook = tkinter.Frame(Tempframe,border=10,bg='skyblue3')
    Tempframe.add(USANoteBook, text="USA_Dataset")

    interfaceUSA.cityBox(USANoteBook, "City Analysis", "Enter city Name", 0)
    interfaceUSA.cityBox(USANoteBook, "Cities Comparision",
                         "Enter cities Name (Comma Seperated)", 1)


# Rainfall Tab

def Rain(notebook):
    RainFrame = tkinter.Frame(notebook, border=10,bg='skyblue3')
    notebook.add(RainFrame, text="Rainfall")

    interfaceRain.countryBox(RainFrame)
    interfaceRain.countriesBox(RainFrame)
    interfaceRain.stateBox(RainFrame)
    interfaceRain.statesBox(RainFrame)

# Participants Tab


def Info(notebook):
    info = tkinter.Frame(notebook, background='skyblue')
    notebook.add(info, text="Participants")
    frame3 = tkinter.LabelFrame(info, text="Participants or Group info",font=("Courier", 17),bg='lightpink')
    frame3.grid(column=0, row=2, padx=8, pady=4)

    list_el_1 = tkinter.Label(frame3, text="1. Harsh Upadhayay - BT20CSE115",font=("Courier", 17),bg='honeydew2').grid(
        column=1, row=0, sticky=tkinter.W, padx=10, pady=5)
    list_el_2 = tkinter.Label(frame3, text="2. Harsh Tripathi - BT20CSE040",font=("Courier", 17),bg='honeydew2').grid(
        column=1, row=2, sticky=tkinter.W, padx=10, pady=5)
    list_el_3 = tkinter.Label(frame3, text="3. Prathamesh Patil - BT20CSE123",font=("Courier", 17),bg='honeydew2').grid(
        column=1, row=4, sticky=tkinter.W, padx=10, pady=5)
    list_el_4 = tkinter.Label(frame3, text="4. Niraj Matere - BT20CSE138",font=("Courier", 17),bg='honeydew2').grid(
        column=1, row=6, sticky=tkinter.W, padx=10, pady=5)
    list_el_5 = tkinter.Label(frame3, text="5. Ayush Chaurasia - BT20CSE149",font=("Courier", 17),bg='honeydew2').grid(
        column=1, row=8, sticky=tkinter.W, padx=10, pady=5)


# Main Program

def main():

    win = tkinter.Tk()
    win.title("Python Mini Project")
    win.state('zoomed')

    # label=Label(text="Python Mini Project : Climate Change Analysis",font=("Noto Serif",17),bg='khaki')
    # label.pack()
    # win.configure(background='gray55')

    style = ttk.Style()
    style.theme_settings
    ("default",
     {"TNotebook.Tab": {"configure": {"padding": [0, 0]},
                        "map": {"background": [("active", "green"),
                                               ("!disabled", "orange")],
                                "fieldbackground": [("!disabled", "blue")],
                                "foreground": [("focus", "blue"),
                                               ("!disabled", "black"),
                                               ("active", 'red')],font:[("15")]}}})

    notebook = ttk.Notebook(win, width=100)
    notebook.pack(expand=0, fill='both', padx=0, pady=0)
    About(notebook)
    Info(notebook)
    Temp(notebook)
    Rain(notebook)

    win.mainloop()


if __name__ == "__main__":
    main()
