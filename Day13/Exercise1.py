import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import confusion_matrix

data=pd.read_csv("iris-data.csv")
print(data.head())
print(data.describe())

print(data.info())

#train - 70
#test - 30
X = data.drop(columns=['species'])
Y = data['species']
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.30)

model = LogisticRegression()

#model training
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)


y_test = np.asarray(y_test)
print(y_test)

print(confusion_matrix(y_test, y_pred))

print("Accuracy:",model.score(x_test, y_test))

print("Accuracy:",model.score(x_test, y_test)*100)

tr_train_score = model.score(x_train, y_train)

tr_test_score= model.score(x_test, y_test)

print('Logistic Regression Train Score is : ' , tr_train_score)

print('Logistic Regression Test Score is : ' , tr_test_score)