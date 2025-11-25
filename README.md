YT Downloader – Local Media Processing Pipeline

A lightweight, container-ready web application built with Flask and yt-dlp, designed to download YouTube videos or extract audio tracks with fast local processing.
This project demonstrates clean architecture, containerization, and cloud deployment readiness—ideal for DevOps and Cloud Engineering workflows.

🚀 Key Features

Fast YouTube downloads using yt-dlp

Automatic MP3 audio extraction

Fully local processing (no data stored server-side)

Minimal, responsive web UI

Production-ready Dockerfile (optimized image < 200MB)

Easily deployable to Azure App Service or Azure Container Apps

🏗️ High-Level Architecture
flowchart TD
    U[User Browser] -->|HTTP Request| F[Flask Web Server]
    F --> R[Route Handlers]
    R --> YT[yt-dlp Processor]
    YT --> FS[Temporary File System]
    FS --> R
    R -->|File Response| U


Components:

Flask Application – Serves the UI and handles download/processing requests

yt-dlp – Core media downloader and transcoder

Temporary Storage – No persistence; files are removed after response

Docker Container – Reproducible, portable runtime environment

📦 Project Structure
yt-downloader/
│
├── app.py                # Flask application and routing
├── requirements.txt      # Python dependencies
├── Dockerfile            # Production-ready container definition
├── templates/            # Jinja2 HTML templates (UI)
└── static/               # CSS and static assets

⚙️ Setup & Local Development
1. Clone the repository
git clone <your_repo_url>
cd yt-downloader

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the application
python app.py

5. Open the UI
http://localhost:5000

🐳 Run with Docker (Recommended)
Build the image
docker build -t yt-downloader .

Run the container
docker run -d -p 5000:5000 yt-downloader


The service will be available at:

http://localhost:5000

☁️ Deploying to Azure
Option A – Azure App Service (Docker Container)

Build and push image to Azure Container Registry (ACR):

az acr build --image yt-downloader:v1 --registry <acrName> --file Dockerfile .


Create the Web App pointing to ACR:

az webapp create \
  --name yt-downloader-app \
  --resource-group <group> \
  --plan <appServicePlan> \
  --deployment-container-image-name <acrName>.azurecr.io/yt-downloader:v1


Configure container registry authentication:

az webapp config container set \
  --name yt-downloader-app \
  --resource-group <group> \
  --docker-registry-server-url https://<acrName>.azurecr.io \
  --docker-registry-server-user <username> \
  --docker-registry-server-password <password>

Option B – Azure Container Apps
az containerapp create \
  --name yt-downloader \
  --resource-group <group> \
  --environment <containerAppEnv> \
  --image <acrName>.azurecr.io/yt-downloader:v1 \
  --target-port 5000 \
  --ingress external

📈 Roadmap
Feature	Status	Priority
Add download progress indicator	⏳ Planned	Medium
Support for playlist downloads	⏳ Planned	High
Optional file persistence	⏳ Planned	Low
API mode (JSON endpoints)	⏳ Planned	High
Authentication layer (API key / OAuth)	⏳ Planned	Medium
Logging & monitoring with Azure Insights	⏳ Planned	Medium
🧪 Tech Stack

Python 3.10+

Flask

yt-dlp

Docker

Azure (optional)
