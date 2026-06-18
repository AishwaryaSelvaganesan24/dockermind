from kubernetes_engine.pod_collector import get_pod_metrics


def analyze_cpu():

    pods = get_pod_metrics()

    alerts = []

    for pod in pods:

        cpu = int(
            pod["cpu"].replace(
                "m",
                ""
            )
        )

        if cpu > 0:

            if cpu > 50:
               severity = "critical"

            elif cpu > 10:
               severity = "high"

            else:
               severity = "medium"

            alerts.append(
            {
               "pod": pod["pod"],
               "cpu": cpu,
               "severity": severity
            }
            )

    return alerts


if __name__ == "__main__":

    print(
        analyze_cpu()
    )