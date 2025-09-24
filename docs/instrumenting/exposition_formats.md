---
title: Exposition formats
sort_rank: 6
---

* goal
  * ways to expose metrics -- to -- Prometheus

## Text-based format

* | Prometheus v2.0,
  * requirements
    * ⚠️ALL processes / expose metrics to Prometheus -> need to use a text-based format ⚠️ 
* implemented by MULTIPLE [client libraries](clientlibs)

### Basic info

| Aspect | Description                                                                                                                                                           |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Inception** | April 2014                                                                                                                                                            |
| **Supported in** | Prometheus version `>=0.4.0`                                                                                                                                          |
| **Transmission** | HTTP                                                                                                                                                                  |
| **Encoding** | UTF-8, `\n` line endings                                                                                                                                              |
| **HTTP `Content-Type`** | `text/plain; version=0.0.4` <br/> if you miss `version` value -> fall-back to the MOST RECENT text format version                                                     |
| **Optional HTTP `Content-Encoding`** | `gzip`                                                                                                                                                                |
| **Advantages** | <ul><li>Human-readable</li><li>Easy to assemble (❌NO need nesting❌)</li><li>Readable line by line</li></ul>                                                           |
| **Limitations** | <ul><li>Verbose</li><li>Types and docstrings not integral part of the syntax, meaning little-to-nonexistent metric contract validation</li><li>Parsing cost</li></ul> |
| **Supported metric primitives** | <ul><li>Counter</li><li>Gauge</li><li>Histogram</li><li>Summary</li><li>Untyped</li></ul>                                                                             |

### Text format details

* line oriented
  * == lines are separated -- by a -- line feed character (`\n`)
  * empty lines are ignored

#### Line format

* | line,
  * tokens can be separated -- by -- >=1 blanks and/or tabs
    * Reason:🧠otherwise, merge with the PREVIOUS token🧠
* Leading & trailing whitespace
  * ignored
* EACH line
  * MUST be unique
    * OTHERWISE, the ingestion behavior is undefined

#### Comments, help text, and type information

* content
  * `#`
    * == comments 
      * ignored by Prometheus
  * `# HELP metricName docstring`
    * NOT ignored
      * != COMMON comment
    * ⚠️OPTIONAL⚠️
    * ⚠️EXIST 1! / `metricName`⚠️
    * `docstring`
      * OPTIONAL
      * == ANY sequence of UTF-8 characters /
        * if you want to escape
          * `\` -> -- via -- `\\`
          * `\n` -> -- via -- `\\`
  * `# TYPE metricName metricType`
    * NOT ignored
      * != COMMON comment
    * ⚠️OPTIONAL⚠️
    * requirements
      * ⚠️EXIST 1! / `metricName`⚠️
      * place BEFORE reporting the FIRST sample / `metricName` 
    * `concreteType`
      * == metric type
      * ALLOWED ones
        * `counter`
        * `gauge`
        * `histogram`
        * `summary`
        * `untyped`
          * default one
  * samples
    * 1 / EACH line
    * 👀-- following -- syntax [EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form)👀

    ```
    metric_name [
      "{" label_name "=" `"` label_value `"` { "," label_name "=" `"` label_value `"` } [ "," ] "}"
    ] value [ timestamp ]
    ```
    * `[]`
      * == OPTIONAL
    * `metric_name` & `label_name`
      * restrictions == PromQL restrictions
    * `label_value`
      * == ANY sequence of UTF-8 characters /
        * backslash (`\`) character is escaped -- as -- `\\`
        * double-quote (`"`) character is escaped -- as -- `\"`
        * line feed (`\n`) character is escaped -- as -- `\n`
    * `value`
      * == float / 
        * represented -- as required by -- Go's [`ParseFloat()`](https://golang.org/pkg/strconv/#ParseFloat) function
        * ALLOWED values
          * standard numerical values,
          * `NaN`,
            * POSSIBLE Reason:🧠
              * Prometheus recently launched
              * NO queries
              * NOT enough window time🧠
          * `+Inf`,
          * `-Inf`
    * `timestamp`
      * == `int64` /
        * milliseconds since epoch == 1970-01-01 00:00:00 UTC 
        * represented -- as required by -- Go's [`ParseInt()`](https://golang.org/pkg/strconv/#ParseInt) function

#### Grouping and sorting

* / EACH metric
  * provide ALL lines -- as -- 1! group
  * FIRSTLY ALL OPTIONAL `HELP` and `TYPE` lines

* recommendations
  * | "/metrics",
    * 👀metrics MUST appear ALWAYS | SAME order👀
      * OTHERWISE, the computational cost is prohibitive

#### Histograms and summaries

The `histogram` and `summary` types are difficult to represent in the text
format. The following conventions apply:

* The sample sum for a summary or histogram named `x` is given as a separate sample named `x_sum`.
* The sample count for a summary or histogram named `x` is given as a separate sample named `x_count`.
* Each quantile of a summary named `x` is given as a separate sample line with the same name `x` and a label `{quantile="y"}`.
* Each bucket count of a histogram named `x` is given as a separate sample line with the name `x_bucket` and a label `{le="y"}` (where `y` is the upper bound of the bucket).
* A histogram _must_ have a bucket with `{le="+Inf"}`. Its value _must_ be identical to the value of `x_count`.
* The buckets of a histogram and the quantiles of a summary must appear in increasing numerical order of their label values (for the `le` or the `quantile` label, respectively).

### Text format example

* _Example:_ FULL-fledged Prometheus metric exposition (comments + `HELP` + `TYPE` expressions + histogram + summary + character escaping examples)

```
# HELP http_requests_total The total number of HTTP requests.
# TYPE http_requests_total counter
http_requests_total{method="post",code="200"} 1027 1395066363000
http_requests_total{method="post",code="400"}    3 1395066363000

# Escaping in label values:
msdos_file_access_time_seconds{path="C:\\DIR\\FILE.TXT",error="Cannot find file:\n\"FILE.TXT\""} 1.458255915e9

# Minimalistic line:
metric_without_timestamp_and_labels 12.47

# A weird metric from before the epoch:
something_weird{problem="division by zero"} +Inf -3982045

# A histogram, which has a pretty complex representation in the text format:
# HELP http_request_duration_seconds A histogram of the request duration.
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{le="0.05"} 24054
http_request_duration_seconds_bucket{le="0.1"} 33444
http_request_duration_seconds_bucket{le="0.2"} 100392
http_request_duration_seconds_bucket{le="0.5"} 129389
http_request_duration_seconds_bucket{le="1"} 133988
http_request_duration_seconds_bucket{le="+Inf"} 144320
http_request_duration_seconds_sum 53423
http_request_duration_seconds_count 144320

# Finally a summary, which has a complex representation, too:
# HELP rpc_duration_seconds A summary of the RPC duration in seconds.
# TYPE rpc_duration_seconds summary
rpc_duration_seconds{quantile="0.01"} 3102
rpc_duration_seconds{quantile="0.05"} 3272
rpc_duration_seconds{quantile="0.5"} 4773
rpc_duration_seconds{quantile="0.9"} 9001
rpc_duration_seconds{quantile="0.99"} 76656
rpc_duration_seconds_sum 1.7560473e+07
rpc_duration_seconds_count 2693
```

## OpenMetrics Text Format

* [OpenMetrics](https://github.com/OpenObservability/OpenMetrics)
  * is the an effort to standardize metric wire formatting built off of Prometheus text format
* It is possible to scrape targets
and it is also available to use for federating metrics since at least v2.23.0.

### Exemplars (Experimental)

Utilizing the OpenMetrics format allows for the exposition and querying of [Exemplars](https://github.com/prometheus/OpenMetrics/blob/v1.0.0/specification/OpenMetrics.md#exemplars).
Exemplars provide a point in time snapshot related to a metric set for an otherwise summarized MetricFamily. Additionally they may have a Trace ID attached to them which when used to together
with a tracing system can provide more detailed information related to the specific service.

To enable this experimental feature you must have at least version v2.26.0 and add `--enable-feature=exemplar-storage` to your arguments.

## Protobuf format

Earlier versions of Prometheus supported an exposition format based on [Protocol Buffers](https://developers.google.com/protocol-buffers/) (aka Protobuf) in addition to the current text-based format. With Prometheus 2.0, the Protobuf format was marked as deprecated and Prometheus stopped ingesting samples from said exposition format.

However, new experimental features were added to Prometheus where the Protobuf format was considered the most viable option. Making Prometheus accept Protocol Buffers once again.

Here is a list of experimental features that, once enabled, will configure Prometheus to favor the Protobuf exposition format:

| feature flag | version that introduced it |
|--------------|----------------------------|
| native-histograms | 2.40.0 |
| created-timestamp-zero-ingestion | 2.50.0 |

* [source code](https://github.com/prometheus/client_model)

## Historical versions

* [Client Data Exposition Format](https://docs.google.com/document/d/1ZjyKiKxZV83VI9ZKAXRGKaUKK2BIWCT7oiGBKDBpjEY/edit?usp=sharing)
