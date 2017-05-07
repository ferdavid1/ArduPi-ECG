import pandas as pd
from sklearn.linear_model import LinearRegression

# Linear Regression Model (on MIT_2)
values = pd.read_csv('MIT_1.txt')

train_size = int(len(values)*0.5) 
test_size = len(values) - train_size
train, test = values[0:(train_size +1)], values[train_size:len(values)]