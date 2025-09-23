---
title: Glossary
sort_rank: 9
---

### Alert

* alert
  * == (Prometheus alerting rule / firing)'s outcome 
  * FROM Prometheus,
    * are sent -- to the -- Alertmanager

### Alertmanager

* [Alertmanager's workflow](/docs/alerting/latest/overview/)
  * takes alerts,
  * aggregates them | groups,
  * de-duplicates,
  * applies silences,
  * throttles,
  * sends out notifications -- to -- email, Pagerduty, Slack etc

### Bridge

* bridge
  * == component /
    * client library's samples are exposed -- to a -- NON-Prometheus monitoring system
  * _Example:_ Python, Go, and Java clients can export metrics -- to -- Graphite

### Client library

A client library is a library in some language (e.g. Go, Java, Python, Ruby)
that makes it easy to directly instrument your code, write custom collectors to
pull metrics from other systems and expose the metrics to Prometheus.

### Collector

* collector
  * == exporter's part / 
    * == set of metrics
      * if it's 
        * | [direct instrumentation](#direct-instrumentation) -> 1! metric
        * pulling metrics from ANOTHER system -> MANY metrics 

![](static/exporter.png)

### Direct instrumentation

* Direct instrumentation
  * == instrumentation added inline | your source code
    * -- via -- [client library](#client-library)

    ![](static/directInstrumentation.png)

  * vs External System
  
    ![](static/directInstrumentationVsExternalSystem.png)


### Endpoint

* source of metrics / can be scraped
  * -- correspond to a -- 1! process
    * _Example:_ if a web application runs | http://localhost:8080 
      * -> metrics exposed | http://localhost:8080/metrics

### Exporter

* exporter
  * == binary running ALONGSIDE application / you want to obtain metrics from
  * ALONGSIDE application == ways
    * | SAME server
    * as library
  * exposes Prometheus metrics
    * -- by COMMONLY --
      * metrics / exposed | NON-Prometheus format, are converted -- into a -- format / Prometheus supports

### Instance

An instance is a label that uniquely identifies a target in a job.

### Job

A collection of targets with the same purpose, for example monitoring a group of like processes replicated for scalability or reliability, is called a job.

### Notification

* == group of >=1 alerts /
  * sent
    * -- by -- Alertmanager
    * -- to -- email, Pagerduty, Slack etc.

### Promdash

Promdash was a native dashboard builder for Prometheus. It has been deprecated and replaced by [Grafana](../visualization/grafana.md).

### Prometheus

* refers to 
  * Prometheus 
    * system's core binary
    * monitoring system

### PromQL

* [PromQL](/docs/prometheus/latest/querying/basics/)
  * == Prometheus Query Language
  * enable operations (aggregation, slicing and dicing, prediction and joins)

### Pushgateway

The [Pushgateway](../instrumenting/pushing.md) persists the most recent push
of metrics from batch jobs. This allows Prometheus to scrape their metrics
after they have terminated.

### Recording Rules

Recording rules precompute frequently needed or computationally expensive expressions
and save their results as a new set of time series.

### Remote Read

Remote read is a Prometheus feature that allows transparent reading of time series from
other systems (such as long term storage) as part of queries.

### Remote Read Adapter

Not all systems directly support remote read. A remote read adapter sits between
Prometheus and another system, converting time series requests and responses between them.

### Remote Read Endpoint

A remote read endpoint is what Prometheus talks to when doing a remote read.

### Remote Write

Remote write is a Prometheus feature that allows sending ingested samples on the
fly to other systems, such as long term storage.

### Remote Write Adapter

Not all systems directly support remote write. A remote write adapter sits
between Prometheus and another system, converting the samples in the remote
write into a format the other system can understand.

### Remote Write Endpoint

A remote write endpoint is what Prometheus talks to when doing a remote write.

### Sample

A sample is a single value at a point in time in a time series.

In Prometheus, each sample consists of a float64 value and a millisecond-precision timestamp.

### Silence

* silence | Alertmanager
  * avoid alerts are -- , via labels, -- included | notifications

### Target

* := definition of an object -- to -- scrape
  * _Examples:_
    * labels to apply
    * authentication required -- to -- connect

### Time Series

* [here](../concepts/data_model.md)
