from src.data_collection import collect_data
from src.data_preprocessing import preprocess_data
from src.model_builder import build_model
from src.train_model import train_model
from src.evaluate_model import evaluate
from src.save_model import save_model

collect_data()

X, y, tokenizer, total_words, max_len = (
    preprocess_data()
)

model = build_model(
    total_words,
    max_len
)

history, training_time = train_model(
    model,
    X,
    y,
    total_words
)

evaluate(
    history,
    training_time
)

save_model(
    model,
    tokenizer
)

print(
    "Training Completed Successfully"
)