from metrics import REQUEST_COUNT, REQUEST_DURATION

def handle_request():
    REQUEST_COUNT.inc()  # ¿Dónde está definida esta métrica?
    # ... lógica
