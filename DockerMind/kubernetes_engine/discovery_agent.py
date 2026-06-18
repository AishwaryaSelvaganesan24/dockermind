import subprocess


def discover_pods():

    output = subprocess.check_output(
        [
            "kubectl",
            "get",
            "pods",
            "-n",
            "dockermind",
            "-o",
            "name"
        ]
    ).decode()

    return [
        pod.replace(
            "pod/",
            ""
        )
        for pod in output.splitlines()
    ]


if __name__ == "__main__":

    print(
        discover_pods()
    )