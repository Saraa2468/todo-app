# 🧩 DevOps Monitoring Project: Todo App with Docker, Prometheus & Grafana

## 📘 Project Overview
This project demonstrates how to containerize a simple *Flask-based Todo Application, implement **monitoring* using *Prometheus, cAdvisor, and Grafana, and integrate **CI/CD* using Jenkins.

The goal of this project is to showcase end-to-end DevOps skills — from application containerization to automated deployment and monitoring.

---

## ⚙️ Tech Stack
- *Flask* – Python web framework for the Todo App  
- *Docker* – Containerization for consistent environments  
- *Prometheus* – Metrics collection and monitoring  
- *cAdvisor* – Container-level resource usage metrics  
- *Grafana* – Visualization and dashboards  
- *Jenkins* – Continuous Integration & Deployment  

---

## 🏗️ Project Architecture
+———————+
|   Flask Todo App    |
| (Python + HTML)     |
+–––––+–––––+
|
v
+———————+
|      Docker         |
|  (Containerization) |
+–––––+–––––+
|
v
+———————+
|   cAdvisor + Prometheus  |
| (Monitoring Stack)       |
+–––––+—————+
|
v
+———————+
|       Grafana       |
| (Metrics Dashboard)  |
+–––––+—————+

## How to Run the Project 
1. Clone the repository git clone
https://github.com/yourusername/todo-devops-project.git cd todo-devops-project
2. Run Docker Compose docker-compose up --build
3. Access the services
   - Todo App → http://localhost:5000
   - Prometheus → http://localhost:9090
   - Grafana → http://localhost:3000
   - cAdvisor → http://localhost:9100
     
## Monitoring Setup 
- cAdvisor collects container metrics like CPU, Memory, and Disk I/O.
- Prometheus scrapes these metrics from cAdvisor.
- Grafana visualizes Prometheus metrics through dashboards.
  
Example Prometheus configuration: scrape_configs:
- job_name: "cadvisor" static_configs:
  targets: ["cadvisor:8080"]
  
Example Grafana Metrics Displayed: 
- Container CPU Usage (%)
- Memory Consumption (MB)
- Container Uptime
- Number of Running Containers
- 
## CI/CD Integration (Jenkins) Every commit triggers: 
1. Jenkins pipeline build
2. Docker image creation
3. Deployment of the updated app
