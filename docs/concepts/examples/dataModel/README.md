* goal
    * time series
    * TODO:
    * monitor another service

# requirements

* install 
  * [Prometheus & Promtool](/prometheus/README.md#install)
  * [docker](https://docs.docker.com/engine/install/)
  * [node](https://nodejs.org/en/download)
* `make assets`

# time series
* | this path
  * `docker compose up -d`
* | http://localhost:9090/query
  * `prometheus_http_requests_total`, graph (adjust timing)

## streams of timestamped values / belong to the SAME metric OR labeled dimensions
* == EACH line | graph

## temporary derived time series
### != exist time series
* check EXISTING time series
  * ways
    * | http://localhost:9090/query
      * `{__name__=~".+"}`
    * [sample.http](sample.http)

### calculated on-fly | Prometheus query results
* `rate(prometheus_http_requests_total[5m])`

## 's notation
### `<metric name>{<label name>=<label value>, ...}`
* | http://localhost:9090/query
  * `prometheus_http_requests_total`
  * `prometheus_http_requests_total{handler="/api/v1/query"}`

### if `metric name` use UTF-8 characters / outside the recommended set -> MUST be quoted
* `{"app.legacy-metrics.cpu-usage"}`

### `{__name__="<metric name>", <label name>="<label value>", ...}`
* `{__name__=~"go_gc_.*"}`
* `{__name__=~"prometheus_.*"}`

# time series data
## == 💡time series + value + timestamp (| was recorded)💡
* steps
  * http://localhost:9090/query
  * `prometheus_http_requests_total[5m]`

# Metric names and labels
## Metric names
* TODO:

## Metric labels
* TODO:

# Notation
* TODO:

# Monitor another service

* how to monitor another service
* default "/metrics" endpoint

* steps
  * `node mock-metrics-server.js`
    * hit `curl http://localhost:3001/metrics`
  * | browser,
    * http://localhost:9090/query
    * `http_requests_total{job="mock-app"}`
  * http://localhost:3001/metrics
    * scraped -- by -- Prometheus
