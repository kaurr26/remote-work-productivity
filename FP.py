import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\rajvi\OneDrive\Desktop\FP\cleaned_employee_data.csv"
df = pd.read_csv(file_path)

print(df.head())


print(df.info())
print(df.isnull().sum())
print(df.describe())


plt.figure(figsize=(8,4))
sns.histplot(df['productivity_score'], kde=True)
plt.title('Distribution of Productivity Scores')
plt.xlabel('Productivity Score')
plt.ylabel('Count')
plt.show()

print(df['work_arrangement'].value_counts())
print(df['department'].value_counts())

plt.figure(figsize=(8,4))
sns.boxplot(x='work_arrangement', y='productivity_score', data=df)
plt.title('Productivity by Work Arrangement')
plt.show()

print(df.groupby('work_arrangement')['productivity_score'].mean())

plt.figure(figsize=(8,4))
sns.barplot(x='work_arrangement', y='productivity_score', data=df, estimator='mean')
plt.title('Average Productivity by Work Arrangement')
plt.show()
