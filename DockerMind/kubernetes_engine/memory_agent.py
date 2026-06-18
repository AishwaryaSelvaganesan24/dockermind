from kubernetes_engine.pod_collector import get_pod_metrics


def analyze_memory():

    pods = get_pod_metrics()

    alerts = []

    for pod in pods:

        memory = int(
            pod["memory"].replace(
                "Mi",
                ""
            )
        )
        if memory > 20:

            if memory > 200:
                severity = "critical"

            elif memory > 100:
                severity = "high"

            else:
                severity = "medium"

            alerts.append(
                {
                    "pod": pod["pod"],
                    "memory": memory,
                    "severity": severity
                }
            )

    return alerts


if __name__ == "__main__":

    print(
        analyze_memory()
    )