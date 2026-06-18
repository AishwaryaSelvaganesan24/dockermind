import subprocess


def get_pod_metrics():

    output = subprocess.check_output(
        [
            "kubectl",
            "top",
            "pods",
            "-n",
            "dockermind",
            "--no-headers"
        ]
    ).decode()

    pods = []

    for line in output.splitlines():

        parts = line.split()

        pods.append(
            {
                "pod": parts[0],
                "cpu": parts[1],
                "memory": parts[2]
            }
        )

    return pods


if __name__ == "__main__":

    metrics = get_pod_metrics()

    print(metrics)