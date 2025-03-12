import numpy as np
import json

with open('data_collected/3.24mL.json', 'r') as f2:
    data2 = json.load(f2)

time2, voltage2 = data2['Time'], data2['Voltage']

print(np.mean(voltage2))

#ESR : Equivalent Series Resistance in Real world capacitor