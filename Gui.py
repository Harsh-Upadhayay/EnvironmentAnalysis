from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

win = Tk()
win.title("Python Mini Project")
win.attributes('-zoomed',True)

#style = ttk.Style()
#style.theme_settings("default", {"TNotebook.Tab": {"configure": {"padding": [30, 30],"background":"#3399FF",}}})

style = ttk.Style()
style.theme_settings("default", { "TNotebook.Tab": { "configure": {"padding": [20,20]},
       "map": { "background": [ ("active", "green"), ("!disabled", "orange")], "fieldbackground": [("!disabled", "blue")],
           "foreground": [("focus", "blue"),("!disabled", "black"),("active",'red')]}}})




# Nexted Temperature Tab

def TempNotebook(Tempframe):
    Tempframe.pack(expand = True,fill = 'both')
    GlobalNotebook = Frame(Tempframe)
    Tempframe.add(GlobalNotebook,text = "Global_Corrupted_Dataset")

    GlobalWBDNoteBook = Frame(Tempframe)
    Tempframe.add(GlobalWBDNoteBook,text = "Global_WBD_Dataset")

    IndiaNoteBook = Frame(Tempframe)
    Tempframe.add(IndiaNoteBook,text = "India_Dataset")

    USANoteBook = Frame(Tempframe)
    Tempframe.add(USANoteBook, text = "USA_Dataset")


# About Tab

def About(notebook):
    AbtFrame = Frame(notebook)
    notebook.add(AbtFrame,text = 'About')





# Temperature tab

def Temp(notebook):
    TempFrame = Frame(notebook)
    notebook.add(TempFrame,text = 'Temperature')
    Tempframe = ttk.Notebook(TempFrame)
    TempNotebook(Tempframe)

    #TempNotebook(TempFrame)




# Rainfall Tab

def Rain(notebook):
    RainFrame = Frame(notebook)
    notebook.add(RainFrame,text = "Rainfall")




# Main Program

def Home():
    notebook = ttk.Notebook(win,width = 100)
    notebook.pack(expand = 0, fill = 'both')
    About(notebook)
    Temp(notebook)
    Rain(notebook)





Home()
win.mainloop()
