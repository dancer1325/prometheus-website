* goal
    * types of configurations
    *

# requirements

* install [Prometheus & Promtool](/prometheus/README.md#install)
* `make assets`

# uses / metric types can be distinguished
* | root path
  * `prometheus --config.file=docs/concepts/examples/metric_types/simple-prometheus.yml --web.listen-address=:9090`
* `curl http://localhost:9090/metrics`
  * 's return
    * wire protocol / 👀expressed | units👀
* `pip3 install prometheus-client` & `python3 metrics_example.py`
  * check EACH metric type is distinguished
    * Reason: 🧠NOT ALLOWED any action🧠

# uses / metric types can NOT be distinguished
* | root path
    * `prometheus --config.file=docs/concepts/examples/metric_types/simple-prometheus.yml --web.listen-address=:9090`
      * Problems:
        * Problem1: "Error opening React index.html: open static/mantine-ui/index.html: no such file or directory"
          * Reason: 🧠/web/ui is generated | prometheus source code
          * Solution: 💡run independently 💡
            * via [npm](https://github.com/dancer1325/prometheus/tree/main/web/ui#how-to-run-local-development-server)
* | browser, http://localhost:9090/graph
  * 

