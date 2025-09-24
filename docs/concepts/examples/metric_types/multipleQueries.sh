for i in $(seq 1 50); do
  curl -sS http://localhost:9090/metrics --limit-rate 20k -o /dev/null &
done

# Opcional: guarda los PIDs para detenerlas luego
jobs -p > /tmp/metrics_pids.txt
