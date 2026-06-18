import pandas as pd

df = pd.read_csv("data/metrics.csv")

# New feature
df["cpu_memory_ratio"] = df["cpu"] / df["memory"]

print(df.head())

df.to_csv(
    "data/processed_metrics.csv",
    index=False
)

print("Processed dataset saved.")