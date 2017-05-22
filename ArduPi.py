import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit
import pandas as pd
import numpy as np
import time 
import sys
import os

values = []

plt.ion()
cnt=0

serialArduino = serial.Serial('com3', 9600) #could also be set to 115200

def plotValues():
    plt.title('Serial value from Arduino')
    plt.grid(True)
    plt.ylabel('Values')
    plt.plot(values, 'rx-', label='values')
    plt.legend(loc='upper right')

def doAtExit():
    serialArduino.close()
    print("Close serial")
    print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

atexit.register(doAtExit)

print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

#pre-load dummy data
for i in range(0,100):
    values.append(0)

# heart rate maximum = 220 - age
# target heart rate  = within the range of 50 to 85 percent of your maximum heart rate

def Countdown(t):
    for i in range(t,0,-1):
        print("Please wait %d seconds for the pulse sensor to adjust to your ear pulse..." % i,
        sys.stdout.flush())
        time.sleep(1)

setup = input('Please place the clip part of the pulse sensor on the back of your earlobe, and breathe normally.')

Countdown(30)

age = input("\nWhat is your age?\n")
athletics = input("Are you an athlete? (Y/N)\n")

for i in range(4000):
    while (serialArduino.inWaiting()==0):
        pass
    print("reading line...")
    valueRead = serialArduino.readline(500) #500

    #check if valid value can be casted
    try:
        valueInInt = float(valueRead)
        print(valueInInt)
        if valueInInt <= 1024:
            if valueInInt >= 0:
                values.append(valueInInt)
                values.pop(0)
                drawnow(plotValues)
            else:
                print("Invalid! negative number")
        else:
            print("Invalid! too large")
    except ValueError:
        print("---")

# Remove biggest outliers if there is a huge deviation from the mean
while (max(values) - np.mean(values)) > 40 :
    mymax = max(values)
    values.remove(mymax)
while (np.mean(values) - min(values)) > 40:
    mymin = min(values)
    values.remove(mymin)

#Remove all zeroes
while values.count(0) >= 1:
    values.remove(0)

#Output values to a txt file
with open('Real_Values.txt', 'w') as data:
    for line in values:
        data.write(str(line) + '\n')

array_values = np.array(values)

def Analysis():
    maximum = 220 - int(age)
    target = (maximum*.5,  maximum*.60)
    print("\nYour TARGET heart rate range is in: {} BPM during moderately intense physical activity\n".format(target))
    print("Your average RESTING heart rate is: {} BPM\n".format(np.mean(array_values)))
    print("Your instantaneous heart rate tended to deviate by: {}\n".format(np.std(array_values)))
    
    if int(age) in range(0, 100):
        if np.mean(array_values) >= 60 and np.mean(array_values) <= 100:
            print("You have a healthy resting heart rate\n")

        elif np.mean(array_values) > 100:
                print("You are at risk for tachychardia, please consult your doctor.\n")

        elif np.mean(array_values) < 60 and np.mean(array_values) >=40:
            if athletics == 'Y' or athletics == 'y':
                print("You have a healthy resting heart rate\n")
            else:
                print("You are at risk for bradychardia, please consult your doctor.\n")
        else:
                print("You are at risk for bradychardia, please consult your doctor.\n")
    else:
        print('Please enter a valid age')

Analysis()

#doAtExit()

exec(open('predictive_analysis.py').read())

