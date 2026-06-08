import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def preprocess_data():

    text = open(
        "data/romeo_and_juliet.txt",
        encoding="utf-8"
    ).read().lower()

    tokenizer = Tokenizer()

    tokenizer.fit_on_texts([text])

    total_words = len(tokenizer.word_index) + 1

    input_sequences = []

    for line in text.split("\n"):

        token_list = tokenizer.texts_to_sequences([line])[0]

        for i in range(1, len(token_list)):
            ngram_seq = token_list[:i+1]
            input_sequences.append(ngram_seq)

    max_sequence_len = max(
        [len(seq) for seq in input_sequences]
    )

    input_sequences = np.array(
        pad_sequences(
            input_sequences,
            maxlen=max_sequence_len,
            padding='pre'
        )
    )

    X = input_sequences[:, :-1]
    y = input_sequences[:, -1]

    return X, y, tokenizer, total_words, max_sequence_len