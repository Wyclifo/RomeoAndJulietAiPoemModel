import os

os.makedirs("models", exist_ok=True)
os.makedirs("visualizations", exist_ok=True)
os.makedirs("data", exist_ok=True)
DATA_PATH = "data/romeo_and_juliet.txt"

MODEL_PATH = "models/best_model.keras"

TOKENIZER_PATH = "models/tokenizer.joblib"

VISUALIZATION_PATH = "visualizations"

