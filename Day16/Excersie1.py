import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('iris-data.csv')  # Update path if needed

# Convert species to binary: 1 if 'Iris-setosa', else 0
df['target'] = df['species'].apply(lambda x: 1 if x == 'Iris-setosa' else 0)
X = df.drop(columns=['species', 'target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Print classification report
report = classification_report(y_test, y_pred, target_names=["Not Setosa", "Setosa"])
print(report)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot confusion matrix heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=["Not Setosa", "Setosa"],
            yticklabels=["Not Setosa", "Setosa"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()
