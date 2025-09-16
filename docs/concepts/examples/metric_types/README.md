* goal
    * types of configurations
    *

# requirements

* install [Prometheus & Promtool](/prometheus/README.md#install)
* `make assets`

# uses / metric types can be distinguished
* `python metrics_example.py`
  * check log messages
* http://localhost:8000/metrics

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

