---
title: Use file-based service discovery to discover scrape targets
---

* Prometheus 
  * provide MULTIPLE [service discovery options](https://github.com/prometheus/prometheus/tree/main/discovery)
    * _Examples:_ [Kubernetes](/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config), [Consul](/docs/prometheus/latest/configuration/configuration/#consul_sd_config), ...
    * 👀[file-based service discovery](../configuration/configuration/#file_sd_config) mechanism👀
      * use cases
        * you need a service discovery system / ❌NOT CURRENTLY supported❌ 
      * enables you 
        * list scrape targets | JSON file

* goal
  * install & run Prometheus [Node Exporter](./node-exporter.md) locally
  * create a "targets.json" / 
    * specify Node Exporter's host & port information 
  * install & run Prometheus instance / 
    * discover -- , via "targets.json", the -- Node Exporter 

## Installing and running the Node Exporter

* follow [this guide](node-exporter.md)

## Installing, configuring, and running Prometheus

* [here](examples/fileSD/README.md#install-configure--run-prometheus)

* "target.json"
  * == JSON service discovery configurations
  * types
    * MANUAL
    * SON-generating process or tool
      * 👀recommended one👀

## Changing the targets list dynamically

* Prometheus' file-based service discovery mechanism
  * enable Prometheus instance
    * listen for file changes / 👀AUTOMATICALLY update the scrape target list👀
