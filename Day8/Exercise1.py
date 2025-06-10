import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("people-10000.csv")

df['Date of birth'] = pd.to_datetime(df['Date of birth'], errors='coerce')
df['Age'] = datetime.now().year - df['Date of birth'].dt.year
df['Birth Year'] = df['Date of birth'].dt.year

sns.set(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Gender Distribution (Bar plot)
sns.countplot(x='Sex', data=df, ax=axes[0, 0], palette='pastel')
axes[0, 0].set_title("Gender Distribution")
axes[0, 0].set_xlabel("Sex")
axes[0, 0].set_ylabel("Count")

# Birth Year
# Histogram
sns.histplot(df['Birth Year'].dropna(), bins=30, kde=False, ax=axes[0, 1], color='skyblue')
axes[0, 1].set_title("Distribution of Birth Years")
axes[0, 1].set_xlabel("Year")
axes[0, 1].set_ylabel("Frequency")

#Top 10 Job Titles
top_jobs = df['Job Title'].value_counts().nlargest(10)
sns.barplot(x=top_jobs.values, y=top_jobs.index, ax=axes[1, 0], palette='muted')
axes[1, 0].set_title("Top 10 Job Titles")
axes[1, 0].set_xlabel("Count")
axes[1, 0].set_ylabel("Job Title")

#Age Box Plot
sns.boxplot(x='Age', data=df, ax=axes[1, 1], color='lightgreen')
axes[1, 1].set_title("Age Distribution")
axes[1, 1].set_xlabel("Age")


plt.tight_layout()
plt.show()
