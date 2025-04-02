# Arduino Sensor Data Collection Project

## Overview
This project interfaces an Arduino with a computer to collect, analyze, and visualize voltage data from analog sensors. The system records voltage readings at regular intervals, saves the data to JSON files, and generates visualizations for analysis.

## Components
- **Arduino**: Reads analog sensor data and sends values via serial connection
- **Python Scripts**: Process, store, and visualize the sensor data
- **Data Storage**: JSON files organized in two directories: `calibrationErrors/` and `data_collected/`

## Hardware Requirements
- Arduino board (with analog input capability)
- Analog sensor connected to Arduino pin A5
- USB cable for computer-Arduino connection

## Software Requirements
- Arduino IDE
- Python 3.12
- Python libraries:
  - `pyserial`
  - `matplotlib`
  - `numpy`

## File Descriptions

### Arduino Code
- **`arduinoToPy.ino`**: Arduino sketch that reads voltage from analog pin A5, converts it to a voltage value (0-5V), and sends readings via serial communication at 500ms intervals.

### Python Scripts
- **`serialMain.py`**: Main data collection script that:
  - Establishes serial connection with Arduino
  - Collects voltage data for a user-specified duration
  - Saves data to a JSON file with a user-specified filename
  - Generates and saves a voltage vs. time plot

- **`filterRecord.py`**: Enhanced data collection script that:
  - Collects voltage data from Arduino
  - Calculates the mean voltage
  - Saves data to a JSON file named based on the mean voltage
  - Generates overlay plots of all calibration runs
  - Organizes files in the `calibrationErrors/` directory

- **`graph.py`**: Visualization script for comparing three specific sucrose samples:
  - Loads data from three JSON files (2.72mL, 3.24mL, 3.87mL of sucrose)
  - Creates an overlay plot comparing voltage readings
  - Saves the visualization to `data_collected/overlayedOldSensor.png`

- **`graph2.py`**: Additional visualization script comparing two different sucrose samples:
  - Loads data from two JSON files
  - Creates an overlay plot
  - Saves the visualization to `data_collected/overlayedNewSensor.png`

- **`main.py`**: Utility script to calculate and print the mean voltage from a specific data file (3.24mL.json)

## Setup Instructions

### Arduino Setup
1. Connect your analog sensor to Arduino pin A5
2. Connect Arduino to computer via USB
3. Upload `arduinoToPy.ino` to your Arduino using the Arduino IDE

### Python Environment Setup
1. Install required Python packages:
   ```
   pip install pyserial matplotlib numpy
   ```
2. Create directories for data storage:
   ```
   mkdir calibrationErrors
   mkdir data_collected
   ```

## Usage

### Basic Data Collection
Run `serialMain.py` to collect and visualize sensor data:
```
python serialMain.py
```
You will be prompted to:
1. Enter duration in seconds for data collection
2. Enter a filename to save the data

### Calibration and Error Analysis
Run `filterRecord.py` to collect data and automatically analyze it against previous calibration runs:
```
python filterRecord.py
```

### Data Analysis
Use the graph scripts to visualize and compare multiple data sets:
```
python graph.py
python graph2.py
```

## Project Applications
This system appears to be designed for:
- Measuring and analyzing sucrose solution concentrations
- Calibrating sensors
- Monitoring voltage changes over time
- Comparing sensor readings across different experimental setups

## Notes
- The serial connection is configured for COM3 port at 9600 baud rate in most scripts but at 115200 in the Arduino sketch
- The system collects data points every 500ms
- Data files are automatically organized and named based on content
