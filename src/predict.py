import numpy as np
import random
from tensorflow.keras.preprocessing.sequence import pad_sequences
from src.load_model import load_saved_objects


model, tokenizer = load_saved_objects()


def sample_with_temperature(preds, temperature=1.0):

    preds = np.asarray(preds).astype("float64")

    preds = np.log(preds + 1e-8) / temperature
    exp_preds = np.exp(preds)

    preds = exp_preds / np.sum(exp_preds)

    probas = np.random.multinomial(1, preds, 1)

    return np.argmax(probas)


def generate_poem(seed_text, max_len, words=40, temperature=0.8):

    result = seed_text

    for _ in range(words):

        token_list = tokenizer.texts_to_sequences([result])[0]

        token_list = pad_sequences(
            [token_list],
            maxlen=max_len - 1,
            padding="pre"
        )

        predictions = model.predict(token_list, verbose=0)[0]

        predicted_index = sample_with_temperature(predictions, temperature)

        next_word = ""

        for word, index in tokenizer.word_index.items():
            if index == predicted_index:
                next_word = word
                break

        if not next_word:
            break

        result += " " + next_word

    return result