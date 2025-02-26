from pyfirmata import Arduino, util
import serial 
import time
import matplotlib.pyplot as plt
import json #could do .txt, lets test json first 
#import pandas as pd
#fake push
board = Arduino("COM3")
voltage = 0.0

it = util.Iterator(board)
it.start()

pin = board.get_pin('a:5:i') #a for analog, 5 for pin number, i for input 
#define array to store values, maybe add to dataframe 
volt_data = []
duration = int(input())
start = time.time()

while time.time() - start < duration: #make while loop time based  - done
    sensorVal = pin.read()
    
    if sensorVal is None: 
        print("No reading found...")
        break
    
    voltage = sensorVal * (5.0 / 1023.0)


    print(" ")
    volt_data.append(voltage)
    print(f"Voltage: {voltage}")


    time.sleep(1) #parameter is in seconds

board.exit()
fileName = input("File name?")
x_axis = list(range(len(volt_data)))  # this will only work for 1s increments which is not reasonable
#potential idea: record elapsed time in its own array right after volt_data.append(voltage), so it would time.time()-start

with open(f"data_collected/{fileName}.json", "w") as json_file:
    json.dump({"Time": x_axis, "Voltage": volt_data}, json_file, indent = 1)

plt.figure(figsize=(10, 5))
plt.plot(x_axis, volt_data, linestyle='-', color = 'g', label='Voltage (V)')
plt.title("Voltage/Time")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)") 
plt.legend()
plt.grid(True)
plt.savefig(f'data_collected/{fileName}.png', dpi=300)
plt.show()

print("JSON and PNG files saved")

