---
title: Understanding metric types
sort_rank: 2
---

## Counter

* PromQL's functions used
  * `rate()`
    * how fast the value is increasing / second
      * -- based on -- history of metrics | time frame & calculates 
    * uses
      * ⚠️ONLY | `counter`⚠️

* steps
    * `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
    * http://localhost:9090/query
        * `go_gc_duration_seconds_count`
        * `rate(go_gc_duration_seconds_count)[5m]`

## Gauge

* PromQL's functions used
    * `max_over_time`
    * `min_over_time`
    * `avg_over_time`

* steps
  * `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
  * http://localhost:9090/query
    * `go_memstats_alloc_bytes`
    * `max_over_time(go_memstats_alloc_bytes[5m])`
    * `min_over_time(go_memstats_alloc_bytes[5m])`
    * `avg_over_time(go_memstats_alloc_bytes[5m])`

## Histogram

* PromQL's functions used
  * `histogram_quantile()` 

* steps
  * `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
  * http://localhost:9090/query
    * `prometheus_http_request_duration_seconds_bucket`
    * `prometheus_http_request_duration_seconds_bucket{handler="/query"}`
    * `prometheus_http_request_duration_seconds_bucket{handler="/query"}`
    * `histogram_quantile(0.9, prometheus_http_request_duration_seconds_bucket{handler="/query"})`
    * `histogram_quantile(0.9, rate(prometheus_http_request_duration_seconds_bucket{handler="/query"}[5m]))`

## Summary

* ❌aggregation of metrics is NOT possible❌ 
  * Reason:🧠they are calculated | application level🧠
