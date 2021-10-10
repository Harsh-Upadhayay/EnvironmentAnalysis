import pandas as pd
import numpy as np
import time
start_time = time.time()

h = pd.read_csv('GlobalLandTemperaturesByCity.csv')

load_time = time.time() - start_time

print("Load Time : --- %s seconds ---" % (load_time))



while 1:
        
    load_time = time.time() - start_time

    print("Load Time : --- %s seconds ---" % (load_time))


    print("Print Time : --- %s seconds ---" % (time.time() - start_time - load_time))
    ch = int(input())
    if 1 == ch:
        print(h)
    elif 2 == ch:
        print(h.head)
    elif 3 == ch:
        print(h.tail)
    elif 4 == ch:
        print(h.describe)
    else:
        exit()
