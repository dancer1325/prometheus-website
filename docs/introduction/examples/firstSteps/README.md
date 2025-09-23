# requirements

* install [Prometheus](/prometheus/README.md#install)

# configure Prometheus
## default Prometheus configuration file
* steps
  * `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`
  * `docker exec -it prometheus sh`
  * `cat /etc/prometheus/prometheus.yml`

## `scrape_interval`
### `global.scrape_interval`
* `docker compose up -d`
* check
  * http://localhost:9090/config
    * `scrape_configs[*].scrape_interval` = 15s
  * http://localhost:9090/targets
    * refresh continuously / check | AFTER 15s, the last scrape, it starts

### `scrape_configs[*].scrape_interval`
* `docker compose up -d`
* check
  * http://localhost:9090/config
    * `scrape_configs[*].scrape_interval` = 15s

## `evaluation_interval` & `rule_files`
* `docker compose up -d`
* check
  * http://localhost:9090/rules
    * refresh continuously / check | AFTER 15s, the last run, it starts

## OWN Prometheus' exposed metrics
* http://localhost:9090/metrics

# Using the expression browser & graph interface
* steps
  * http://localhost:9090/query, 
    * table
      * `promhttp_metric_handler_requests_total`
        * MULTIPLE time series == MULTIPLE labels o dimensions
        * `promhttp_metric_handler_requests_total{code="200"}`
          * 1! time series
        * `count(promhttp_metric_handler_requests_total)`
          * 's return
            * scalar
              * != time series
    * graph,
      * `rate(promhttp_metric_handler_requests_total{code="200"}[1m])`

