import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json

dataset = pd.read_csv('data.csv')
x = dataset.iloc[:, :-1].values
print(x)
y = dataset.iloc[:, 1].values
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/4, random_state = 0)
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
pickle.dump(regressor, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1]]))
print(model.predict([[3]]))
print(model.predict([[7]]))