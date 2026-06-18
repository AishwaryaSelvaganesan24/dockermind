from fastapi import FastAPI
import joblib

from llm_engine.advisor import get_recommendation

app = FastAPI(
    title="DockerMind API"
)

# Random Forest Model
model = joblib.load(
    "models/model.pkl"
)

# Log Classification Model
log_model = joblib.load(
    "log_classifier/log_model.pkl"
)

@app.get("/")
def home():

    return {
        "message": "DockerMind API Running"
    }


@app.post("/predict")
def predict(data: dict):

    cpu = data["cpu"]
    memory = data["memory"]
    restart = data["restart"]

    ratio = cpu / memory

    prediction = model.predict(
        [[cpu, memory, restart, ratio]]
    )[0]

    result = (
        "anomaly"
        if prediction == 1
        else "normal"
    )

    return {
        "prediction": result
    }


@app.post("/analyze-log")
def analyze_log(data: dict):

    try:

        log_text = data["log"]

        issue = log_model.predict(
            [log_text]
        )[0]

        recommendation = get_recommendation(
            issue,
            log_text
        )

        return {
            "issue": issue,
            "recommendation": recommendation
        }

    except Exception as e:

        return {
            "error": str(e)
        }