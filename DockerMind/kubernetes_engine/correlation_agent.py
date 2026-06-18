from kubernetes_engine.cpu_agent import analyze_cpu
from kubernetes_engine.memory_agent import analyze_memory


def correlate():

    cpu_alerts = analyze_cpu()

    memory_alerts = analyze_memory()

    findings = []

    memory_pods = {
        x["pod"]
        for x in memory_alerts
    }

    for alert in cpu_alerts:

        if alert["pod"] in memory_pods:

           findings.append(
                {
                    "pod": alert["pod"],
                    "issue": "CPU and Memory anomaly detected",
                    "confidence": 0.95
                }
           )    

        

    return findings


if __name__ == "__main__":

    print(
        correlate()
    )