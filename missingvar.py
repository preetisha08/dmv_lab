import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("your_dataset.csv")

print("Missing values in each column:\n")
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nAfter handling missing values:\n")
print(df.isnull().sum())

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

plt.figure(figsize=(10, 6))
plt.boxplot(df[numeric_cols].dropna())

plt.title("Boxplot after handling missing values")
plt.xticks(range(1, len(numeric_cols)+1), numeric_cols, rotation=45)

plt.savefig("boxplot.png")
plt.show()
