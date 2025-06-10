import pandas as pd
from datetime import datetime

file_path = "people-10000.csv"
df = pd.read_csv(file_path)

#calculate age
df['Date of birth'] = pd.to_datetime(df['Date of birth'], errors='coerce')
df['Age'] = df['Date of birth'].apply(lambda dob: datetime.now().year - dob.year if pd.notnull(dob) else None)

sex_count = df.groupby('Sex')['User Id'].count()
print("Count of people by Sex:")
print(sex_count)
print()

# Common Job Titles
top_job_titles = df['Job Title'].value_counts().head(10)
print("Top 10 most common Job Titles:")
print(top_job_titles)
print()

# Group by Job title and count number of male and female
job_sex_counts = df.groupby(['Job Title', 'Sex'])['User Id'].count().unstack().fillna(0)
print("Job Titles with Male/Female counts (Top 10):")
print(job_sex_counts.head(10))
print()

#Average age by Job Title
average_age_by_job = df.groupby('Job Title')['Age'].mean().sort_values(ascending=False).head(10)
print("Top 10 Job Titles with Highest Average Age:")
print(average_age_by_job)
