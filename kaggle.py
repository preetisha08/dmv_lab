import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("dataset.xlsx")
print("Dataset Preview:\n", df.head())

print("\nMissing Values:\n", df.isnull().sum())

# Fill missing values with mean (for numeric columns)
df.fillna(df.mean(numeric_only=True), inplace=True)

#bar chart
plt.figure()
df.iloc[:, 0].value_counts().plot(kind='bar')
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Count")
plt.show()

# LINE CHART
plt.figure()
df.iloc[:, 1].plot(kind='line')
plt.title("Line Chart")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()

# PIE CHART
plt.figure()
df.iloc[:, 0].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Pie Chart")
plt.ylabel("")
plt.show()

# HISTOGRAM
plt.figure()
df.iloc[:, 2].plot(kind='hist', bins=10)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# S_lair PLOT
plt.figure()
plt.scatter(df.iloc[:, 1], df.iloc[:, 2])
plt.title("Scatter Plot")
plt.xlabel("Column 2")
plt.ylabel("Column 3")
plt.show()

# OUTLIERS DETECTION (BOXPLOT)
plt.figure()
sns.boxplot(data=df.select_dtypes(include=np.number))
plt.title("Outliers Detection (Boxplot)")
plt.show()

# PRINT OUTLIERS 
Q1 = df.select_dtypes(include=np.number).quantile(0.25)
Q3 = df.select_dtypes(include=np.number).quantile(0.75)
IQR = Q3 - Q1

outliers = ((df.select_dtypes(include=np.number) < (Q1 - 1.5 * IQR)) |
            (df.select_dtypes(include=np.number) > (Q3 + 1.5 * IQR)))

print("\nOutliers:\n", df[outliers.any(axis=1)])
