import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    classification_report
)

df = pd.read_csv(
    "data/processed_metrics.csv"
)

X = df[
    [
        "cpu",
        "memory",
        "restart",
        "cpu_memory_ratio"
    ]
]

y = df["anomaly"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = SVC()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)

print(
    "Accuracy:",
    accuracy_score(
        y_test,
        predictions
    )
)

print(
    classification_report(
        y_test,
        predictions
    )
)