

# 🚀 Vehicle Insurance Prediction — End-to-End MLOps Project Production-grade MLOps system built using 

## MongoDB Atlas

## FastAPI

## Scikit-Learn

## AWS S3, ECR, EKS

## Docker

## GitHub Actions

## Kubernetes

## Prometheus + Grafana

## SMOTE, Feature Engineering, Model Registry, CI/CD

# 🧠 Problem Statement

Predict whether a customer will purchase vehicle insurance using demographic and historical data.

The system implements a fully automated MLOps pipeline, from data ingestion to production deployment and monitoring.

# 📌 Architecture (High-Level)

✔️ Data Source → MongoDB Atlas
✔️ Training Pipeline → Python + Scikit-Learn
✔️ Model Registry → AWS S3
✔️ CI/CD → GitHub Actions
✔️ Deployment → AWS EKS (Kubernetes)
✔️ Observability → Prometheus + Grafana

Automatic model retraining & version comparison included!

# 📂 Project Setup
1️⃣ Create project structure
python template.py

2️⃣ Install local package

Add modules in:

setup.py

pyproject.toml

Reference: crashcourse.txt

3️⃣ Create & activate virtual environment
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list

🗃️ MongoDB Atlas Setup

Sign up → Create project

Deploy free tier cluster (M0)

Create DB user + password

Add IP access: 0.0.0.0/0

Copy connection string (Python, v4.6+)

Create notebook & push dataset to MongoDB

Verify data in Collections → Browse data

🧾 Logging & Exception Handling

Create logger.py

Create exception.py

Test using:

python demo.py

# 📊 Data Pipeline Components
✔️ 1. Data Ingestion

Define config: constants/__init__.py

Write DB connection: configuration/mongo_db_connection.py

Data access: data_access/proj1_data.py

Entity configs: entity/config_entity.py

Artifacts: entity/artifact_entity.py

Set MongoDB URL:

Bash
export MONGODB_URL="mongodb+srv://...."

PowerShell
$env:MONGODB_URL="mongodb+srv://...."

# ✔️ 2. Data Validation

Add schema.yaml

Implement validation code in data_validation component

Validate column types, missing fields, schema mismatch

# ✔️ 3. Data Transformation

Feature encoding

One-hot encoding

Scaling

SMOTE-ENN imbalance handling

Save preprocessor.pkl

# ✔️ 4. Model Training

Build model (RandomForestClassifier)

Compute metrics:

F1

Precision

Recall

Save model.pkl

# ☁️ AWS Integration (Model Registry + Push)
Create IAM user (CLI access)

Create access key

Export to terminal:

export AWS_ACCESS_KEY_ID="xxx"
export AWS_SECRET_ACCESS_KEY="yyy"

Create S3 bucket
mlops-project-model-mlopsproj

Code required

aws_connection.py

s3_estimator.py

# ✔️ 5. Model Evaluation

Load production model from S3

Compare new vs old model

If new model F1 > old model F1 → push to S3 automatically

Threshold:

MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02

# ✔️ 6. Model Pusher

Upload model to S3 registry

Maintain versioning

# ✔️ 7. Prediction Pipeline

REST API using FastAPI

Swagger UI enabled

Load model + preprocessor from S3

# 🐳 CI/CD — Docker + GitHub Actions
YAML contains:

Build Docker image

Login to ECR

Push image to ECR

# Deploy to EKS

GitHub Secrets
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO

# ☸️ AWS EKS Deployment
Install CLI
kubectl
eksctl

Create EKS cluster
eksctl create cluster \
--name vehicle-insurance-cluster \
--region us-east-1 \
--node-type t2.medium \
--nodes 2

Deploy Kubernetes manifests
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# 📈 Observability (Production Monitoring)

✔️ Prometheus — metrics scraping
✔️ Grafana — dashboards
✔️ Helm — deployment automation

# Monitor:

API latency

Pod usage

Model prediction distribution

Error rate


# 🧹 Cleanup & Tear-Down

Delete EKS cluster

Delete ECR repo

Delete S3 bucket

Delete IAM users

Delete MongoDB cluster

Remove GitHub secrets

eksctl delete cluster --name vehicle-insurance-cluster

# 📌 Repository

🔗 https://github.com/Ravipanavi/MLOps-End-to-End-Project

⭐️ Key Features

✔️ Fully automated ML training pipeline
✔️ Model registry using AWS S3
✔️ Auto model comparison (A/B)
✔️ CI/CD deployment on Kubernetes
✔️ 100% production-ready
✔️ Scalable API using FastAPI
✔️ Live monitoring dashboards
