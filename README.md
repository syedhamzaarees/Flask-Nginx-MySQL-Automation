# 🚀 Flask-based Web Application with Nginx Reverse Proxy and MySQL — Fully Automated via Jenkins & GitHub

## 📦 Project Overview
A fully containerized and automated **three-tier architecture** using:
- **Flask** (Python backend)
- **Nginx** (reverse proxy)
- **MySQL** (database)
- **Docker & Docker Compose**
- **Jenkins CI/CD pipeline** with **GitHub Webhooks**

Whenever new code is pushed to GitHub, Jenkins automatically:
1. Pulls the latest code  
2. Builds Docker images for Flask & Nginx  
3. Pushes images to Docker Hub  
4. Deploys the containers using Docker Compose  

---

## 🧰 Tech Stack
| Layer | Technology |
|-------|-------------|
| Backend | Flask (Python) |
| Proxy | Nginx |
| Database | MySQL |
| Containerization | Docker, Docker Compose |
| CI/CD | Jenkins + GitHub Webhooks |
| Version Control | Git / GitHub |
| Host | Ubuntu Server (VirtualBox VM) |

---

## 🧱 Folder Structure
.
├── flask_app/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── nginx/
│ ├── default.conf
│ └── Dockerfile├── docker-compose.yaml
├── Jenkinsfile
└── README.md

---

## 🔄 Jenkins Pipeline Flow
1. Clone Code from GitHub  
2. Build Flask & Nginx Docker Images  
3. Push Flask image to Docker Hub  
4. Deploy containers via `docker-compose`  

All these stages are implemented using **Jenkins Shared Libraries** (`Demo-Shared-Library`).

---

## 🧠 Key Learnings
- Building multi-container apps with Docker  
- Automating deployment pipelines using Jenkins  
- Triggering CI/CD via GitHub Webhooks  
- Working with Docker Hub tokens securely  

---

## 👨‍💻 Author
**Syed Hamza Arees**  
- 🧠 DevOps Engineer | Cloud & Automation Learner  
- 🔗 [LinkedIn](https://www.linkedin.com/in/syedhamzaarees)  
- 🐙 [GitHub](https://github.com/syedhamzaarees)




