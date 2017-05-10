import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

values = pd.read_table('MIT_1.txt')

train_size = int(len(values)*0.5) 
test_size = len(values) - train_size
train, test = values[0:(train_size +1)], values[train_size:len(values)]
## print(len(train), len(test))

# Linear Regression Model (on MIT_1)
model = LinearRegression()
model.fit(train, test)
predicted = model.predict(test)

plt.figure()
plt.plot(values)
plt.plot(predicted)
plt.savefig('SampleLR_1_PredValues.png')
plt.show()

with open('SampleLR_1_PredValues.txt', 'w') as pred:
	for line in predicted:
		pred.write(str(line).strip('[ ]') + '\n')
