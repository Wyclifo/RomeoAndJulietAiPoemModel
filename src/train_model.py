import json
import time
import numpy as np
import matplotlib.pyplot as plt
import os


def evaluate(history, training_time):

    # 🔥 FIX: ensure folder exists
    os.makedirs("visualizations", exist_ok=True)

    accuracy = max(history.history["accuracy"])
    val_accuracy = max(history.history["val_accuracy"])
    final_loss = min(history.history["val_loss"])

    perplexity = float(np.exp(final_loss))

    metrics = {
        "accuracy": float(accuracy),
        "validation_accuracy": float(val_accuracy),
        "loss": float(final_loss),
        "perplexity": perplexity,
        "training_time_seconds": float(training_time)
    }

    # Save metrics
    with open("visualizations/metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    # Accuracy plot
    plt.figure()
    plt.plot(history.history["accuracy"])
    plt.plot(history.history["val_accuracy"])
    plt.title("Accuracy")
    plt.legend(["train", "val"])
    plt.savefig("visualizations/accuracy.png")
    plt.close()

    # Loss plot
    plt.figure()
    plt.plot(history.history["loss"])
    plt.plot(history.history["val_loss"])
    plt.title("Loss")
    plt.legend(["train", "val"])
    plt.savefig("visualizations/loss.png")
    plt.close()


    import time
from tensorflow.keras.utils import to_categorical


def train_model(model, X, y, total_words):

    start_time = time.time()

    y = to_categorical(y, num_classes=total_words)

    history = model.fit(
        X,
        y,
        epochs=30,
        batch_size=128,
        validation_split=0.2,
        verbose=1
    )

    training_time = time.time() - start_time

    return history, training_time