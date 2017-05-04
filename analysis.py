import pandas as pd
from sklearn.linear_model import SGDRegressor

values = pd.read_csv('Values.csv')

train_size = int(len(values)*0.67)
test_size = len(values) - train_size
train, test = values[0:train_size,:], values[train_size:len(values),:]
## print(len(train), len(test))

def create_dataset(values, look_back): #look back is the last time point each point references
    dataX, dataY = [],[]
    for i in range(len(values)-look_back-1):
        a = values[i:(i+look_back),0]
        dataX.append(a)
        dataY.append(values[i + look_back, 0])
    return np.array(dataX), np.array(dataY)
#create the new values 
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)

model = SGDRegressor()
model.fit(trainX, trainY)
predicted = model.predict(testX)

with open('PredictedValues.csv', 'w') as pred:
	pred.write(predicted)