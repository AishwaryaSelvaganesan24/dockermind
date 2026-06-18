import pandas as pd

df = pd.read_csv(
    "logs/container_logs.csv"
)

print(df.head())

print("\nClass Distribution:\n")

print(
    df["label"].value_counts()
)