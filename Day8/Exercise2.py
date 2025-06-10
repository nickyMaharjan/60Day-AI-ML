import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("people-10000.csv")

df['Date of birth'] = pd.to_datetime(df['Date of birth'], errors='coerce')
df['Age'] = datetime.now().year - df['Date of birth'].dt.year
df['Birth Year'] = df['Date of birth'].dt.year

sns.set(style="whitegrid")
# plt.figure(figsize=(8, 6))
# sns.countplot(x='Sex', data=df, palette='pastel')
# plt.title("Gender Distribution")
# plt.xlabel("Sex")
# plt.ylabel("Count")
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.histplot(df['Birth Year'].dropna(), bins=30, color='skyblue')
# plt.title("Distribution of Birth Years")
# plt.xlabel("Year")
# plt.ylabel("Frequency")
# plt.show()

# top_jobs = df['Job Title'].value_counts().nlargest(10)
#
# plt.figure(figsize=(12, 6))
# sns.barplot(x=top_jobs.values, y=top_jobs.index, palette='muted')
# plt.title("Top 10 Job Titles")
# plt.xlabel("Count")
# plt.ylabel("Job Title")
# plt.show()

plt.figure(figsize=(10, 4))
sns.boxplot(x='Age', data=df, color='lightgreen')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.show()



