import pyautogui as pt
import pyperclip as pp
import time 

CountriesMap = {}

def __setCountriesMap():
    """
    Call only once
    """
    global CountriesMap
    with open("datasets\WhoDataBank\countriesCode.txt", "r") as file:
        data = file.readlines()
        for line in data:
                word = line.split('^^^^^')
  
    for pair in word:
        x, y = pair.split('**')
        CountriesMap[y] = x


i = 148
xTab, yTab = 400, 10

while 1:
    try:
        xRoot, yRoot = pt.locateCenterOnScreen(r"Extras\baseLocn.png")
        pt.doubleClick(xRoot, yRoot)
        pt.press('tab')
        pt.press('down')
        pt.press('tab')
        pt.press('down')
        pt.press('tab')
        pt.press('down')
        pt.press('tab')
        pt.press('down', i)
        pt.press('tab')
        pt.press('enter')
        i += 1
        time.sleep(10)
    except:
        pt.click(xTab, yTab)