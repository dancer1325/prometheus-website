* goal
    * types of configurations

# requirements

* install [Prometheus & Promtool](/prometheus/README.md#install)

# `_count` & `_sum`
* steps
  * `python3 exporterWithNegativeValues.py` 
    * http://localhost:8000/metrics
      * metrics exposed
  * `docker compose up -d`
## `rate()` NOT valid
* http://localhost:9090/query
  * `temperature_celsius_sum / temperature_celsius_count`
    * Problems:
      * Problem1: it cna return negative values
        * Solution: TODO:
  * `account_balance_sum / account_balance_count`
    * Problems:
      * Problem1: it cna return negative values
        * Solution: TODO:
