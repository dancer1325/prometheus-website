* goal
    * types of configurations

# requirements

* install [Prometheus & Promtool](/prometheus/README.md#install)
* `make assets`

# uses
## metric types can be distinguished
* | root path
  * `prometheus --config.file=docs/concepts/examples/metric_types/simple-prometheus.yml --web.listen-address=:9090`
* `curl http://localhost:9090/metrics`
  * 's return
    * wire protocol / 👀expressed | units👀
* `pip3 install prometheus-client` & `python3 metrics_example.py`
  * check EACH metric type is distinguished
    * Reason: 🧠NOT ALLOWED any action🧠

## metric types can NOT be distinguished
* steps
  * `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
  * http://localhost:9090/query
    * `avg(prometheus_http_requests_total)`
      * Reason of Prometheus can NOT distinguish metric types: 🧠
        * `prometheus_http_requests_total` == counter
        * `avg()` == function -- for -- Gauges
        * Prometheus executed the query WITHOUT errors🧠

# Counter
* steps
  * `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
## 1! monotonically increasing counter
* http://localhost:9090/metrics
  * `prometheus_http_requests_total`
    * == `<basename>`
    * hit SEVERAL times http://localhost:9090/api/v1/alerts
      * increate `prometheus_http_requests_total{code="200",handler="/api/v1/alerts"}`
## | restart, reset to 0
* `docker stop prometheus`, `docker container prune -f`, `docker volume prune -f`
* `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
* http://localhost:9090/metrics
  * `prometheus_http_requests_total{code="200",handler="/api/v1/alerts"}` = 0
## | query,
### use `rate()`
* `rate(prometheus_http_requests_total[5m])`
### use `increase()`
* `increase(prometheus_http_requests_total[5m])`

# Gauge


# Histogram
* steps
  * `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
## 1! metric / expose MULTIPLE time series
* http://localhost:9090/metrics
  * `prometheus_http_request_duration_seconds`
    * == `<basename>`
    * `prometheus_http_request_duration_seconds_bucket{`
      * == `<basename>_bucket{le="<upper inclusive bound>"}`
      * CUMULATIVE -- `go_gc_pauses_seconds_bucket` -- 
    * `prometheus_http_request_duration_seconds_sum`
      * == `<basename>_sum`
    * `prometheus_http_request_duration_seconds_count`
      * == `<basename>_count`

# Summary
* steps
  * `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
## 1! metric / expose MULTIPLE time series
* http://localhost:9090/metrics
  * `prometheus_rule_evaluation_duration_seconds`
    * == `<basename>`
    * `prometheus_rule_evaluation_duration_seconds{quantile="`
      * == `<basename>{quantile="<φ>"}`
    * `prometheus_rule_evaluation_duration_seconds_sum`
      * == `<basename>_sum`
    * `prometheus_rule_evaluation_duration_seconds_count`
      * == `<basename>_count`

