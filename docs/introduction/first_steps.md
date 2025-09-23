---
title: First steps with Prometheus
nav_title: First steps
sort_rank: 3
---

* goal
  * how to,
    * about Prometheus, 
      * install
      * configure
    * about FIRST resource | Prometheus, 
      * install 
      * configure
      * monitor
    * about exporters,
      * download
      * install

* exporters
  * expose time series data | hosts & services
  * 💡Prometheus itself💡
    * FIRST exporter
    * provides
      * host-level metrics (memory usage, garbage collection, ...)

## Downloading Prometheus

* [here](https://github.com/dancer1325/prometheus/blob/main/README.md#install)

## Configuring Prometheus

* Prometheus configuration
  * == [YAML](https://yaml.org/)
  * | download Prometheus,
    * 👀sample `prometheus.yml` 👀

* `scrape_interval`
  * == FREQUENCY / scrape targets
  * ways to set it up
    * `global.scrape_interval`
    * `scrape_configs[*].scrape_interval`

* `evaluation_interval`
  * FREQUENCY / evaluate rules

* `rule_files`
  * == rule files location / we want the Prometheus server load

* `scrape_configs`
  * == resources / Prometheus scrape
  * see [here](https://github.com/dancer1325/prometheus/blob/main/docs/configuration/configuration.md#scrape_config)

* `/metrics`
  * 👀== endpoint / Prometheus expects metrics / exposed -- by -- targets👀

* http://localhost:9090/metrics
  * OWN Prometheus' exposed metrics 

## Using the expression browser

* _Examples:_ [here](examples/firstSteps/README.md#using-the-expression-browser--graph-interface)
* see [PromQl](https://prometheus.io/docs/prometheus/latest/querying/basics/)

## Using the graphing interface

* _Examples:_ [here](examples/firstSteps/README.md#using-the-expression-browser--graph-interface)
