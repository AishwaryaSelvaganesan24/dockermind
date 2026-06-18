from kubernetes_engine.discovery_agent import discover_pods
from kubernetes_engine.cpu_agent import analyze_cpu
from kubernetes_engine.memory_agent import analyze_memory
from kubernetes_engine.correlation_agent import correlate


def generate_insight():

    pods = discover_pods()

    cpu_findings = analyze_cpu()

    memory_findings = analyze_memory()

    correlation_findings = correlate()

    return {
        "total_pods": len(pods),
        "cpu_findings": cpu_findings,
        "memory_findings": memory_findings,
        "correlation_findings": correlation_findings
    }


if __name__ == "__main__":

    print(
        generate_insight()
    )