---
title: Metric types
sort_rank: 2
---

# Metric types

* Prometheus client libraries' core metric types
  * are
    * `counter`
    * `gauge`
    * `histogram`
    * `summary`
  * uses /
    * can distinguish them
      * client libraries
        * _Example of use:_ enable APIs -- based on the -- usage of the specific types
      * wire protocol 
    * can NOT distinguish them
      * Prometheus server
        * Reason:🧠ALL data -- is flatten into -- untyped time series🧠

## Counter

* == cumulative metric /
  * == 1! [👀monotonically increasing👀 counter](https://en.wikipedia.org/wiki/Monotonic_function) 
    * `<basename>`
    * 's value
      * ONLY increase OR
      * | restart,
        * reset to 0
  * uses
    * number of 
      * requests served,
      * tasks completed
      * errors
  * ❌NOT uses❌
    * expose a value / can decrease
      * _Example:_ number of CURRENTLY running processes
  * 👀recommendations👀
    * | query,
      * use
        * `rate()`
        * `increase()`
      * Reason:🧠OTHERWISE, it's a cumulative value / NO valuable information🧠

* Client library / support counters
  * [Go](http://godoc.org/github.com/prometheus/client_golang/prometheus#Counter)
  * [Java](https://prometheus.github.io/client_java/getting-started/metric-types/#counter)
  * [Python](https://prometheus.github.io/client_python/instrumenting/counter/)
  * [Ruby](https://github.com/prometheus/client_ruby#counter)
  * [.Net](https://github.com/prometheus-net/prometheus-net#counters)
  * [Rust](https://docs.rs/prometheus-client/latest/prometheus_client/metrics/counter/index.html)

## Gauge

A _gauge_ is a metric that represents a single numerical value that can
arbitrarily go up and down.

Gauges are typically used for measured values like temperatures or current
memory usage, but also "counts" that can go up and down, like the number of
concurrent requests.

Client library usage documentation for gauges:

   * [Go](http://godoc.org/github.com/prometheus/client_golang/prometheus#Gauge)
   * [Java](https://prometheus.github.io/client_java/getting-started/metric-types/#gauge)
   * [Python](https://prometheus.github.io/client_python/instrumenting/gauge/)
   * [Ruby](https://github.com/prometheus/client_ruby#gauge)
   * [.Net](https://github.com/prometheus-net/prometheus-net#gauges)
   * [Rust](https://docs.rs/prometheus-client/latest/prometheus_client/metrics/gauge/index.html)

## Histogram

* _histogram_
  * == 👀1! metric / expose MULTIPLE time series👀
    * `<basename>_bucket{le="<upper inclusive bound>"}`
      * == cumulative counters -- for the -- observation buckets
      * | Prometheus v3.0+,
        * `le` label's values
          * | ingestion,
            * are normalized -- to follow -- [OpenMetrics Canonical Numbers](https://github.com/prometheus/OpenMetrics/blob/main/specification/OpenMetrics.md#considerations-canonical-numbers)
    * `<basename>_sum`
      * **total sum** of ALL observed values
    * `<basename>_count`
      * == `<basename>_bucket{le="+Inf"}`
      * == **count** of events / have been observed 
  * how does it work?
    * take sample observations (_Example:_ `prometheus_http_request_duration_seconds`)
    * count the observations | configurable buckets
  * [`histogram_quantile()` function](/prometheus/docs/querying/functions.md#histogram_quantile)
    * uses
      * calculate an [Apdex score](http://en.wikipedia.org/wiki/Apdex)
  * [MORE](../practices/histograms)

* [native histograms](../specs/native_histograms.md)

* Client libraries / support histograms
  * [Go](http://godoc.org/github.com/prometheus/client_golang/prometheus#Histogram)
  * [Java](https://prometheus.github.io/client_java/getting-started/metric-types/#histogram)
  * [Python](https://prometheus.github.io/client_python/instrumenting/histogram/)
  * [Ruby](https://github.com/prometheus/client_ruby#histogram)
  * [.Net](https://github.com/prometheus-net/prometheus-net#histogram)
  * [Rust](https://docs.rs/prometheus-client/latest/prometheus_client/metrics/histogram/index.html)

## Summary

* _summary_
  * == 👀1! metric / expose MULTIPLE time series👀
    * `<basename>{quantile="<φ>"}`
      * streaming **φ-quantiles** (0 ≤ φ ≤ 1) of observed events
        * streaming
          * == calculated | real time
        * φ-quantile == percentile
          * _Examples:_
            * φ = 0.5 → percentile 50 (mediana)
            * φ = 0.95 → percentile 95
            * φ = 0.99 → percentile 99
        * `<φ>`
          * | Prometheus v3.0,
            * | ingestion,
              * are normalized -- to follow -- [OpenMetrics Canonical Numbers](https://github.com/prometheus/OpenMetrics/blob/main/specification/OpenMetrics.md#considerations-canonical-numbers)
    * `<basename>_sum`
      * **total sum** of ALL observed values
    * `<basename>_count`
      * == **count** of events / have been observed
  * [MORE](../practices/histograms)

* Client libraries / support summaries
  * [Go](http://godoc.org/github.com/prometheus/client_golang/prometheus#Summary)
  * [Java](https://prometheus.github.io/client_java/getting-started/metric-types/#summary)
  * [Python](https://prometheus.github.io/client_python/instrumenting/summary/)
  * [Ruby](https://github.com/prometheus/client_ruby#summary)
  * [.Net](https://github.com/prometheus-net/prometheus-net#summary)
