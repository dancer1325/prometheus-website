* goal
    * types of configurations

# requirements

* install [Prometheus & Promtool](/prometheus/README.md#install)

# `_count` & `_sum`
* steps
  * `python3 exporterWithNegativeValues.py`
    * print negative values
  * `docker compose up -d`
## it can have negative values
* http://localhost:8000/metrics
  * check negative values 
## `rate(_sum)` mathematically NO sense
* http://localhost:9090/query
  * `rate(temperature_celsius_sum[2m])`
    * rate change of sum of Celsius / s
  * `rate(temperature_celsius_sum[2m]) / rate(temperature_celsius_count[2m])`
    * rate change of sum of Celsius / count

# TODO: