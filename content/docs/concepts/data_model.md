---
title: Data model
sort_rank: 1
---

# Data model

* ⭐️[_time series_](http://en.wikipedia.org/wiki/Time_series) ⭐️
  * == streams of timestamped values / belong to the SAME
    * metric
    * set of labeled dimensions
  * == data model / 
    * uses
      * 👀MOST used one by Prometheus -- to store -- ALL data 👀
  * temporary derived time series
    * == Prometheus query results

## Metric names and labels

* **Metric names**
  * allows
    * specifying the general feature of a system / it's measured
      * _Example:_ `http_requests_total` == total # of HTTP requests received
  * requirements
    * match the regex `[a-zA-Z_:][a-zA-Z0-9_:]*`
  * may contain
    * ASCII letters,
    * digits,
    * underscores,
    * colons
      * reserved for user defined recording rules
        * NOT valid to -- be used by -- exporters or direct instrumentation
  * uses
    * ⚠️identify UNIQUELY time series -> MANDATORY ⚠️
  * see [best practices for naming metrics and labels](/docs/practices/naming/)

* **Metric labels**
  * == key-value pairs
    * optional
  * enable Prometheus's dimensional data model
    * allows
      * identify
        * ANY given combination of labels / SAME metric name
        * particular dimensional instantiation of that metric 
          * _Example:_ ALL HTTP requests / used the method `POST` `/api/tracks` 
    * uses
      * query language can filter and aggregate -- based on -- these dimensions
  * requirements
    * `[a-zA-Z_][a-zA-Z0-9_]*`
  * may contain
    * ASCII letters,
    * numbers,
  * naming rules
    * NOT beginning with `__` (two "_")
      * Reason: 🧠RESERVED for internal use 🧠
    * see [best practices for naming metrics and labels](/docs/practices/naming/)
  * 's value
    * may contain 
      * ANY Unicode characters
    * change (_Example:_ add or remove) -> will create a NEW time series
    * if it's empty == labels / NOT exist

## Samples

* 👀== actual time series data 👀
* 👀== float64 value + millisecond-precision timestamp 👀
  * float64 value
    * | Prometheus v2.40+ / experimental 
      * -- can be replaced by -- full histogram

## Notation 

* Notation of time series
  ```
  <metric name>{<label name>=<label value>, ...}
  ```
  
  * _Example:_ 
    ```
    api_http_requests_total{method="POST", handler="/messages"}
    ```

  * == notation of [OpenTSDB](http://opentsdb.net/) 
