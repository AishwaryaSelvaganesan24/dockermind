def get_insight(cpu, memory, restart):

    if cpu > 90 and memory > 800:
        return (
            "CPU and Memory Saturation",
            "Increase CPU allocation and investigate workload spikes."
        )

    elif restart > 4:
        return (
            "Pod Restart Loop",
            "Inspect pod logs and application crashes."
        )

    elif cpu > 85:
        return (
            "High CPU Usage",
            "Consider horizontal scaling."
        )

    else:
        return (
            "Healthy Pod",
            "No action required."
        )