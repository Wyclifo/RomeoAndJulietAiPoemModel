import json
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