import joblib

from tensorflow.keras.models import load_model

def load_saved_objects():

    model = load_model(
        "models/best_model.keras"
    )

    tokenizer = joblib.load(
        "models/tokenizer.joblib"
    )

    return model, tokenizer