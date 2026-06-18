import pandas as pd

df = pd.read_csv("data/metrics.csv")

print(df["anomaly"].value_counts())