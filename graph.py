import matplotlib.pyplot as plt
import json

with open('data_collected/ActualFinalNewSensor.json', 'r') as f1:
    data1 = json.load(f1)

with open('data_collected/NewSensorFinal.json', 'r') as f2:
    data2 = json.load(f2)

with open('data_collected/oldSensTimeSeries.json', 'r') as f3:
    data3 = json.load(f3)

time1, voltage1 = data1['Time'], data1['Voltage']
time2, voltage2 = data2['Time'], data2['Voltage']
time3, voltage3 = data3['Time'], data3['Voltage']

plt.plot(time1, voltage1, label='3.547 mL of Sucrose')
plt.plot(time2, voltage2, label='2.567 mL of Sucrose')
plt.plot(time3, voltage3, label='2.440 mL of Sucrose ')

plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Overlayed Voltage vs Time Data')
plt.legend()
plt.grid(True)

# Display the plot
plot_path = f"data_collected/overlayedOldSensor.png"
plt.savefig(plot_path, dpi=300)
plt.show()
