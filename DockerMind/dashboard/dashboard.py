import streamlit as st
import pandas as pd
import joblib
import sys
from pathlib import Path

# Project root access

sys.path.append(
str(Path(__file__).resolve().parent.parent)
)

from llm_engine.advisor import get_recommendation
from collector.live_metrics import get_metrics
from kubernetes_engine.rca_agent import generate_rca
from kubernetes_engine.pod_collector import get_pod_metrics
from kubernetes_engine.coordinator_agent import generate_insight

from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="DockerMind",
    layout="wide"
)

st_autorefresh(
    interval=10000,
    key="refresh"
)
# -----------------------------

# Load Models

# -----------------------------

log_model = joblib.load(
"log_classifier/log_model.pkl"
)

# -----------------------------

# Get Live Metrics

# -----------------------------

try:


   live_metrics = get_metrics()

   live_cpu = live_metrics["cpu"]
   live_memory = live_metrics["memory"]

except Exception as e:


  live_cpu = 0
  live_memory = 0


# -----------------------------

# Page Config

# -----------------------------

st.set_page_config(
page_title="DockerMind",
layout="wide"
)

# -----------------------------

# Header

# -----------------------------

st.title("🚀 DockerMind")

st.subheader(
"AI-Powered Kubernetes Intelligence Platform"
)

st.caption(
"Live Metrics Powered by Prometheus + Node Exporter"
)

# -----------------------------

# Live Infrastructure Metrics

# -----------------------------

st.divider()

st.subheader(
"📡 Live Infrastructure Metrics"
)

col1, col2 = st.columns(2)

col1.metric(
"CPU Usage %",
round(live_cpu, 2)
)

col2.metric(
"Memory Usage %",
round(live_memory, 2)
)

# -----------------------------

# Live Kubernetes Pods

# -----------------------------

st.divider()

st.subheader(
"☸️ Live Kubernetes Pods"
)

try:


  pod_data = get_pod_metrics()

  st.dataframe(
    pd.DataFrame(pod_data),
    use_container_width=True
  )


except Exception as e:

  st.error(
    f"Failed to fetch pod metrics: {e}"
)


# -----------------------------

# Agent Findings

# -----------------------------

st.divider()

st.subheader(
"🧠 Agent Findings"
)

try:


  insight = generate_insight()

  st.write(
    "CPU Agent Findings"
  )

  st.json(
    insight["cpu_findings"]
  )

  st.write(
    "Memory Agent Findings"
  )

  st.json(
    insight["memory_findings"]
  )

  st.write(
    "Correlation Agent Findings"
  )

  st.json(
    insight["correlation_findings"]
  )


except Exception as e:


  st.error(
    f"Agent analysis failed: {e}"
  )

# -----------------------------

# Multi-Agent RCA

# -----------------------------

st.divider()

st.subheader(
    "🧠 Multi-Agent Root Cause Analysis"
)

if st.button(
    "Analyze Kubernetes Cluster"
):

    try:

        with st.spinner(
            "Running Agents..."
        ):

            rca = generate_rca()

        st.markdown(
            rca
        )

    except Exception as e:

        st.error(
            f"RCA failed: {e}"
        )


# -----------------------------

# AI Log Troubleshooter

# -----------------------------

st.divider()

st.subheader(
"🤖 AI Log Troubleshooter"
)

log_text = st.text_area(
"Paste Container Log Here"
)

if st.button(
    "Analyze Log"
):

    if log_text.strip():

        issue = log_model.predict(
            [log_text]
        )[0]

        recommendation = get_recommendation(
            issue,
            log_text
        )

        st.markdown(
            recommendation
        )

    else:

        st.warning(
            "Please enter a log message."
        )