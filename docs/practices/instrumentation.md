---
title: Instrumentation
sort_rank: 3
---

* goal
  * how to instrument your code

## How to instrument

* instrument everything (library + subsystem + service)
  * Reason:🧠check the performance🧠

* instantiate the metric classes | file == file / use the metric
  * Reason:🧠
    * clean
    * easy to look up🧠

### types of services

* types of services,
  * | monitoring point of view,
    * online-serving,
    * offline-processing,
    * batch jobs

#### Online-serving systems

* use cases
  * human or another system expects an IMMEDIATE response
    * _Example:_ MOST database and HTTP requests 

* MAIN metrics
  * number of
    * performed queries,
    * errors,
    * in-progress requests
    * [failed queries](#failures) 
  * latency

* requirements
  * monitor | client & server side

* recommendations
  * count queries 
    * ALWAYS | start OR end
    * | end
      * Reason:🧠contains error + latency stats🧠

#### Offline processing

* use cases
  * NO ONE ACTIVELY waits for a response
  * batch

* MAIN metrics
  * items / 
    * come in
    * in progress,
    * sent out
  * last time | you processed something,
  * batches / go
    * in
    * out

#### Batch jobs

* Batch jobs
  * vs offline-processing 
    * ❌NOT run CONTINUOUSLY❌
      * -> scraping MORE DIFFICULT
  * 's metrics
    * [pushed to a PushGateway](../instrumenting/pushing.md)
    * measured -- via -- gauges
  * recommendations
    * if 
      * batch jobs take to run MULTIPLE minutes -> scrap -- via -- PULL-based monitoring
      * run very often (every 15 minutes) -> 
        * convert them into daemons
        * handle them as offline-processing jobs

* MAIN metrics
  * last time it completed (succeeded or failed)
  * how long each major stage of the job took
  * overall
    * runtime
    * job-specific statistics (total number of records processed)

### Subsystems

* == systems' sub-parts

#### Libraries

* Libraries
  * requirements
    * provide instrumentation / NO ADDITIONAL configuration -- required by -- users
  * recommendations
    * if you use it to access resource outside of the process (_Example:_ network, disk, or IPC) -> track the overall query count + errors + latency
    * track internal errors & latency | library itself

#### Logging

* recommendations
  * counter / EVERY line of logging code
    * Reason:🧠counter's
      * frequency
      * how long🧠

* if there are MULTIPLE closely-related log messages | SAME function -> increment 1! counter / ALL of them 
  * _Example:_ different if OR switch statement's branches 

* uses
  * export the total number of info/error/warning lines / were logged -- by the -- application
  * check for significant differences as part of your release process

#### Failures

* Failures
  * ' handling vs logging's handling
    * counter / EVERY failure
      * bubble up | MORE general error counter

#### Threadpools

* MAIN metrics
  * number of
    * queued requests, 
    * threads | use,
    * threads,
    * tasks processed,
  * how long
    * they took
    * things were waiting | queue

#### Caches

* MAIN metrics
  * total queries,
  * hits,
  * overall latency
  * errors

#### Collectors

* | implement a non-trivial custom metrics collector,
  * export a gauge for 
    * how long the collection took | seconds
    * the number of errors encountered

## Things to watch out for

### Use labels

Few monitoring systems have the notion of labels and an expression language to
take advantage of them, so it takes a bit of getting used to.

When you have multiple metrics that you want to add/average/sum, they should
usually be one metric with labels rather than multiple metrics.

For example, rather than `http_responses_500_total` and `http_responses_403_total`,
create a single metric called `http_responses_total` with a `code` label
for the HTTP response code
* You can then process the entire metric as one in
rules and graphs.

As a rule of thumb, no part of a metric name should ever be procedurally
generated (use labels instead)
* The one exception is when proxying metrics
from another monitoring/instrumentation system.

See also the [naming](/docs/practices/naming/) section.

### Do not overuse labels

Each labelset is an additional time series that has RAM, CPU, disk, and network
costs
* Usually the overhead is negligible, but in scenarios with lots of
metrics and hundreds of labelsets across hundreds of servers, this can add up
quickly.

As a general guideline, try to keep the cardinality of your metrics below 10,
and for metrics that exceed that, aim to limit them to a handful across your
whole system
* The vast majority of your metrics should have no labels.

If you have a metric that has a cardinality over 100 or the potential to grow
that large, investigate alternate solutions such as reducing the number of
dimensions or moving the analysis away from monitoring and to a general-purpose
processing system.

To give you a better idea of the underlying numbers, let's look at node\_exporter.
node\_exporter exposes metrics for every mounted filesystem
* Every node will have
in the tens of timeseries for, say, `node_filesystem_avail`
* If you have
10,000 nodes, you will end up with roughly 100,000 timeseries for
`node_filesystem_avail`, which is fine for Prometheus to handle.

If you were to now add quota per user, you would quickly reach a double digit
number of millions with 10,000 users on 10,000 nodes
* This is too much for the
current implementation of Prometheus
* Even with smaller numbers, there's an
opportunity cost as you can't have other, potentially more useful metrics on
this machine any more.

If you are unsure, start with no labels and add more labels over time as
concrete use cases arise.

### Counter vs
* gauge, summary vs
* histogram

It is important to know which of the four main metric types to use for
a given metric.

To pick between counter and gauge, there is a simple rule of thumb: if
the value can go down, it is a gauge.

Counters can only go up (and reset, such as when a process restarts)
* They are
useful for accumulating the number of events, or the amount of something at
each event
* For example, the total number of HTTP requests, or the total number of
bytes sent in HTTP requests
* Raw counters are rarely useful
* Use the
`rate()` function to get the per-second rate at which they are increasing.

Gauges can be set, go up, and go down
* They are useful for snapshots of state,
such as in-progress requests, free/total memory, or temperature
* You should
never take a `rate()` of a gauge.

Summaries and histograms are more complex metric types discussed in
[their own section](/docs/practices/histograms/).

### Timestamps, not time since

If you want to track the amount of time since something happened, export the
Unix timestamp at which it happened - not the time since it happened.

With the timestamp exported, you can use the expression `time() - my_timestamp_metric` to
calculate the time since the event, removing the need for update logic and
protecting you against the update logic getting stuck.

### Inner loops

In general, the additional resource cost of instrumentation is far outweighed by
the benefits it brings to operations and development.

For code which is performance-critical or called more than 100k times a second
inside a given process, you may wish to take some care as to how many metrics
you update.

A Java counter takes
[12-17ns](https://github.com/prometheus/client_java/blob/main/benchmarks/README.md)
to increment depending on contention
* Other languages will have similar
performance
* If that amount of time is significant for your inner loop, limit
the number of metrics you increment in the inner loop and avoid labels (or
cache the result of the label lookup, for example, the return value of `With()`
in Go or `labels()` in Java) where possible.

Beware also of metric updates involving time or durations, as getting the time
may involve a syscall
* As with all matters involving performance-critical code,
benchmarks are the best way to determine the impact of any given change.

### Avoid missing metrics

Time series that are not present until something happens are difficult
to deal with, as the usual simple operations are no longer sufficient to
correctly handle them
* To avoid this, export a default value such as `0` for
any time series you know may exist in advance.

Most Prometheus client libraries (including Go, Java, and Python) will
automatically export a `0` for you for metrics with no labels.
