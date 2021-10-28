import Climate.Temperature.GlobalWBD  as globalWBD
import Climate.Temperature.Global  as golbalKaggle
import Climate.Temperature.USA as USA
import Climate.Temperature.India as India

import matplotlib.pyplot as plt




df = golbalKaggle.TemperaturesByState('Uttar Pradesh', 'January')
df.plot('dt')

plt.show()
print(df)