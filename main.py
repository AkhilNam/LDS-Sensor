from pyfirmata import Arduino, util
import time
import matplotlib.pyplot as plt
#import pandas as pd
board = Arduino('COM3')
voltage = 0.0

it = util.Iterator(board)
it.start()

pin = board.get_pin('a:5:i') #a for analog, 5 for pin number, i for input 
#define array to store values, maybe add to dataframe 

volt_data = []

while True: #make while loop time based 
    sensorVal = pin.read()
    
    if sensorVal is None: 
        print("No reading found...")
        break
    
    voltage = sensorVal * (5.0 / 1023.0)


    print(" ")
    volt_data.append(voltage)
    print(f"Voltage: {voltage}")


    time.sleep(1) #parameter is in seconds





