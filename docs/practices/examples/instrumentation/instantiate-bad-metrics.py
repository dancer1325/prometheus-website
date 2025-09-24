from prometheus_client import Counter, Histogram

# Métricas definidas en archivo separado
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests')
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP request duration')
