import tkinter
from tkinter import ttk

from GUI import interfaceGlobal
from GUI import interfaceRain
from GUI import interfaceIndia
from GUI import interfaceWBD
from GUI import interfaceUSA

# About Tab

def About(notebook):
    AbtFrame = tkinter.Frame(notebook)
    notebook.add(AbtFrame, text='About')
    frame1 = tkinter.LabelFrame(AbtFrame, text="Analysis of Climate Change")
    frame1.grid(column=0, row=0, padx=8, pady=4)

    para = tkinter.Label(frame1, text="The program will analyze changes in the climate over an interval . It will also generate the distribution curve of the data. ")
    para.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady=10)

    frame2 = tkinter.LabelFrame(AbtFrame, text="Tech stack")
    frame2.grid(column=0, row=1, padx=8, pady=4)

    para2_1 = tkinter.Label(frame2, text="Numpy & Scipy : Data Analysis").grid(
        column=0, row=0, sticky=tkinter.W, padx=10, pady=10)
    para2_2 = tkinter.Label(frame2, text="Pandas : Data Manipulation").grid(
        column=0, row=1, sticky=tkinter.W, padx=10, pady=10)
    para2_3 = tkinter.Label(frame2, text="Matplotlib : Data Representation").grid(
        column=0, row=2, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="CSV : File Handling").grid(
        column=0, row=3, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Pyautogui : GUI Automation").grid(
        column=0, row=4, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Selenium : Browser Automation").grid(
        column=0, row=5, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Tkinter : Python GUI").grid(
        column=0, row=6, sticky=tkinter.W, padx=10, pady=10)
    para2_4 = tkinter.Label(frame2, text="Exception Handling").grid(
        column=0, row=7, sticky=tkinter.W, padx=10, pady=10)

    frame3 = tkinter.LabelFrame(AbtFrame, text="Participants or Group info")
    frame3.grid(column=0, row=2, padx=8, pady=4)

    list_el_1 = tkinter.Label(frame3, text="1.Harsh Upadhayay").grid(
        column=0, row=0, sticky=tkinter.W, padx=10, pady=5)
    list_el_2 = tkinter.Label(frame3, text="2.Harsh Tripathi").grid(
        column=0, row=1, sticky=tkinter.W, padx=10, pady=5)
    list_el_3 = tkinter.Label(frame3, text="3.Prathamesh Patil").grid(
        column=0, row=2, sticky=tkinter.W, padx=10, pady=5)
    list_el_4 = tkinter.Label(frame3, text="4.Niraj Matere").grid(
        column=0, row=3, sticky=tkinter.W, padx=10, pady=5)
    list_el_5 = tkinter.Label(frame3, text="5.Ayush Chaurasia").grid(
        column=0, row=4, sticky=tkinter.W, padx=10, pady=5)


# Temperature tab

def Temp(notebook):
    TempFrame = tkinter.Frame(notebook)
    notebook.add(TempFrame, text='Temperature')
    Tempframe = ttk.Notebook(TempFrame)
    TempNotebook(Tempframe)


# Nested Temperature Tab

def TempNotebook(Tempframe):
    Tempframe.pack(expand=True, fill='both')
    GlobalNotebook = tkinter.Frame(Tempframe)
    Tempframe.add(GlobalNotebook, text="Global_Kaggle_Dataset")

    interfaceGlobal.countryBox(GlobalNotebook, "Countries Comparision", "Enter Countries Name (Comma Seperated)", 0)
    interfaceGlobal.stateBox(GlobalNotebook, "States Comparision", "Enter States Name (Comma Seperated)", 1)
    interfaceGlobal.cityBox(GlobalNotebook, "Cities Comparision", "Enter Cities Name (Comma Seperated)", 2)


    GlobalWBDNoteBook = tkinter.Frame(Tempframe)
    Tempframe.add(GlobalWBDNoteBook, text="Global_WBD_Dataset")

    interfaceWBD.countryBox(GlobalWBDNoteBook, "Country Analysis", "Enter Country Name", 0)
    interfaceWBD.countryBox(GlobalWBDNoteBook, "Countries Comparision", "Enter Countries Name (Comma Seperated)", 1)
    interfaceWBD.stateBox(GlobalWBDNoteBook, "State Analysis", "Enter State Name", 2)
    interfaceWBD.stateBox(GlobalWBDNoteBook, "States Comparision", "Enter States Name (Comma Seperated)", 3)

    IndiaNoteBook = tkinter.Frame(Tempframe)
    Tempframe.add(IndiaNoteBook, text="India_Dataset")
    
    interfaceIndia.IndiaBox(IndiaNoteBook, "India Analysis", "Enter Month (required)", 0)

    USANoteBook = tkinter.Frame(Tempframe)
    Tempframe.add(USANoteBook, text="USA_Dataset")
    
    interfaceUSA.cityBox(USANoteBook, "City Analysis", "Enter city Name", 0)
    interfaceUSA.cityBox(USANoteBook, "Cities Comparision", "Enter cities Name (Comma Seperated)", 1)


# Rainfall Tab

def Rain(notebook):
    RainFrame = tkinter.Frame(notebook)
    notebook.add(RainFrame, text="Rainfall")
   
    interfaceRain.countryBox(RainFrame)
    interfaceRain.countriesBox(RainFrame)
    interfaceRain.stateBox(RainFrame)
    interfaceRain.statesBox(RainFrame)


# Main Program

def main():
        
    win = tkinter.Tk()
    win.title("Python Mini Project")
    # win.attributes("-zoomed",True)
    style = ttk.Style()
    style.theme_settings
    ("default",
    {"TNotebook.Tab": {"configure": {"padding": [20, 20]},
    "map": {"background": [("active", "green"),
    ("!disabled", "orange")],
    "fieldbackground": [("!disabled", "blue")],
    "foreground": [("focus", "blue"),
    ("!disabled", "black"),
    ("active", 'red')]}}})


    notebook = ttk.Notebook(win, width=100)
    notebook.pack(expand=0, fill='both')
    About(notebook)
    Temp(notebook)
    Rain(notebook)
    win.mainloop()


if __name__ == "__main__":
    main()
