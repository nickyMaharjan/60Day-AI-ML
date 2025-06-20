import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("lr-Real-estate.csv")
df = df.drop(columns=["No"])

#Standardize feature
X = df.drop(columns=["Y house price of unit area"])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#PCA to 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

#KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_pca)

#Silhouette score
sil_score = silhouette_score(X_pca, clusters)

# Visualize PCA + Clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=clusters, palette="viridis")
plt.title(f"KMeans Clusters on PCA Data (Silhouette Score: {sil_score:.2f})")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.grid(True)
plt.tight_layout()
plt.show()
