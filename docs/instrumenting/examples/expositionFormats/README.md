# requirements

* install [Prometheus](/prometheus/README.md#install)

# Text-based format
* `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
* http://localhost:9090/metrics
  * look for ALL supported metric types
  * `# HELP metricName docstring`
  * `# TYPE metricName concreteType`
  * sampleS
    * `go_gc_cycles_automatic_gc_cycles_total`
    * `prometheus_http_request_duration_seconds_bucket`
    * `value`
      * NON-standard numerical values
        * `Nan`
    * `[ timestamp ]`
      * ALMOST NONE built-in Prometheus metric included
        * Reason:🧠SAMPLE | specific time (RIGHT now)🧠
    * recommended to appear ALWAYS | SAME order 
      * refresh http://localhost:9090/metrics

## Grouping and sorting
### provide ALL lines -- as -- 1! group
* `go_gc_duration_seconds`
  * comments & `go_gc_duration_seconds` & `go_gc_duration_seconds_count`

## Histograms and summaries
* `go_gc_heap_allocs_by_size_bytes_`
  * histogram
* `prometheus_rule_evaluation_duration_seconds`
  * summary

# OpenMetrics Text Format
* TODO:

# Protobuf format

