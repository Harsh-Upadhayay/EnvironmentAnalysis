import pyautogui as pt
import pyperclip as pp
import time 


i = 1
xTab, yTab = 400, 10

while 1:
    try:
        xRoot, yRoot = pt.locateCenterOnScreen(r"Extras\baseLocn.png", confidence=0.7)
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