import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # Seaborn makes matplotlib plots look prettier!

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.head())
print(df.describe())

print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].median())

print(df.isnull().sum())

# PLOT 1
plt.figure(figsize=(6,4))
sns.countplot(x='Survived' , data = df)
plt.title("Survival Count")
plt.xlabel("Survival (0 = NO , 1 = YES)")
plt.ylabel("Number of Passengers")
plt.show()

# PLOT 2
plt.figure(figsize=(6,4))
sns.countplot(x='Sex', hue = 'Survived' , data = df)
plt.title("Survival by gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# PLOT 3
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=30, kde= True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# PLOT 4
plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Passenger Class vs Survival")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.show()