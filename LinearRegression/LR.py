import pandas as pd
from sklearn.linear_model import LinearRegression
import pylab as pl
import numpy as np

values = pd.read_table('../Real_Values.txt')

train_size = int(len(values)*0.5) 
test_size = len(values) - train_size
train, test = values[0:(train_size +1)], values[train_size:len(values)]
## print(len(train), len(test))

# Linear Regression Model (on Pulse Sensor Values)
model = LinearRegression()
model.fit(train, test)
predicted = model.predict(test)

with open('PredValues.txt', 'w') as pred:
	for line in predicted:
		pred.write(str(line).strip('[ ]') + '\n')

predicted = list(predicted)
pl.figure()
pl.plot(np.arange(80, 121), predicted, 'b', label='Predicted Values', linewidth=3)
pl.plot(np.arange(0, len(values)), values, 'r', label='Given Data', linewidth=3)
pl.legend()
pl.title('Standard Linear Regression')
pl.ylabel('BPM')
pl.xlabel('Sample')
pl.show()
pl.savefig('StandardLR.png')
