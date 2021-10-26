# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 07:40:54 2021

@author: admin
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#Browse = webdriver.Firefox(executable_path = r"C:\Users\admin\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe")

def Download(Ind):
    

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    Drive = webdriver.Chrome(executable_path = r"C:\Users\admin\Downloads\chromedriver_win32\chromedriver.exe")
    
    Drive.get('https://climateknowledgeportal.worldbank.org/download-data')
    
    Drive.maximize_window()
    
    Drive.implicitly_wait(30)
    Search = WebDriverWait(Drive, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'TIMESERIES')))
    Search.click()
    
    
    Drive.execute_script("window.scrollBy(0, 430)")
    
    WebDriverWait(Drive, 10)
    
    Sel = Select(Drive.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/section/div/section/div/div/div[3]/form/div[1]/div/select"))
    #print([o.text for o in Sel.options])
    Sel.select_by_index(0)
    
    '''
    for o in Sel.options:
        if o.text == 'Observed data (CRU)':
            Sel.select_by_visible_text(o.text)
            #print('Yes')'''
            
    WebDriverWait(Drive, 10)
    
    
    
    Sel1 = Select(Drive.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/section/div/section/div/div/div[3]/form/div[2]/div/select"))
    #print([r.text for r in Sel1.options])
    Sel1.select_by_index(4)
    
    
    
    '''
    for r in Sel1.options:
        if r.text == 'Precipitation':
            Sel1.select_by_index(4)
            #print('Yes')
            break'''
    
    WebDriverWait(Drive, 10)
    
    
    
    Sel2 = Select(Drive.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/section/div/section/div/div/div[3]/form/div[3]/div/select"))
    #print([p.text for p in Sel2.options])
    Sel2.select_by_index(1)
    
    
    
    '''
    for p in Sel2.options:
        if p.text == 'Annual':
            Sel2.select_by_index(1)
            #print('Yes')
            break'''
        
    WebDriverWait(Drive, 10)
    
    
    
    Sel3 = Select(Drive.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/section/div/section/div/div/div[3]/form/div[4]/div/select"))
    #print([s.text for s in Sel3.options])
    Sel3.select_by_index(1)
    
    
    '''
    for s in Sel3.options:
        if s.text == 'Country + Sub-national units':
            Sel3.select_by_index(1)
            #print('Yes')
            break'''
        
    WebDriverWait(Drive, 10)
    
    
    
    Sel4 = Select(Drive.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/section/div/section/div/div/div[3]/form/div[5]/div/select"))
    #print([t.text for t in Self4.options])
    Sel4.select_by_index(Ind)
    
    
    '''
    for t in Sel4.options:
        #print(t.text)
        Sel4.select_by_index(Ind)
        #print('Yes')
        break '''
    
    Drive.implicitly_wait(50)
    
    #WebDriverWait(Drive, 40)
    
    #sleep(10)
    #Var = Drive.find_element(By.LINK_TEXT,"DOWNLOAD CSV")
    #Var.click()
    
    
    sleep(2)
    
    
    
    Val = Drive.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/section/div/section/div/div/div[3]/form/div[10]/div/button")
    Val.click()
    sleep(11)
    
    
    
    
    
    
    '''
    Var = Drive.find_element(By.ID,"submit")
    Var = WebDriverWait(Drive, 10).until(EC.presence_of_element_located((By.LINK_TEXT,"DOWNLOAD CSV")))
    #Var = Drive.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/section/div/section/div/div/div[3]/form/div[10]/div/button")
    #Var = WebDriverWait(Drive, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/main/div/div/section/div/section/div/div/div[3]/form/div[10]/div/button")))
    #Var = Drive.find_element_by_link_text('DOWNLOAD CSV')
    Var.click()
    sleep(10)
    Var = WebDriverWait(Drive, 10).until(EC.element_to_be_clickable())
    #Val = Drive.find_element(By.XPATH,"/html/body/div[1]/div/main/div/div/section/div/section/div/div/div[3]/form/div[10]/div/button")
    
    Var.click()'''
        


#WebDriverWait(Drive, 10).until(EC.element_to_be_selected())


'''
Sel = Select(Drive.find_element_by_id('variable'))
Drive.implicitly_wait(2)
Sel.select_by_value('tas')'''

#Sel1 = Select(Drive.find_element_by_id('aggregation'))
#Sel1.select_by_value('annual')


'''

sleep(4)

#Sel = Select(Drive.find_element_by_id('collection'))

Sel1 = Select(Drive.find_element_by_id('variable'))

sleep(4)
Sel1.select_by_visible_text('')

sleep(4)

Sel2 = Select(Drive.find_element_by_id('aggregation'))
sleep(10)

Sel2.select_by_visible_text('Annual')
sleep(10)

Sel3 = Select(Drive.find_element_by_id('type'))

Sel3.select_by_visible_text('Country + Sub-national')'''









for i in range(220,235):
    print(i)
    Download(i)
    






            
            
    
        
        