import matplotlib.pyplot as plt
import json

with open('data_collected/LastOldSens.json', 'r') as f1:
    data1 = json.load(f1)

with open('data_collected/oldSens1.json', 'r') as f2:
    data2 = json.load(f2)


time1, voltage1 = data1['Time'], data1['Voltage']
time2, voltage2 = data2['Time'], data2['Voltage']

plt.plot(time1, voltage1, label='2.511 mL of Sucrose')
plt.plot(time2, voltage2, label='3.425 mL of Sucrose')

plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Overlayed Voltage vs Time Data')
plt.legend()
plt.grid(True)

# Display the plot
plot_path = f"data_collected/overlayedNewSensor.png"
plt.savefig(plot_path, dpi=300)
plt.show()
