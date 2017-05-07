import pandas as pd
from sklearn.linear_model import LinearRegression

# Linear Regression Model (on MIT_2)
values = pd.read_csv('MIT_2.txt')

train_size = int(len(values)*0.5) 
test_size = len(values) - train_size
train, test = values[0:(train_size +1)], values[train_size:len(values)]
## print(len(train), len(test))

model = LinearRegression()
model.fit(train, test)
predicted = model.predict(test)

with open('SampleLR_2_PredValues.txt', 'w') as pred:
	for line in predicted:
		pred.write(str(line).strip('[ ]') + '\n')


