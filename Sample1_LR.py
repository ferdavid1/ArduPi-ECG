import pandas as pd
from sklearn.linear_model import LinearRegression

values = pd.read_csv('MIT_1.txt')

train_size = int(len(values)*0.5) 
test_size = len(values) - train_size
train, test = values[0:(train_size +1)], values[train_size:len(values)]
## print(len(train), len(test))

# Linear Regression Model (on MIT_1)
model = LinearRegression()
model.fit(train, test)
predicted = model.predict(test)

with open('SampleLR_1_PredValues.txt', 'w') as pred:
	for line in predicted:
		pred.write(str(line).strip('[ ]') + '\n')
