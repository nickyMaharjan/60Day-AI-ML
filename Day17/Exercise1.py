import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("iris-data.csv")

#Converting all measurement columns to numeric
for col in ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with any NaN values
df = df.dropna()

# Drop the label column 
X = df.drop('species', axis=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Visualize the clusters using seaborn pairplot
sns.set(style="whitegrid")
pairplot = sns.pairplot(df, hue='cluster',
                        vars=['sepal-length', 'sepal-width', 'petal-length', 'petal-width'],
                        palette='Set1')
plt.suptitle("KMeans Clustering on Iris Dataset", y=1.02)
plt.tight_layout()
plt.show()
