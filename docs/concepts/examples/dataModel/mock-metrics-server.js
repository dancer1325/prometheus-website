import http from 'http';

let requestCount = 0;
let startTime = Date.now();

const server = http.createServer((req, res) => {
  //            /metrics            Prometheus' standard endpoint | expose metrics
  if (req.url === '/metrics') {
    requestCount++;
    const uptime = Math.floor((Date.now() - startTime) / 1000);
    
    const metrics = `# HELP http_requests_total Total HTTP requests
# TYPE http_requests_total counter
http_requests_total{code="200",handler="/",instance="localhost:3001",job="mock-app"} ${requestCount}

# HELP process_uptime_seconds Process uptime
# TYPE process_uptime_seconds gauge
process_uptime_seconds ${uptime}

# HELP random_value Random increasing value
# TYPE random_value gauge
random_value ${Math.floor(Math.random() * 100) + requestCount}

# HELP "app.legacy-metrics.cpu-usage" Legacy CPU usage metric with special characters
# TYPE "app.legacy-metrics.cpu-usage" gauge
{"app.legacy-metrics.cpu-usage",instance="localhost:3001",job="mock-app"} ${Math.floor(Math.random() * 100)}
`;

    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end(metrics);
  } else {
    res.writeHead(404);
    res.end('Not found');
  }
});

server.listen(3001, () => {
  console.log('Mock metrics server running on http://localhost:3001/metrics');
});