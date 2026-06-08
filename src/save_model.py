import joblib
import os


def save_model(model, tokenizer):

    # 🔥 FIX: ensure directory exists
    os.makedirs("models", exist_ok=True)

    # Save model
    model.save("models/best_model.keras")

    # Save tokenizer
    joblib.dump(tokenizer, "models/tokenizer.joblib")