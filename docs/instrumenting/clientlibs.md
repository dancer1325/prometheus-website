---
title: Client libraries
sort_rank: 1
---

* Prometheus client libraries
  * implement the Prometheus [metric types](../concepts/metric_types.md) 
  * allows
    * monitor your services
    * define & expose internal metrics -- via -- HTTP endpoint | your application’s instance
  * ways
    * official ones
      * [Go](https://github.com/prometheus/client_golang)
      * [Java or Scala](https://github.com/prometheus/client_java)
      * [Python](https://github.com/prometheus/client_python)
      * [Ruby](https://github.com/prometheus/client_ruby)
      * [Rust](https://github.com/prometheus/client_rust)
    * third-party ones
      * [Bash](https://github.com/aecolley/client_bash)
      * [C](https://github.com/digitalocean/prometheus-client-c)
      * [C++](https://github.com/jupp0r/prometheus-cpp)
      * [Common Lisp](https://github.com/deadtrickster/prometheus.cl)
      * [Dart](https://github.com/tentaclelabs/prometheus_client)
      * [Delphi](https://github.com/marcobreveglieri/prometheus-client-delphi)
      * [Elixir](https://github.com/deadtrickster/prometheus.ex)
      * [Erlang](https://github.com/deadtrickster/prometheus.erl)
      * [Haskell](https://github.com/fimad/prometheus-haskell)
      * [Julia](https://github.com/fredrikekre/Prometheus.jl)
      * [Lua](https://github.com/knyar/nginx-lua-prometheus) for Nginx
      * [Lua](https://github.com/tarantool/metrics) for Tarantool
      * [.NET / C#](https://github.com/prometheus-net/prometheus-net)
      * [Node.js](https://github.com/siimon/prom-client)
      * [OCaml](https://github.com/mirage/prometheus)
      * [Perl](https://metacpan.org/pod/Net::Prometheus)
      * [PHP](https://github.com/promphp/prometheus_client_php)
      * [R](https://github.com/cfmack/pRometheus)
    * implement some supported [exposition formats](exposition_formats.md)
      * use case
        * NO client library is AVAILABLE | your language
        * avoid dependencies
      * [how to write client libraries](writing_clientlibs)
  * 's work
    * 👀| Prometheus scrapes your instance's HTTP endpoint,👀
      * client library sends ALL tracked metrics' CURRENT state -- to the -- server
