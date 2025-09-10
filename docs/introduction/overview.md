---
title: Overview
sort_rank: 1
---

## What is Prometheus?

* [here](/prometheus-website/src/components/Hero.md)
* [external documentation links](media.md)

### Features

* [here](/prometheus-website/src/components/FeaturesCards.md)
* time series collection
  * -- via -- HTTP / pull model 
* [pushing time series](../instrumenting/pushing.md)
  * supported -- via an -- intermediary gateway
* targets are discovered -- via -- service discovery OR static configuration
* multiple modes of graphing & dashboarding support

### What are metrics?

* metrics
  * == 👀numerical measurements / SIMPLY explained👀
  * allows
    * understand your application 

* term time series
  * == recording of changes | time

* what to measure
  * depend -- on -- EACH application
    * _Examples:_ 
      * _Example1:_ | web server, request count metric
      * _Example2:_ | database, number of active connections or active queries

### Components

* characteristics
  * MOST are OPTIONAL
  * written | [Go](https://golang.org/)
    * -> easy to build & deploy -- as -- static binaries

* are
  * [Prometheus server](https://github.com/prometheus/prometheus)
    * about time series data,
      * scrapes
      * stores 
  * [client libraries](../instrumenting/clientlibs.md)
    * allows
      * instrumenting application code
  * [push gateway](https://github.com/prometheus/pushgateway)
    * support 
      * short-lived jobs
  * [exporters](../instrumenting/exporters.md)
    * uses
      * special-purpose
        * _Examples:_ like HAProxy, StatsD, Graphite, etc.
  * [alertmanager](https://github.com/prometheus/alertmanager)
    * allows
      * handle alerts
  * OTHERS

### Architecture

* goal
  * Prometheus' architecture + its ecosystem components

![Prometheus architecture](/prometheus-website/public/assets/docs/architecture.svg)

* Prometheus 
  * scrapes instrumented jobs' metrics -- via --
    * directly OR
    * short-lived jobs' intermediary push gateway 
  * stores locally ALL scraped samples
  * runs rules -- over -- this data
    * Reason: 🧠
      * aggregate & record new time series -- from -- existing data OR
      * generate alerts🧠

* [Grafana](https://grafana.com/) OR other API consumers
  * uses
    * visualize the collected data

## Use cases

* recording any purely numeric time series
* monitoring
  * machine-centric or
  * highly dynamic service-oriented architectures
* | microservices architecture
  * Reason: 🧠support multi-dimensional data
    * collection &
    * querying🧠

* reliability
  * MAIN design's goal
  * == | outage,
    * allow you to quickly diagnose problems
  * Reasons: 🧠
    * EACH Prometheus server is standalone
    * ❌NOT depend on network storage OR other remote services❌ 
    * ❌NOT need to setup extensive infrastructure❌
    * ALTHOUGH other parts of your infrastructure are broken -> you can rely on it🧠

## ❌NOT use cases❌

* need 100% accuracy
  * _Example:_ for billing
  * Reason: 🧠the collected data NORMALLY is NOT detailed and complete enough🧠
