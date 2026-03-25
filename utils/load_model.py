import joblib
import json

def load_model():
    return joblib.load("artifacts/market_price_model.pkl")

def load_mapping():
    with open("artifacts/preprocessing.json", "r") as f:
        return json.load(f)