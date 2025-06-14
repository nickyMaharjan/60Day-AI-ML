import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("iris-data.csv")
print(data.head())
print(data.describe())

print(data.info())

print("Check Duplicate:")
print(data.duplicated())

print("Unique Species:")
print(data['species'].unique())

#to display no. of samples on each class
print("Value Counts of each one:")
print(data['species'].value_counts())

#check for null values
print(data.isnull())
print("Total no. of NUll value")
print(data.isnull().sum())

# #Histogram
# data['sepal-length'].hist()
# plt.xlabel('Sepal Length')
# plt.ylabel('Frequency')
# plt.title('Histogram of Sepal Length')
#
# plt.show()

# Scatter Plot
# colors = ['red', 'orange', 'blue']
# species = ['Iris-virginica', 'Iris-versicolor', 'Iris-setosa']
#
# for i in range(3):
#     x = data[data['species'] == species[i]]
#     plt.scatter(x['sepal-length'], x['sepal-width'], c=colors[i], label=species[i])
#
# plt.xlabel("Sepal length")
# plt.ylabel("Sepal width")
# plt.title("Sepal Length vs Sepal Width by Species")
# plt.legend()
#
# plt.show()

label_encoder=LabelEncoder()
label_encoder.fit_transform(data['species'])
data['species']=label_encoder.fit_transform(data['species'])
print(data.head())
print(data.corr())

corr = data.corr()
fig, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(corr, annot=True, ax=ax, cmap='coolwarm')

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
