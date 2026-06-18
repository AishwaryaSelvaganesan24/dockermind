import pandas as pd
import random

rows = []

for i in range(5000):

    cpu = random.randint(5, 100)
    memory = random.randint(100, 1000)
    restart = random.randint(0, 5)

    if (cpu > 90 and memory > 800) or restart > 4:
        anomaly = 1
    else:
        anomaly = 0

    rows.append([
        cpu,
        memory,
        restart,
        anomaly
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "cpu",
        "memory",
        "restart",
        "anomaly"
    ]
)

df.to_csv(
    "data/metrics.csv",
    index=False
)

print("Dataset Created Successfully!")
print(df.head())