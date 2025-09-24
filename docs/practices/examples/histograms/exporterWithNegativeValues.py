from prometheus_client import Histogram, Summary, start_http_server
import time
import random

# Histograma para temperaturas (puede ser negativo)
temp_histogram = Histogram('temperature_celsius', 'Temperature measurements')

# Summary para balance (puede ser negativo)
balance_summary = Summary('account_balance', 'Account balance')

def generate_metrics():
    while True:
        # Temperatura entre -20 y 40 grados
        temp = random.uniform(-20, 40)
        temp_histogram.observe(temp)

        # Balance entre -1000 y 5000
        balance = random.uniform(-1000, 5000)
        balance_summary.observe(balance)

        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    generate_metrics()
