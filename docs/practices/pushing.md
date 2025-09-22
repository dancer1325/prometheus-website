---
title: When to use the Pushgateway
sort_rank: 7
---

* see [Pushing metrics](../instrumenting/pushing.md)

## use cases -- for -- Pushgateway

* ⚠️| limited cases⚠️
  * Reason: 🧠use Pushgategay (!= Prometheus pull model) -> problems🧠
    * if MULTIPLE applications push | 1! Pushgateway -> Pushgateway == 
      * single point of failure
      * potential bottleneck
    * lose Prometheus's automatic instance health monitoring ( == `up` metric)
      * Reason: 🧠NOT provided -- by -- Pushgateway🧠
    * Pushgateway NEVER forgets series pushed | it -> expose them | Prometheus, FOREVER
      * Reason:🧠Pushgateway's lifecycle -- INDEPENDENT OF -- processes / push the metrics 🧠
      * ALTERNATIVE
        * delete MANUALLY the series -- via the -- Pushgateway's API
      * ⚠️!= Prometheus model⚠️
        * Reason:🧠Prometheus delete AUTOMATICALLY unused series🧠
  * capture the service-level batch job's outcome
    * "service-level" batch job 
      * _Example:_ batch job / deletes users | ALL platform
      * != machine-specific or job instance
        * _Example:_ batch job / deletes users | entire service
    * see [best practices for monitoring batch jobs](/docs/practices/instrumentation/#batch-jobs)

## Alternative strategies

* if an inbound firewall or NAT is preventing you -- from -- 
  * pulling metrics -- from -- targets ->
    * move the Prometheus server BEHIND the network barrier
      * recommendations
        * run Prometheus servers | network / == monitored instances' networks
        * use [PushProx](https://github.com/RobustPerception/PushProx)
          * enable Prometheus / traverse a firewall or NAT
* machine-specific or job instance
  * recommendations
    * expose the metrics -- via -- [Node Exporter's](https://github.com/prometheus/node_exporter) [textfile collector](https://github.com/prometheus/node_exporter#textfile-collector)
      * ❌NOT -- via -- Pushgateway❌
