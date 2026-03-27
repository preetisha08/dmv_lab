import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students_admission.csv")

# Display data
print(df.head())

df = pd.read_csv("C:/Users/YourName/Downloads/students_admission.csv")

print(df.isnull().sum())

df.fillna(method='ffill', inplace=True)

df.to_csv("cleaned_data.csv", index=False)

df.iloc[:, 0].value_counts().plot(kind='bar')
plt.show()

df.iloc[:, 1].plot()
plt.show()

df.iloc[:, 0].value_counts().plot(kind='pie')
plt.show()

plt.scatter(df.iloc[:, 1], df.iloc[:, 2])
plt.show()

df.iloc[:, 1].plot(kind='hist')
plt.show()

