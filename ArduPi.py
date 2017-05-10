import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit
import pandas as pd
from Modelrithm import Modelrithm
import numpy as np
import time 
import sys

values = []

plt.ion()
cnt=0

serialArduino = serial.Serial('com3', 115200)

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
for i in range(0,26):
    values.append(0)

# heart rate maximum = 220 - age
# target heart rate  = within the range of 50 to 85 percent of your maximum heart rate

def Countdown(t):
    for i in range(t,0,-1):
        print("Please wait %d seconds for the pulse sensor to adjust to your ear pulse..." % i,
        sys.stdout.flush())
        time.sleep(1)
    return

Countdown(10)

age = input("What is your age?\n")
athletics = input("Are you an athlete? (Y/N)\n")

# while True:
for i in range(3000):
    while (serialArduino.inWaiting()==0):
        pass
    print("reading line...")
    valueRead = serialArduino.readline(500)

    #check if valid value can be casted
    try:
        valueInInt = int(valueRead)
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

with open('Real_Values.txt', 'w') as data:
    data.write(str(values).strip('[]'))

array_values = np.array(values)

def Analysis():
    maximum = 220 - int(age)
    target = (maximum*.5,  maximum*.60)
    print("\nYour TARGET heart rate range is in: {} BPM during moderately intense physical activity\n".format(target))
    print("Your average RESTING heart rate is: {} BPM\n".format(np.mean(array_values)))
    print("Your instantaneous heart rate tended to deviate by: {}\n".format(np.std(array_values)))
    if int(age) in range(0, 90):
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
    return 

Analysis()


# from sklearn.cross_validation import train_test_split

# trainX, testX, trainY, testY = train_test_split()

# model.fit(trainX, trainY)
# predicted = model.predict(testX)

# with open('PredictedValues.csv', 'w') as pred:
#     pred.write(predicted)
