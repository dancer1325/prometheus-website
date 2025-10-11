package main

import (
	"log"
	"math/rand"
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
	// Crear native histogram
	requestDuration := prometheus.NewHistogram(prometheus.HistogramOpts{
		Name: "http_request_duration_seconds",
		Help: "HTTP request duration in seconds",
		// Configuración para native histogram
		NativeHistogramBucketFactor:     1.1,       // Factor exponencial
		NativeHistogramMaxBucketNumber:  100,       // Máximo buckets
		NativeHistogramMinResetDuration: time.Hour, // Reset mínimo
	})

	// Registrar métrica
	prometheus.MustRegister(requestDuration)

	// Simular observaciones
	go func() {
		for {
			// Generar latencias realistas
			latency := rand.Float64() * 2.0 // 0-2 segundos
			requestDuration.Observe(latency)
			time.Sleep(100 * time.Millisecond)
		}
	}()

	// Exponer métricas
	http.Handle("/metrics", promhttp.Handler())
	log.Println("Native histogram server running on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
