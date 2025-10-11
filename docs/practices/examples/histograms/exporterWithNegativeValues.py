from prometheus_client import Histogram, Summary, start_http_server
import time
import random

# Histograma para temperaturas (puede ser negativo)
temp_histogram = Histogram('temperature_celsius', 'Temperature measurements')

# Summary para balance (puede ser negativo)
balance_summary = Summary('account_balance', 'Account balance')

def generate_metrics():
    while True:
        # Temperatura entre -20 y 0 grados (siempre negativo)
        temp = random.uniform(-20, 0)
        print(f"Observing temperature: {temp:.2f}°C")
        temp_histogram.observe(temp)

        # Balance entre -1000 y 5000
        balance = random.uniform(-1000, 5000)
        print(f"Observing balance: ${balance:.2f}")
        balance_summary.observe(balance)
        
        # Mostrar valores internos
        print(f"Histogram _sum: {temp_histogram._sum._value}")
        print(f"Summary _sum: {balance_summary._sum._value}")
        print("---")

        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    generate_metrics()
