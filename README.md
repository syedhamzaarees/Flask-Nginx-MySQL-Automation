# Flask + Nginx + MySQL (Docker Compose)

## Overview
This is a 3-tier web application built using:
- **Backend:** Flask
- **Database:** MySQL
- **Reverse Proxy:** Nginx  
All services are containerized and orchestrated with **Docker Compose**.

## Features
- Containerized Flask app with isolated dependencies  
- Nginx reverse proxy configured for Flask  
- Persistent MySQL database using Docker volumes  
- Port mapping and volume binding for easy development  

## How to Run
```bash
git clone https://github.com/syedhamzaarees/Flask-Nginx-MySQL-Docker-Compose.git
cd Flask-Nginx-MySQL-Docker-Compose
docker-compose up --build
