from kubernetes_engine.pod_collector import get_pod_metrics


def analyze_resources():

    pods = get_pod_metrics()

    highest_memory = max(
        pods,
        key=lambda x: int(
            x["memory"].replace(
                "Mi",
                ""
            )
        )
    )

    highest_cpu = max(
        pods,
        key=lambda x: int(
            x["cpu"].replace(
                "m",
                ""
            )
        )
    )

    return {
        "highest_cpu": highest_cpu,
        "highest_memory": highest_memory
    }


if __name__ == "__main__":

    print(
        analyze_resources()
    )