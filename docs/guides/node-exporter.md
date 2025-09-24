---
title: Monitoring Linux host metrics with the Node Exporter
---

* Prometheus [**Node Exporter**](https://github.com/prometheus/node_exporter)
  * == 1! static binary
  * valid |
    * Unix systems
      * ⚠️| Windows, use [Windows exporter](https://github.com/prometheus-community/windows_exporter)⚠️
  * exposes 
    * hardware metrics
    * kernel-related metrics

* goals
  * | `localhost`, 
    * start up a 
      * Node Exporter 
      * Prometheus instance / configured to scrape metrics from the running Node Exporter

## Installing and running the Node Exporter

* ways to install & run
  * [download + extract + run](examples/nodeExporter/README.md#download--extract--run) 
  * [ansible](https://github.com/prometheus/node_exporter?tab=readme-ov-file#ansible)
  * [docker](https://github.com/prometheus/node_exporter?tab=readme-ov-file#docker)

## Node Exporter metrics

* http://localhost:9100/metrics
  * look up 💡"node_"💡
    ```bash
    curl http://localhost:9100/metrics | grep "node_"
    ```
  * ⚠️!= http://localhost:9090/metrics ⚠️
    * == Prometheus' OWN metrics

## Configuring your Prometheus instances

* goal
  * Prometheus can access Node Exporter metrics

* [here](examples/nodeExporter/README.md#configure-prometheus-instance)
