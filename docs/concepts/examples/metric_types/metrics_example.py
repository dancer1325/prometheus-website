"""
This example demonstrates that Prometheus client libraries enforce and distinguish
between different metric types (Counter, Gauge, Histogram, Summary).

Run it and open http://localhost:8000/metrics to see the different metrics exposed.
"""

from prometheus_client import Counter, Gauge, Histogram, Summary, start_http_server
import random
import time

# Counter - can ONLY increase (monotonic)
requests_total = Counter('app_requests_total', 'Total requests processed')

# Gauge - can go up and down (arbitrary value at a point in time)
memory_bytes = Gauge('app_memory_bytes', 'Memory usage in bytes')

# Histogram - counts observations in configurable buckets + sum & count
request_duration_seconds = Histogram(
    'app_request_duration_seconds',
    'Request latency in seconds',
    buckets=(0.05, 0.1, 0.2, 0.5, 1, 2, 5)
)

# Summary - tracks observations with quantiles (client-side) plus sum & count
payload_size_bytes = Summary('app_payload_size_bytes', 'Payload size in bytes')


def demonstrate_invalid_ops_once():
    """Show (safely) that invalid operations are not allowed for a metric type."""
    examples = [
        (requests_total, 'dec', (1,), "Counter cannot decrease (no dec method)"),
        (requests_total, 'set', (123,), "Counter cannot be set directly (no set method)"),
        (memory_bytes, 'observe', (1.23,), "Gauge has no observe; use set/inc/dec"),
        (request_duration_seconds, 'inc', (1,), "Histogram does not support inc; use observe"),
        (payload_size_bytes, 'set', (2048,), "Summary cannot be set; use observe"),
    ]
    for obj, method, args, note in examples:
        try:
            getattr(obj, method)(*args)  # type: ignore[attr-defined]
        except Exception as e:  # noqa: BLE001 - show the enforcement clearly
            print(f"As expected -> {note}: {e.__class__.__name__}: {e}")


if __name__ == '__main__':
    start_http_server(8000)
    print("Prometheus metrics server started on :8000/metrics")
    print("Demonstrating type-specific operations. Press Ctrl+C to stop.\n")

    # Show once that wrong operations are rejected by the client library
    demonstrate_invalid_ops_once()

    while True:
        # Counter: only increments are valid
        requests_total.inc()

        # Gauge: can move up, down, or be set
        memory_bytes.inc(random.randint(0, 10))
        memory_bytes.dec(random.randint(0, 5))
        # Setting to a concrete value (e.g., sampled memory reading)
        memory_bytes.set(1024 + random.randint(-128, 256))

        # Histogram: record observed durations
        simulated_latency = random.uniform(0.01, 1.5)
        request_duration_seconds.observe(simulated_latency)

        # Summary: record observed sizes
        simulated_payload = random.randint(100, 5000)
        payload_size_bytes.observe(simulated_payload)

        # Illustrative invalid operations (commented out):
        # requests_total.dec()          # ❌ counters cannot decrease
        # requests_total.set(1)         # ❌ counters cannot be set
        # memory_bytes.observe(1.2)     # ❌ gauges do not support observe
        # request_duration_seconds.inc()# ❌ histograms do not support inc
        # payload_size_bytes.set(10)    # ❌ summaries do not support set

        time.sleep(1)
