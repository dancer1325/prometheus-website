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
      * 👀by Prometheus -- to store -- ALL data 👀
  * temporary derived time series
    * ⚠️!= exist time series⚠️
    * == 👀calculated on-fly | Prometheus query results👀
  * 's notation
    ```
    <metric name>{<label name>=<label value>, ...}
    ```
    * _Example:_
      ```
      api_http_requests_total{method="POST", handler="/messages"}
      ```
    * follow [OpenTSDB's notation](http://opentsdb.net/)
    * if `metric name` use UTF-8 characters / outside the recommended set -> MUST be quoted
      ```
      {"<metric name>", <label name>="<label value>", ...}
      ```
    * `{__name__="<metric name>", <label name>="<label value>", ...}`
      * allows
        * complex querying
      * == 👀way / Prometheus internally stores 👀

* time series data
  * == 👀1! point | specific time series👀
  * == 💡`<metric name>{<label name>=<label value>, …}  value  @Timestamp|wasRegistered`💡
    * == 👀sample👀
    * `value`
      * == float64
    * `@Timestamp|wasRegistered`
      * 
  * _Example:_
    ```text
    http_requests_total{method="GET", status="200"} 1547 @1609459200
    # 1547                              == number of requests
    # @1609459200                       == timestamp | it was registered
    # {method="GET", status="200"}      == labels
    ```

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
  * ⚠️if you want to identify UNIQUELY time series -> MANDATORY ⚠️
  * see [best practices for naming metrics and labels](/prometheus-website/docs/practices/naming.md)

* **Metric labels**
  * == key-value pairs
    * OPTIONAL
    * 's value
      * may contain
        * ANY Unicode characters
      * change (_Example:_ add or remove) -> NEW time series
  * enable Prometheus's dimensional data model
    * dimension
      * == labels
    * allows
      * identify
        * ANY given combination of labels / SAME metric name
        * particular dimensional instantiation of that metric 
          * _Example:_ ALL HTTP requests / used the method `POST` `/api/tracks` 
    * uses
      * query language can filter & aggregate -- based on -- these dimensions
  * requirements
    * `[a-zA-Z_][a-zA-Z0-9_]*`
  * may contain
    * ASCII letters,
    * numbers,
  * naming rules
    * NOT beginning with `__` (two "_")
      * Reason: 🧠RESERVED for internal use 🧠
    * see [best practices for naming metrics and labels](/prometheus-website/docs/practices/naming.md)
