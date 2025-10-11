* `docker compose up -d`

# native histogram == 1! time series
## ⚠️converted | ingest⚠️
* http://localhost:9090/query
  * `prometheus_http_request_duration_seconds{handler="/api/v1/scrape_pools"}`
  * `http_request_duration_seconds`
## /metrics, exposition format == classic histogram
* http://localhost:8080/metrics
  * look for histogram
## != classic histograms / have MULTIPLE time series
* launch prometheus classic
  ```
  docker run -d \
    --name prometheus-classic \
    -p 9091:9090 \
    prom/prometheus:latest \
    --config.file=/etc/prometheus/prometheus.yml \
    --web.listen-address=0.0.0.0:9090
  ```
* http://localhost:9091/query
  * ❌`prometheus_http_request_duration_seconds` does NOT exist❌
    * exist
      * `prometheus_http_request_duration_seconds_bucket`
      * `prometheus_http_request_duration_seconds_count`
      * `prometheus_http_request_duration_seconds_sum`

## higher resolution
* http://localhost:9090/query
  * `histogram_count(http_request_duration_seconds)`
    * \>> next value
* http://localhost:9091/query
  * `{__name__=~".*_bucket"}`

## cheaper
* http://localhost:9091/query
  * some series are empty
    * `go_gc_pauses_seconds_bucket`
    * `prometheus_http_request_duration_seconds_bucket`
* http://localhost:9090/query
  * `prometheus_http_request_duration_seconds{handler="/api/v1/scrape_pools"}`

# TODO:
