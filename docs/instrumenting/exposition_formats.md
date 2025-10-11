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

* conventions
  * sample sum
    * `x` -> `x_sum`
  * sample count
    * `x` -> `x_count`
  * EACH summary's quantile | DIFFERENT line
    * label `{quantile="y"}`
  * EACH histogram's bucket | DIFFERENT line
    * `x` -> `x_bucket{le="y", ...}`
      * `y` == bucket's upper bound
      * `x_bucket{le="+Inf"}`'s value == `x_count`
  * histogram's buckets & summary's quantiles 
    * appear | increasing numerical order of their label values

## OpenMetrics Text Format

* [OpenMetrics](https://github.com/OpenObservability/OpenMetrics)
  * goal
    * standardize metric wire formatting 
  * -- based on -- Prometheus text format
  * allows
    * scrape targets
    * | v2.23.0,
      * use | federating metrics 
    * expose & query [Exemplars](https://github.com/prometheus/OpenMetrics/blob/v1.0.0/specification/OpenMetrics.md#exemplars) 

### Exemplars (Experimental)

* requirements
  * Prometheus v2.26.0
  * `--enable-feature=exemplar-storage` 

* Exemplars
  * provide
    * metric set' snapshot
    * Trace ID
      * OPTIONAL
  * uses |
    * aggregated metrics 
      * _Example:_ histogram OR summary  

## Protobuf format

* history
  * | Prometheus earlier versions,
    * supported 
  * | Prometheus 2.0,
    * deprecated
    * Prometheus stopped ingesting samples
  * | NEW experimental features,
    * Protobuf format is the most viable option
      * -> 👀Prometheus accept Protocol Buffers again👀

| feature flag                     | version that introduced it  |
|----------------------------------|-----------------------------|
| native-histograms                | 2.40.0                      |
| created-timestamp-zero-ingestion | 2.50.0                      |

* [source code](https://github.com/prometheus/client_model)

## Historical versions

* [Client Data Exposition Format](https://docs.google.com/document/d/1ZjyKiKxZV83VI9ZKAXRGKaUKK2BIWCT7oiGBKDBpjEY/edit?usp=sharing)
