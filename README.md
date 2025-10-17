# 🐳 FastAPI Docker Project – Documentation

## 🔹 Overview
This project demonstrates how to containerize a small **FastAPI** web application using **Docker**.  
It shows how Docker images, containers, and the underlying components work together.

---

## 🧩 Components Used

| Component | Purpose |
|------------|----------|
| **main.py** | The FastAPI app (Python code) |
| **Python & pip** | Runtime and dependency manager inside the image |
| **Dockerfile** | Recipe describing how to build the image |
| **Docker Image** | Blueprint containing OS + Python + dependencies + app |
| **Docker Container** | A running instance of the image |
| **Docker Engine / Desktop** | The runtime that builds & runs containers |
| **Uvicorn** | Server that runs the FastAPI app inside the container |
| **VS Code** | IDE for editing and running Docker commands easily |

---

## 🔁 Flowchart – How Everything Works
<img width="332" height="698" alt="image" src="https://github.com/user-attachments/assets/81c12886-a517-401d-8ccb-d853a7976cbb" />

🧱 1. Build the Image
bash
Copy code
docker build -t fastapi-demo .
What happens:

Docker reads the Dockerfile

Pulls the base image python:3.11-slim

Installs dependencies (pip install fastapi uvicorn)

Copies your app code into the image

Creates a final image named fastapi-demo:latest

🚀 2. Run the Container
bash
Copy code
docker run -d -p 8000:8000 --name fastapi-container fastapi-demo
What happens:

Docker creates a running instance (container) from the image

The container runs the command from the Dockerfile:

nginx
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000
Port 8000 in the container is mapped to your PC’s port 8000

You can access your app at http://localhost:8000

🧠 3. Key Concepts
Term	Description
Image	Read-only blueprint containing all dependencies
Container	Live, running instance of an image
Build Context (.)	Files/folders sent to Docker during build
Layer	Each instruction in Dockerfile forms a cached image layer
Port Mapping (-p)	Connects container port → host port
Detached Mode (-d)	Runs container in background
CMD	Command that starts automatically when container runs

🧰 4. Useful Docker Commands
bash
Copy code
docker images               # List images
docker ps                   # List running containers
docker ps -a                # List all containers
docker logs fastapi-container
docker exec -it fastapi-container bash
docker stop fastapi-container
docker rm fastapi-container
docker rmi fastapi-demo
📦 Why Docker Matters
✅ Reproducible environments
✅ Isolation from host system
✅ Easy to share (works anywhere)
✅ Clean, fast setup and teardown
✅ Ideal for DevOps, CI/CD, and cloud deployments

🌐 How Networking Works
The container runs its own isolated network stack

-p 8000:8000 maps internal port 8000 → your PC’s port 8000

Requests from browser → Docker engine → container → Uvicorn → FastAPI

🧭 Summary
Step	Action	Result
1	Write FastAPI code	app ready
2	Write Dockerfile	build recipe
3	Build image	environment packaged
4	Run container	app running on localhost
5	Test in browser	FastAPI responds

