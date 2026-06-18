import requests

PROM_URL = "http://localhost:9090"

def query(q):
    response = requests.get(
        f"{PROM_URL}/api/v1/query",
        params={"query": q}
    )
    return response.json()


cpu_query = '100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)'

memory_query = '(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100'

print("CPU")
print(query(cpu_query))

print("\nMEMORY")
print(query(memory_query))