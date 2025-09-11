* := monitoring solution
  * allows
    * about metrics
      * instrument
        * == | your applications, 
          * add code / expose metrics
      * collect
        * Prometheus pull (== scrap) your services' HTTP endpoints
      * store -- as -- ⭐️time series data⭐️
      * query 
    * monitor your applications, systems & services
  * open source
  * use cases
    * alerting
    * dashboarding
  * [active ecosystem](/prometheus-website/src/app/community)
  * history
    * | 2012, built | [SoundCloud](http://soundcloud.com) 
    * | 2016, part of [CNCF](https://cncf.io/)
      * 2@ project / got `graduate` status
        * 1@ was Kubernetes
  * ONLY system / 👀directly supported -- by -- [Kubernetes](https://kubernetes.io/)👀

* time series data
  * == 💡timestamp (| was recorded) + optional labels (== key-value pairs)💡
  * _Example:_ 
    ```text
    http_requests_total{method="GET", status="200"} 1547 @1609459200
    # 1547                              == number of requests
    # @1609459200                       == timestamp | it was registered
    # {method="GET", status="200"}      == labels
    ```

* [MORE](/prometheus-website/docs/introduction/overview.md)
