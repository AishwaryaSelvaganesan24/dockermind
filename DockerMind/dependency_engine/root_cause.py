from pod_metrics import pods


def find_root_cause():

    highest_cpu = 0
    culprit = None

    for pod, metrics in pods.items():

        if metrics["cpu"] > highest_cpu:

            highest_cpu = metrics["cpu"]
            culprit = pod

    return culprit


if __name__ == "__main__":

    root = find_root_cause()

    print(
        "Root Cause:",
        root
    )