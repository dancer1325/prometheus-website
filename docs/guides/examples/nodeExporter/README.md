* goal
  * node exporter

# requirements

* install [Prometheus & Promtool](/prometheus/README.md#install)
* `make assets`
* | this path,
  * `prometheus --config.file=prometheus.yml`
* | [web/ui](https://github.com/dancer1325/prometheus/tree/main/web/ui)
  * `npm run start`

# download + extract + run
* steps
  * [download](https://github.com/prometheus/node_exporter/releases) + extract | [here](node_exporter-1.9.1.darwin-arm64)
    ```bash
    # NOTE: Replace the URL with one from the above mentioned "downloads" page.
    # <VERSION>, <OS>, and <ARCH> are placeholders.
    wget https://github.com/prometheus/node_exporter/releases/download/v<VERSION>/node_exporter-<VERSION>.<OS>-<ARCH>.tar.gz
    tar xvfz node_exporter-*.*-amd64.tar.gz
    ```
  * | [node_exporter-1.9.1.darwin-arm64](node_exporter-1.9.1.darwin-arm64)
    * `./node_exporter`
      * Problems:
        * Problem1: "Apple could not verify “node_exporter” is free of malware that may harm your Mac or compromise your privacy."
          * Solution: `xattr -d com.apple.quarantine ./node_exporter`

* | browser,
  * http://localhost:9100/metrics
    * check "node_"
  * http://localhost:9090/metrics
    * NOT find "node_"

# configure Prometheus' instance

* steps
  * | [prometheus.yml](prometheus.yml), add
    ```yaml
    scrape_configs:
    - job_name: node
      static_configs:
      - targets: ['localhost:9100']
    ```
  * | browser,
    * http://localhost:5173/query,
      * look up "node_" and check ALL suggested node-exporter's metrics
        * _Examples:_
          * `node_filesystem_avail_bytes`
          * `rate(node_cpu_seconds_total{mode="system"}[1m])`
          * `rate(node_network_receive_bytes_total[1m])`