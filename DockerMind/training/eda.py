import pandas as pd

df = pd.read_csv("data/metrics.csv")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nStatistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())