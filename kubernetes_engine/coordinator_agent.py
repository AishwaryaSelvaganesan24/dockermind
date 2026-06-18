from kubernetes_engine.discovery_agent import discover_pods
from kubernetes_engine.resource_agent import analyze_resources
from kubernetes_engine.dependency_agent import get_affected_services


def generate_insight():

    pods = discover_pods()

    resource_info = analyze_resources()

    root_pod = resource_info[
        "highest_memory"
    ]["pod"]

    affected = get_affected_services(
        root_pod
    )

    return {
        "root_cause": root_pod,
        "affected_services": affected,
        "total_pods": len(pods)
    }


if __name__ == "__main__":

    print(
        generate_insight()
    )