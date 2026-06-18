import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent)
)

from kubernetes_engine.coordinator_agent import generate_insight
from llm_engine.advisor import get_recommendation


def generate_rca():

    insight = generate_insight()

    context = f"""
Total Pods:
{insight['total_pods']}

CPU Findings:
{insight['cpu_findings']}

Memory Findings:
{insight['memory_findings']}

Correlation Findings:
{insight['correlation_findings']}
"""

    return get_recommendation(
        "resource_bottleneck",
        context
    )


if __name__ == "__main__":
    print(generate_rca())
