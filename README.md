#  Small Language Model (SLM) Pipeline Deployment

##  Project Overview
This repository contains the implementation and deployment code for a Small Language Model (SLM) pipeline built as part of the Prodigal AI Internship Assignment. The project showcases real-time inference using a cloud-hosted RESTful API with sentiment classification capabilities based on DistilBERT.

---

## Model Details
- **Model Used:** `distilbert-base-uncased-finetuned-sst-2-english`
- **Task:** Sentiment Classification (Positive/Negative)
- **Library:** Hugging Face Transformers

---
## Project Structure
```bash
prodigal_ai_project/
│
├── app/
│   ├── main.py                  # FastAPI app with model endpoints
│   ├── functions.py             # Search result logic (can be extended)
│   └── data/                    # Parquet files and model paths
│
├── Dockerfile                  # Container setup
├── requirements.txt            # Python dependencies
├── frontend/                   # Optional frontend (HTML/JS or React)
├── index.html                  # Static HTML frontend
└── README.md                   # Documentation
```

---

##  FastAPI REST API
### Endpoints
- `/` → Health check
- `/info` → Model/API metadata
- `/search?query=...` → Search using semantic embedding matching

---

##  Docker Build & Run
```bash
# Build Docker image
docker build -t slm-api .

# Run locally
docker run -d --name slm-api -p 8000:8000 slm-api
```

Access API: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ☁️ Deployment on AWS ECS (Fargate)
### Step-by-Step:
1. **Build Docker Image Locally**
```bash
docker build -t slm-api .
docker tag slm-api <your-dockerhub-username>/slm-api
```

2. **Push to DockerHub**
```bash
docker push <your-dockerhub-username>/slm-api
```

3. **ECS Setup (Console)**
- Navigate to ECS > Clusters > Create Cluster (use Fargate).
- Create a **task definition** with the following:
  - Container image: `your-dockerhub-username/slm-api`
  - Port mapping: `8000:8000`
  - Assign `ecsTaskExecutionRole` with:
    - `AmazonECSTaskExecutionRolePolicy`
    - `CloudWatchLogsFullAccess`

4. **Service Setup**
- Create a service linked to the task definition.
- Choose desired autoscaling config.
- Map port 8000 in the **load balancer** or networking.

5. **Accessing the API**
- Find public IP / DNS of load balancer.
- Visit: `http://<your-ecs-load-balancer>:8000/docs`

---

## Testing
- **Postman** or **cURL** to hit `/search?query=...`
- **Swagger UI:** at `/docs`
- **Browser:** visit index.html if using HTML frontend

---

## Monitoring
- **Logs:** CloudWatch (enabled via ecsTaskExecutionRole)
- **Metrics:** ECS service dashboard

---

##  Deliverables Summary
| Component         | Status       | Description                                          |
|------------------|--------------|------------------------------------------------------|
| Model & Pipeline | ✅ Complete  | DistilBERT-based sentiment API using FastAPI         |
| Cloud Deployment | ✅ Complete  | Hosted via AWS ECS (Fargate)                         |
| Docker Container | ✅ Complete  | Includes Dockerfile and pushed to DockerHub         |
| Documentation    | ✅ Complete  | Setup instructions, architecture, usage included     |
| Monitoring Setup | ✅ Complete  | Integrated with CloudWatch for logs & metrics        |
| Frontend (Bonus) | ✅ (Static)  | HTML frontend to interact with API              |

---


## Credits
Project built by **Aadya Sharma** for the Gen AI Internship @ Prodigal AI.

---
# prodigal-ai-task
