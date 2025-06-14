# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load the dataset
df = pd.read_csv("people-10000.csv")
print(df.head())

# # Step 3: Define your target column and features
# # Replace 'target_column_name' with the actual name of the column you're trying to predict
# target_column = 'target_column_name'  # <- UPDATE THIS
# X = df.drop(columns=[target_column])
# y = df[target_column]
#
# # Step 4: Identify column types
# numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
# categorical_features = X.select_dtypes(include=["object", "bool", "category"]).columns.tolist()
#
# # Step 5: Preprocessing for numerical and categorical data
# preprocessor = ColumnTransformer(
#     transformers=[
#         ('num', StandardScaler(), numeric_features),
#         ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
#     ])
#
# # Step 6: Build the pipeline
# pipeline = Pipeline([
#     ('preprocessor', preprocessor),
#     ('classifier', LogisticRegression(max_iter=1000))
# ])
#
# # Step 7: Split the dataset into train and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Step 8: Fit the pipeline
# pipeline.fit(X_train, y_train)
#
# # Step 9: Predict and evaluate
# y_pred = pipeline.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# report = classification_report(y_test, y_pred)
#
# # Step 10: Print results
# print("Accuracy:", accuracy)
# print("\nClassification Report:\n", report)
