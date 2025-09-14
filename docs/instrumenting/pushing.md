---
title: Pushing metrics
sort_rank: 3
---

* [Prometheus Pushgateway](https://github.com/prometheus/pushgateway)
  * allows you
    * | [short-lived service-level batch jobs](../practices/pushing.md),
      * push time series -- to an -- intermediary job / 
        * Prometheus can scrape
    * \+ Prometheus's simple text-based exposition format,
      * easy to instrument
        * _Example:_ shell scripts WITHOUT a client library
  * uses
    * monitor components / can NOT be scraped
    * by [client libraries](../instrumenting/clientlibs.md)
      * [Java](https://prometheus.github.io/client_java/exporters/pushgateway/)
      * [Go](https://godoc.org/github.com/prometheus/client_golang)
      * [Python](https://prometheus.github.io/client_python)
      * [Ruby](https://github.com/prometheus/client_ruby)
