# ---------------------------------------------------
# Prometheus and Grafana
# Scraping Prometheus Metrics and Visualizing in Grafana
# ---------------------------------------------------

mkdir monitoring

cd monitoring

# ---------------------------------------------------
# Install Docker Compose
# ---------------------------------------------------

sudo apt update

sudo apt install docker-compose-v2 -y

docker compose version

# ---------------------------------------------------
# Create docker-compose.yml
# ---------------------------------------------------

nano docker-compose.yml

version: '3'

services:

  prometheus:

    image: prom/prometheus

    container_name: prometheus

    ports:
      - "9090:9090"

    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:

    image: grafana/grafana

    container_name: grafana

    ports:
      - "3000:3000"

# ---------------------------------------------------
# Create prometheus.yml
# ---------------------------------------------------

nano prometheus.yml

global:

  scrape_interval: 15s

scrape_configs:

  - job_name: "prometheus"

    static_configs:

      - targets: ["prometheus:9090"]

# ---------------------------------------------------
# Start Containers
# ---------------------------------------------------

sudo docker compose up -d

sudo docker ps

# Verify containers:
# prometheus
# grafana

# ---------------------------------------------------
# Open Prometheus
# ---------------------------------------------------

# http://localhost:9090

# Run Queries

prometheus_ready

process_resident_memory_bytes

prometheus_http_requests_total

# ---------------------------------------------------
# Open Grafana
# ---------------------------------------------------

# http://localhost:3000

# Username
admin

# Password
admin

# ---------------------------------------------------
# Add Prometheus Data Source
# ---------------------------------------------------

# Connections -> Add new connection

# Search:
Prometheus

# Add new data source

# URL
http://prometheus:9090

# Click:
Save & Test

# ---------------------------------------------------
# Create Dashboard
# ---------------------------------------------------

# Dashboards -> New Dashboard

# Add Visualization

# Select:
Prometheus Data Source

# ---------------------------------------------------
# Visualization 1
# ---------------------------------------------------

# Query
process_resident_memory_bytes

# Visualization
Time Series

# Apply

# ---------------------------------------------------
# Visualization 2
# ---------------------------------------------------

# Add Visualization

# Query
prometheus_http_requests_total

# Visualization
Time Series

# Apply

# ---------------------------------------------------
# Stop Containers
# ---------------------------------------------------

sudo docker compose down
