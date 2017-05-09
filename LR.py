import pandas as pd
from sklearn.linear_model import LinearRegression

values = pd.read_table('Real_Values.txt')

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
