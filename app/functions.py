from transformers import pipeline

# Load the sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Define function to get sentiment

def predict_sentiment(text: str):
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }