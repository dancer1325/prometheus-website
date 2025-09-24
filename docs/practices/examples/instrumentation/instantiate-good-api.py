from prometheus_client import Counter, Histogram

# Métricas definidas donde se usan
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests')
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP request duration')

def handle_request():
    REQUEST_COUNT.inc()  # Métrica definida arriba, fácil de encontrar
    # ... lógica
