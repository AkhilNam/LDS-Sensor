import serial
import time
import matplotlib.pyplot as plt
import json


board = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
time.sleep(2)  # Wait for connection
print("Connected to Arduino on COM3")


volt_data = []
time_data = []

duration = int(input("Enter duration in seconds: "))
start_time = time.time()

while time.time() - start_time < duration:
    line = board.readline().decode().strip()  # Read  data

    if not line:
        print("No data received")
        continue

    voltage = float(line)
    elapsed_time = time.time() - start_time
    volt_data.append(voltage)
    time_data.append(elapsed_time)
    

    time.sleep(0.5)  #Parameter for sleep is the interval -- match delay in arduino program in ms

board.close()  

file_name = input("Enter file name: ")

data_path = f"data_collected/{file_name}.json"
with open(data_path, "w") as json_file:
    json.dump({"Time": time_data, "Voltage": volt_data}, json_file, indent=2)


plt.figure(figsize=(10, 5))
plt.plot(time_data, volt_data, linestyle='-', color='g', label='Voltage (V)')
plt.title("Voltage vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid(True)

plot_path = f"data_collected/{file_name}.png"
plt.savefig(plot_path, dpi=300)
plt.show()
