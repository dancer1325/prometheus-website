# Multi-Dimensional data model
* Prometheus
  * models time series | 👀dimensional data model 👀 
    * != raw tables
    * -> 
      * flexible
      * powerful

* Time series
  * == 💡metric name + key-value pairS💡

* [MORE](/prometheus-website/docs/concepts/data_model.md)

# PromQL query language
* := query language / 
  * powerful
    * Reason: 🧠based -- on -- dimensionality🧠
  * allows you,
    * about time series data
      * query, 
      * correlate,
      * transform -- in -- 
        * visualizations
        * alerts
        * ...

* [MORE](https://github.com/dancer1325/prometheus/blob/main/docs/querying/basics.md)

# Precise alerting
* alerting rules
  * -- based on -- PromQL + dimensional data model

* Alertmanager 
  * == component
    * ⚠️separated⚠️
  * handles 
    * notifications
    * silencing

* [MORE](https://github.com/dancer1325/prometheus-alertmanager/blob/main/docs/overview.md)

# Simple operation
* Prometheus servers
  * operate ⚠️INDEPENDENTLY⚠️
  * rely ONLY -- on -- local storage
    * ❌!= distributed storage❌
  * developed | Go
  * statically linked binaries
    * == Prometheus executables include 👀ALSO ALL dependencies👀
    * -> 👀easy to deploy | VARIOUS environments👀

* [how to configure](https://github.com/dancer1325/prometheus/blob/main/docs/configuration/configuration.md)

# Metrics instrumentation libraries
* types
  * official
  * community-contributed
* cover MOST major languages

* [MORE](/prometheus-website/docs/instrumenting/clientlibs.md)

# Integrations
* types
  * official
  * community-contributed

* allow you to
  * easily extract metrics -- from -- existing systems

* [MORE](/prometheus-website/docs/instrumenting/exporters.md)


# Others
* [here](/prometheus-website/docs/introduction/overview.md)
