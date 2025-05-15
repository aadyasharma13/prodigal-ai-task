from fastapi import FastAPI
from transformers import pipeline

# Load sentiment analysis model
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased")

# Create FastAPI object
app = FastAPI()

# API endpoints
@app.get("/")
def health_check():
    return {"health_check": "OK"}

@app.get("/info")
def info():
    return {
        "name": "sentiment-api",
        "description": "Sentiment analysis API using DistilBERT."
    }

@app.get("/predict")
def predict(text: str):
    result = sentiment_model(text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }