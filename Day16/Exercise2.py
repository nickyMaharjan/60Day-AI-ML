import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('iris-data.csv')  # Update path if needed

# Convert to binary classification: 1 if Iris-versicolor, else 0
df['target'] = df['species'].apply(lambda x: 1 if x == 'Iris-versicolor' else 0)

# Features and target
X = df.drop(columns=['species', 'target'])
y = df['target']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Print classification report
print(classification_report(y_test, y_pred, target_names=["Not Versicolor", "Versicolor"]))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens',
            xticklabels=["Not Versicolor", "Versicolor"],
            yticklabels=["Not Versicolor", "Versicolor"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix: Iris-versicolor")
plt.tight_layout()
plt.show()
