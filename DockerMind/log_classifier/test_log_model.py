import joblib

model = joblib.load(
    "log_classifier/log_model.pkl"
)

samples = [
    "Database connection timeout",
    "Container terminated due to OOMKilled",
    "Pod entered CrashLoopBackOff state",
    "Network unreachable error",
    "Application started successfully"
]

for log in samples:

    prediction = model.predict(
        [log]
    )[0]

    print(
        f"{log} --> {prediction}"
    )