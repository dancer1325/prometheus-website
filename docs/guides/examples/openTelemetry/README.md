* goal
  * open telemetry

# Enable the OTLP receiver
## by default, it's disabled
* `docker compose up -d`
* http://localhost:9090/flags
  * check that "--web.enable-otlp-receiver" is false
## if you want to enable -> pass CLI flag `--web.enable-otlp-receiver`
* uncomment | "docker-compose.yml"
* `docker compose up -d`
* http://localhost:9090/flags
  * check that "--web.enable-otlp-receiver" is true
### OTLP metrics received | `/api/v1/otlp/v1/metrics` path
* Attempts:
  * Attempt1: http://localhost:9090/api/v1/otlp/v1/metrics
  * Attempt2: [sample.http](sample.http)
* Solution:
  * TODO:

# Send OpenTelemetry Metrics -- to the -- Prometheus Server
* TODO: 
