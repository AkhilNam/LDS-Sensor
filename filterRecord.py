import serial
import time
import matplotlib.pyplot as plt
import json
import numpy as np
import os

# === Step 1: Serial Setup ===
board = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
time.sleep(2)  # Wait for connection
print("Connected to Arduino on COM3")

volt_data = []
time_data = []

duration = 7
start_time = time.time()

while time.time() - start_time < duration:
    line = board.readline().decode().strip()
    if not line:
        print("No data received")
        continue

    voltage = float(line)
    elapsed_time = time.time() - start_time
    volt_data.append(voltage)
    time_data.append(elapsed_time)

    time.sleep(0.5)  # Match delay in Arduino

board.close()

# === Step 2: Save new data ===
mean_voltage = np.mean(volt_data)
file_name = f"avg_{mean_voltage:.3f}V"
os.makedirs("calibrationErrors", exist_ok=True)
os.makedirs("data_collected", exist_ok=True)

data_path = f"calibrationErrors/{file_name}.json"
with open(data_path, "w") as json_file:
    json.dump({"Time": time_data, "Voltage": volt_data}, json_file, indent=2)

plt.figure(figsize=(10, 5))

# Loop through all JSON files
for file in os.listdir("calibrationErrors"):
    if file.endswith(".json"):
        with open(os.path.join("calibrationErrors", file), "r") as f:
            data = json.load(f)
            avg_voltage = np.mean(data["Voltage"])
            label = f"{file.replace('.json', '')} - avg: {avg_voltage:.2f} V"
            plt.plot(data["Time"], data["Voltage"], label=label)
    

plt.title("Voltage vs Time (Overlayed Runs)")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid(True)

plot_path = f"calibrationErrors/overlay_{file_name}.png"
plt.savefig(plot_path, dpi=300)
plt.show()

print(f"Average Voltage: {np.mean(volt_data):.3f} V")
