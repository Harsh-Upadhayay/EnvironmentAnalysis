from Climate.Temperature.USA import TemperatureAnalysisUS as analysis
import matplotlib.pyplot as plt

df = analysis().citiesAnalysis(['NewYork', 'Seattle'], month='June', day=17)
df.plot(x = 'Date')

plt.show()
print(df)