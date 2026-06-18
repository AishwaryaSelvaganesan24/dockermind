import requests

PROM_URL = "http://localhost:9090"


def query(query_text):

    response = requests.get(
        f"{PROM_URL}/api/v1/query",
        params={
            "query": query_text
        }
    )

    data = response.json()

    return float(
        data["data"]["result"][0]["value"][1]
    )


def get_metrics():

    cpu_query = """
    100 - (
    avg(rate(node_cpu_seconds_total{mode="idle"}[1m]))
    * 100
    )
    """

    memory_query = """
    (
    1 -
    (
    node_memory_MemAvailable_bytes
    /
    node_memory_MemTotal_bytes
    )
    ) * 100
    """

    cpu = query(cpu_query)

    memory = query(memory_query)

    return {
        "cpu": round(cpu, 2),
        "memory": round(memory, 2)
    }

if __name__ == "__main__":

    print(
        get_metrics()
    )