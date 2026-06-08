from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout


def build_model(total_words, sequence_length):

    model = Sequential()

    model.add(
        Embedding(
            input_dim=total_words,
            output_dim=128,
            input_length=sequence_length - 1
        )
    )

    # 🔥 smaller + more stable than 256
    model.add(LSTM(128, return_sequences=True))
    model.add(Dropout(0.3))

    model.add(LSTM(128))
    model.add(Dropout(0.3))

    model.add(Dense(total_words, activation="softmax"))

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy", "top_k_categorical_accuracy"]
    )

    return model