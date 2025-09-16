---
title: Grafana support for Prometheus
nav_title: Grafana
sort_rank: 2
---

* [Grafana](http://grafana.com/)
  * == analytics & visualization platform
    * open-source  
  * allows users,
    * about dashboards
      * create,
      * explore,
      * share
  * uses
    * FROM MULTIPLE data sources,
      * monitor
      * analyze metrics 
  * use cases
    * observability
  * support
    * integrations -- with -- databases (_Examples:_ Prometheus, InfluxDB, Elasticsearch, ...)
      * _Example:_ Grafana data source -- for -- Prometheus
        * requirements
          * Grafana v2.5.0 (2015-10-28)
  * provide
    * alerting,
    * plugin extensibility
    * query editor -- for -- real-time data visualization /
      * flexible

* _Example:_ Grafana dashboard / queries Prometheus -- for -- data

  [![Grafana screenshot](/prometheus-website/public/assets/docs/grafana_prometheus.png)](/assets/docs/grafana_prometheus.png)

## Installing

* follow [official Grafana documentation](https://grafana.com/grafana/download/)

## Using

* | browser,
  * http://localhost:3000, 
    * default one
    * login
      * "admin" / "admin"

### Creating a Prometheus data source | Grafana

1. Click on the "cogwheel" in the sidebar to open the Configuration menu.
2. Click on "Data Sources".
3. Click on "Add data source".
4. Select "Prometheus" as the type.
5. Set the appropriate Prometheus server URL (for example, `http://localhost:9090/`)
6. Adjust other data source settings as desired (for example, choosing the right Access method).
7. Click "Save & Test" to save the new data source.

The following shows an example data source configuration:

[![Data source configuration](/assets/docs/grafana_configuring_datasource.png)](/assets/docs/grafana_configuring_datasource.png)

### Creating a Prometheus graph

Follow the standard way of adding a new Grafana graph. Then:

1. Click the graph title, then click "Edit".
2. Under the "Metrics" tab, select your Prometheus data source (bottom right).
3. Enter any Prometheus expression into the "Query" field, while using the
   "Metric" field to lookup metrics via autocompletion.
4. To format the legend names of time series, use the "Legend format" input. For
   example, to show only the `method` and `status` labels of a returned query
   result, separated by a dash, you could use the legend format string
   `{{method}} - {{status}}`.
5. Tune other graph settings until you have a working graph.

The following shows an example Prometheus graph configuration:
[![Prometheus graph creation](/assets/docs/grafana_qps_graph.png)](/assets/docs/grafana_qps_graph.png)

In Grafana 7.2 and later, the `$__rate_interval` variable is
[recommended](https://grafana.com/docs/grafana/latest/datasources/prometheus/#using-__rate_interval)
for use in the `rate`and `increase` functions.

### Importing pre-built dashboards from Grafana.com

Grafana.com maintains [a collection of shared dashboards](https://grafana.com/dashboards)
which can be downloaded and used with standalone instances of Grafana. Use
the Grafana.com "Filter" option to browse dashboards for the "Prometheus"
data source only.

You must currently manually edit the downloaded JSON files and correct the
`datasource:` entries to reflect the Grafana data source name which you
chose for your Prometheus server. Use the "Dashboards" → "Home" → "Import"
option to import the edited dashboard file into your Grafana install.
