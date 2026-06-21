---

# ☀️ HeliosGrid: Cloud-Native Renewable Energy Telemetry

An enterprise-grade, microservices-based IoT telemetry platform designed to monitor renewable energy infrastructure (solar arrays, wind turbines, and battery storage) in real-time.

This project demonstrates a complete, secure, and production-ready DevOps lifecycle, focusing on high availability, zero-trust security, and full-stack observability.

---

## 📖 The Problem Statement

In the renewable energy sector, managing physical infrastructure requires continuous, real-time telemetry. Traditional monolithic monitoring applications suffer from critical flaws:

1. **Fragility:** They cannot scale dynamically and crash under data loads.
2. **Security Risks:** API keys and credentials are often hardcoded into source code.
3. **Zero Visibility:** Operators lack centralized, real-time metrics when system failures occur.

**The Solution:** HeliosGrid engineered a Cloud-Native DevOps Ecosystem that guarantees high availability via Kubernetes orchestration, enforces zero-trust security using HashiCorp Vault, and provides real-time infrastructure observability through Prometheus and Grafana.

---

## 🛠️ Architecture & Tech Stack

* **Application:** Python (Flask/FastAPI) simulating live IoT hardware telemetry.
* **Containerization:** Docker
* **CI/CD Automation:** Jenkins (Dockerized Pipeline)
* **Container Orchestration:** Kubernetes (Minikube/Kind)
* **Secrets Management:** HashiCorp Vault (Dev-Mode Container)
* **Observability & Monitoring:** Prometheus (Time-Series DB) & Grafana (Dashboards)
* **Infrastructure as Code (IaC):** Terraform

---

## 🚀 Quick Start & Deployment Guide

### 1. Prerequisites

Ensure you have the following installed on your local machine:

* Docker Engine
* Kubernetes CLI (`kubectl`)
* Local K8s Cluster (Minikube or Kind)

### 2. Start the Local Vault (Secrets Management)

HeliosGrid uses a zero-trust model. The application requires a Vault instance to inject the Weather API Key at runtime.

```bash
# Start Vault in Dev Mode
docker run -d --name local-vault -p 8200:8200 -e "VAULT_DEV_ROOT_TOKEN_ID=my-super-secret-token" hashicorp/vault

```

* Navigate to `http://localhost:8200` and log in with token: `my-super-secret-token`.
* Create a secret engine path `helios-config` and add the Key: `WEATHER_API_KEY` and Value: `SolarWindGrid9921_Secure!`.

### 3. Deploy the Kubernetes Infrastructure

Start your local cluster and apply the declarative deployment files.

```bash
# Apply all Kubernetes manifests (Deployments & Services)
kubectl apply -f .

# Verify all pods are running
kubectl get pods

```

### 4. Access the Command Center (Port Forwarding)

Once the pods show a status of `Running`, open the internal network tunnels:

```bash
# 1. HeliosGrid Telemetry API
kubectl port-forward svc/heliosgrid-service 30080:8080

# 2. Prometheus Metrics Engine
kubectl port-forward svc/prometheus-service 30090:9090

# 3. Grafana Dashboard
kubectl port-forward svc/grafana-service 30300:3000

```

* **App URL:** [http://localhost:30080/telemetry](https://www.google.com/search?q=http://localhost:30080/telemetry)
* **Grafana URL:** [http://localhost:30300](https://www.google.com/search?q=http://localhost:30300) *(Default Login: admin / admin)*

---

## 🔄 CI/CD Pipeline Integration

This project utilizes a `Jenkinsfile` to automate the build, test, and deployment phases. The Jenkins server runs locally via Docker (`docker start jenkins-local`), connected on port `8081`. The pipeline ensures that any changes pushed to the repository automatically trigger a new Docker image build and update the Kubernetes rollout.

---

## ⚠️ Infrastructure Constraints & Logging Strategy

*Note regarding ELK Stack Implementation:* A full-scale ELK stack (Elasticsearch, Logstash, Kibana) deployment was initially architected and attempted for centralized log aggregation. However, due to hardware-level system call filtering constraints and JVM memory limitations inherent to running heavyweight enterprise Java applications inside a local Kubernetes cluster on Apple Silicon (ARM64), Elasticsearch encountered bootstrap check failures.

As a strategic engineering decision to prioritize cluster stability and system availability, the observability strategy was pivoted to rely fully on the lightweight **Prometheus and Grafana** stack for complete infrastructure visibility.

---

## 📂 Repository Structure

* `/kubernetes` - K8s Deployment and Service YAML manifests
* `/terraform` - IaC configuration scripts (`main.tf`)
* `/docs` - Architecture diagrams and Disaster Recovery plans
* `app.py` - Core application logic
* `Dockerfile` - Container build instructions
* `Jenkinsfile` - CI/CD Pipeline configuration

---

**Prepared for Project Presentation.**
