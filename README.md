# 🎭 Shakespeare Poem Generation AI (LSTM + FastAPI + Docker)

## 📌 Project Overview

This project is a Deep Learning-based Natural Language Processing (NLP) system that generates Shakespeare-style poetry using a **Long Short-Term Memory (LSTM)** neural network trained on *Romeo and Juliet*.

It demonstrates the full **Artificial Intelligence lifecycle**:

* Data Collection
* Data Preprocessing
* Model Training (LSTM)
* Model Evaluation
* Prediction & Text Generation
* REST API Deployment (FastAPI)
* Containerization (Docker)

---

# 🧠 Machine Learning Approach

## Model Type: LSTM (Long Short-Term Memory)

LSTM is a type of Recurrent Neural Network (RNN) designed for sequence learning.

It is ideal for poetry generation because:

* Language is sequential
* Context matters across long text
* It learns dependencies between words

---

## 🏗️ Model Architecture

```
Input Text → Tokenization → Embedding Layer → LSTM Layer → Dense Softmax → Next Word Prediction
```

---

# 📚 Dataset

## Source

* 📖 Romeo and Juliet — William Shakespeare
* Source: Project Gutenberg

## Why this dataset?

* Rich poetic structure
* Strong linguistic patterns
* Shakespearean vocabulary
* Ideal for language modeling

---

# 📁 Project Structure

```
poem-generation-ai/
│
├── data/
│   └── romeo_and_juliet.txt
│
├── models/
│   ├── best_model.keras
│   └── tokenizer.joblib
│
├── visualizations/
│   ├── accuracy.png
│   ├── loss.png
│   ├── confusion_matrix.png
│   └── metrics.json
│
├── src/
│   ├── data_collection.py
│   ├── data_preprocessing.py
│   ├── model_builder.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── save_model.py
│   ├── load_model.py
│   ├── predict.py
│   └── config.py
│
├── api/
│   └── main.py
│
├── train.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚙️ How Artificial Intelligence Works in This Project

---

## 1. 📥 Data Collection

The system downloads Shakespeare’s text from Project Gutenberg.

### File:

```python
src/data_collection.py
```

### Output:

```
data/romeo_and_juliet.txt
```

---

## 2. 🧹 Data Preprocessing

Raw text is converted into machine-readable format.

### Steps:

### ✔ Lowercasing

```
Love IS → love is
```

### ✔ Tokenization

```
love → 1
is → 2
beautiful → 3
```

### ✔ Sequence Generation

```
love is → predict next word
love is beautiful → training sequence
```

### ✔ Padding

Ensures equal-length inputs for neural network training.

---

## 3. 🧠 Training Algorithm

### File:

```
src/model_builder.py
src/train_model.py
```

### Model Components:

#### Embedding Layer

Converts words into vectors:

```
love → [0.12, -0.33, 0.88]
```

#### LSTM Layer

Learns:

* Grammar structure
* Context
* Poetry patterns

#### Dense Softmax Layer

Predicts next word probability.

---

## ⚙️ Optimizer

* Adam Optimizer
* Loss: Categorical Crossentropy

---

## 4. 📊 Model Evaluation

### File:

```
src/evaluate_model.py
```

### Metrics:

| Metric              | Description                |
| ------------------- | -------------------------- |
| Accuracy            | Correct predictions        |
| Validation Accuracy | Generalization performance |
| Loss                | Prediction error           |
| Perplexity          | Language uncertainty       |
| Training Time       | Performance efficiency     |

---

### 📈 Outputs

```
visualizations/accuracy.png
visualizations/loss.png
visualizations/metrics.json
```

---

## 5. ✍️ Prediction & Text Generation

### File:

```
src/predict.py
```

### Process:

1. User inputs seed text
2. Text is tokenized
3. Model predicts next word
4. Word is appended
5. Process repeats

---

### Example:

Input:

```
love is
```

Output:

```
love is the gentle light that guides the human heart through night
```

---

## 6. 🚀 Model Saving

### Files:

* Model:

```
models/best_model.keras
```

* Tokenizer:

```
models/tokenizer.joblib
```

---

## 7. 🌐 FastAPI Deployment

### Base URL:

```
http://localhost:8000
```

---

### Health Check

```
GET /api/v1/health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Generate Poem

```
POST /api/v1/generate
```

Request:

```json
{
  "text": "love is"
}
```

Response:

```json
{
  "generated_poem": "love is the golden fire that burns within the soul"
}
```

---

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t poem-ai .
```

---

### Run API

```bash
docker run -p 8000:8000 poem-ai
```

---

### Run with Docker Compose

```bash
docker compose up --build
```

---

## 🧪 Testing API (curl)

### Windows CMD

```bash
curl -X POST http://localhost:8000/api/v1/generate ^
-H "Content-Type: application/json" ^
-d "{\"text\":\"love is\"}"
```

---

### PowerShell

```powershell
curl -X POST "http://localhost:8000/api/v1/generate" `
-H "Content-Type: application/json" `
-d '{"text":"love is"}'
```

---

## 📦 Installation (Local Setup)

```bash
pip install -r requirements.txt
python train.py
uvicorn api.main:app --reload
```

---

## 📊 Training Pipeline

```
Data Collection
      ↓
Preprocessing
      ↓
LSTM Model Training
      ↓
Evaluation
      ↓
Model Saving
      ↓
API Deployment
```

---

## 🔮 Future Improvements

* Replace LSTM with Transformer (GPT-style model)
* Add Beam Search decoding
* Improve rhyme detection
* Add temperature sampling for creativity control
* Deploy to AWS / Azure / GCP
* Add frontend UI for poem generation

---

## 🏁 Conclusion

This project demonstrates an end-to-end AI system for poetry generation using LSTM neural networks. It integrates:

* Deep Learning (LSTM)
* NLP preprocessing
* Model evaluation
* REST API development
* Docker containerization

It serves as a complete **production-style AI pipeline** suitable for learning, portfolios, and deployment.
