# test_metrics.py
from prometheus_client import Counter, Gauge, start_http_server
import time

# Counter - ONLY can increase
requests = Counter('app_requests_total', 'Total requests')

# Gauge - can increase & decrease
memory = Gauge('app_memory_bytes', 'Memory usage')

if __name__ == '__main__':
    start_http_server(8000)

    while True:
        requests.inc()        # ✅ -- for -- counter
        memory.set(1024)      # ✅ -- for -- gauge
        # requests.dec()      # ❌ counters can NOT decrease
        time.sleep(1)
