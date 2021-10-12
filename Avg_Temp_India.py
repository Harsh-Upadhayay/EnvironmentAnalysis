import pandas as Pd
import numpy as nm
import csv
import matplotlib.pyplot as Plt
import time

start_time = time.time()
File = Pd.read_csv('GlobalLandTemperaturesByCountry.csv')
print(File)
print(type(File))
print(len(File))
print(File.shape)
print(File.head)
print(File.info)
print(File.describe)
print(File['dt'])

load_time = time.time() - start_time
print("Load Time : --- %s seconds ---" % (load_time))