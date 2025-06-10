import pandas as pd

df = pd.read_csv('diabetes.csv')

print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistics Summary")
print(df.describe())

columns_to_clean = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[columns_to_clean] = df[columns_to_clean].replace(0, pd.NA)

print("\nMissing Values Count:")
print(df.isnull().sum())

# df_clean = df.dropna()

#Fill missing values with median
for column in columns_to_clean:
    median_value = df[column].median()
    df[column].fillna(median_value, inplace=True)

# Verify no more missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df = df.rename(columns={
    'Pregnancies': 'pregnancies',
    'Glucose': 'glucose',
    'BloodPressure': 'blood_pressure',
    'SkinThickness': 'skin_thickness',
    'Insulin': 'insulin',
    'BMI': 'bmi',
    'DiabetesPedigreeFunction': 'diabetes_pedigree',
    'Age': 'age',
    'Outcome': 'outcome'  # 1 = diabetic, 0 = not diabetic
})

print("\nUpdated Column Names:")
print(df.columns)

# Filter for diabetic patients only
diabetic_patients = df[df['outcome'] == 1]
print("\nDiabetic Patients Count:", len(diabetic_patients))

# Filter for non-diabetic patients only
non_diabetic_patients = df[df['outcome'] == 0]
print("Non-Diabetic Patients Count:", len(non_diabetic_patients))

# Filter for patients with high glucose levels (> 140)
high_glucose = df[df['glucose'] > 140]
print("Patients with High Glucose:", len(high_glucose))

# Filter for patients with both high glucose and high BMI
high_risk = df[(df['glucose'] > 140) & (df['bmi'] > 30)]
print("High Risk Patients:", len(high_risk))

# Save the cleaned dataframe to a new CSV file
df.to_csv('diabetes_cleaned.csv', index=False)
print("\nCleaned data saved to 'diabetes_cleaned.csv'")