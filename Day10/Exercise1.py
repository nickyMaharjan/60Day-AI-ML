import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import datetime as dt
import numpy as np

# Load dataset
df = pd.read_csv("people-10000.csv")

# Convert 'Date of birth' to datetime and calculate age
df['Date of birth'] = pd.to_datetime(df['Date of birth'], errors='coerce')
current_year = dt.datetime.now().year
df['Age'] = current_year - df['Date of birth'].dt.year

# Drop rows with missing age
df = df.dropna(subset=['Age'])

# Encode 'Sex' column
le = LabelEncoder()
df['Sex_encoded'] = le.fit_transform(df['Sex'])  # in the dataset: Female=0, Male=1

# Defining the feature
X = df[['Sex_encoded']]
y = df['Age']

# Splitting the data set test size = 20%, train size = 80%
# random_state = avoid shuffling dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression() #linear regression model
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("RMSE:", rmse) #Root Mean Squared Error: how far the predictions are from actual values
