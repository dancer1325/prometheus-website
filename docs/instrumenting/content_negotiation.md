---
title: Scrape protocol content negotiation
nav_title: Content negotiation
sort_rank: 8
---

## Abstract

* goal
  * protocol negotiation mechanism / Prometheus used | scrap targets' metrics
    * ==
      * `- H Accept`
      * supported Content Types
        * chosen -- based on -- `- H Accept` 
      * negotiation process

## Introduction

* Prometheus supported formats | scrape metrics
  * text-based
  * binary protobuf

## Protocol Types

### Prometheus supported Protocols

1. `PrometheusProto`
   * Binary protobuf format
   * use cases
     * HIGH volume
     * low network
2. `PrometheusText0.0.4`
   * Prometheus text format version 0.0.4
   * use cases
     * legacy services
3. `PrometheusText1.0.0`
   * Prometheus text format version 1.0.0
4. `OpenMetricsText0.0.1`
   * OpenMetrics text format version 0.0.1
5. `OpenMetricsText1.0.0`
   * OpenMetrics text format version 1.0.0
   * use cases
     * modern services
     * recommended standard

### Protocol Headers

| Protocol             | MIME Type                       | Parameters                                                 |
| -------------------- | ------------------------------- | ---------------------------------------------------------- |
| PrometheusProto      | application/vnd.google.protobuf | proto=io.prometheus.client.MetricFamily;encoding=delimited |
| PrometheusText0.0.4  | text/plain                      | version=0.0.4                                              |
| PrometheusText1.0.0  | text/plain                      | version=1.0.0                                              |
| OpenMetricsText0.0.1 | application/openmetrics-text    | version=0.0.1                                              |
| OpenMetricsText1.0.0 | application/openmetrics-text    | version=1.0.0                                              |

## Accept Header Construction

* Accept header
  * constructed -- by -- Prometheus
  * == formats / it supports

### Basic Format

1. / EACH protocol / supported -- by the -- target
   - protocol's MIME type & parameters
     - MUST be specified
   - | protobuf protocols,
     - encoding of "delimited" MUST be specified
   - | PrometheusText1.0.0 & OpenMetricsText1.0.0,
     - escaping scheme parameter SHOULD be appended
   - quality value (q) parameter
     - SHOULD be appended
2. catch-all `*/*` / the lowest quality value
   - SHOULD be appended

### Quality Values

* Quality values
  * SHOULD be assigned | descending order
    * -- based on the -- protocol's position | Accept header
      - First protocol
        - q=0.{n+1} 
          - n == NUMBER of supported protocols
      - Second protocol
        - q=0.{n}
          - n == NUMBER of supported protocols
      - ... 

### Escaping Scheme

* `-H Accept` / has `escaping=<scheme>`
  * ⚠️required |⚠️
    * PrometheusText1.0.0 protocol
    * OpenMetricsText1.0.0 protocol
  * ALLOWED `<scheme>` values
    - `allow-utf8`
    - `underscores`
    - `dots`
    - `values`
  * see [Escaping Schemes](escaping_schemes.md)

### Compression

* `-H Accept-Encoding`
  * SHOULD be
    - if compression is 
      - enabled -> `gzip` 
      - disabled -> `identity` 

## Selection of Format

* selection process of an appropriate Content-Type / follows the scrape target
  1. use the protocol | `-H Accept` / highest weighting / supported by Prometheus
  2. if NO protocols are supported -> the target MAY use a user-configured fallback
     scrape protocol
  3. if NO fallback is specified -> the target MUST use PrometheusText0.0.4 -- as a -- last resort

## Content-Type Response

* Targets SHOULD respond with `-H Content-Type` / MUST include
  1. appropriate MIME type
  2. version parameter
  3. | text formats version 1.0.0+,
     * the escaping scheme parameter

## Security Considerations

1. Targets MUST validate the Accept header
   * Reason:🧠prevent potential injection attacks🧠
2. escaping scheme parameter MUST be validated
   * Reason:🧠prevent protocol confusion🧠
3. Content-Type headers MUST be properly sanitized
   * Reason:🧠prevent MIME type confusion🧠

## Examples

### Default Accept Header

```
Accept: application/openmetrics-text;version=1.0.0;escaping=allow-utf8;q=0.5,application/openmetrics-text;version=0.0.1;q=0.4,text/plain;version=1.0.0;escaping=allow-utf8;q=0.3,text/plain;version=0.0.4;q=0.2,/;q=0.1
```

### Protobuf-First Accept Header

```
Accept: application/vnd.google.protobuf;proto=io.prometheus.client.MetricFamily;encoding=delimited;q=0.5,application/
openmetrics-text;version=1.0.0;escaping=allow-utf8;q=0.4,application/openmetrics-text;version=0.0.1;q=0.3,text/plain;version=1.0.0;escaping=allow-utf8;q=0.2,text/plain;version=0.0.4;q=0.1,/;q=0.0
```
