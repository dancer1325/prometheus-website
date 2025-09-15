* goal
  * file-sd

# requirements

* install [Prometheus & Promtool](/prometheus/README.md#install)
* `make assets`
* | this path,
  * `prometheus --config.file=prometheus.yml`
* | [web/ui](https://github.com/dancer1325/prometheus/tree/main/web/ui)
  * `npm run start`

# install & run Node Exporter

* steps
  * | [here](node_exporter-1.9.1.darwin-arm64)
    * `./node_exporter`

# install, configure & run Prometheus

* steps
  * | this path,
    * create MANUAL "target.json"
    * `prometheus --config.file=prometheus.yml`
  * | browser,
    * http://localhost:5173/query,
      * look up "node_"
      * `up{job="node"}`
        * check Node Exporter is being PROPERLY discovered

# Changing the targets list dynamically

* steps
  * | [here](node_exporter-1.9.1.darwin-arm64)
    * `./node_exporter --web.listen-address=":9200"`
  * | ["targets.json"](targets.json),
    * add
      ```json
      {
        "targets": [
          "localhost:9200"
        ],
        "labels": {
          "job": "node"
        }
      }  
      ```
  * | browser,
    * http://localhost:5173/query
      * `up{job="node"}`
        * check 's return 2 
