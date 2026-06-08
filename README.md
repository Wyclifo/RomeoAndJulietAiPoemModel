# 🎭 Shakespeare Poem Generation AI

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green.svg)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-LSTM-red.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)
![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-purple.svg)
![Status](https://img.shields.io/badge/Project-Active-success.svg)

---

## 🧠 Overview

An end-to-end **Deep Learning NLP system** that generates Shakespeare-style poetry using an **LSTM neural network** trained on *Romeo and Juliet*.

This project demonstrates a full **AI engineering lifecycle** from dataset → training → API → deployment.

---

## 🖼️ Demo Preview

> Replace these with real screenshots or GIFs from your project

### 🏠 Landing Page
![UI](https://via.placeholder.com/900x400.png?text=AI+Poem+Generator+UI)

### ✍️ Generated Poem Output
![Output](https://via.placeholder.com/900x400.png?text=Generated+Shakespeare+Poem)

---

## 🚀 Features

- 🎭 Shakespeare-style poem generation
- 🧠 LSTM-based neural network
- ⚙️ Adjustable creativity (temperature)
- 📏 Custom poem length control
- 🌐 FastAPI REST backend
- 🐳 Docker containerization
- 📊 Training evaluation metrics
- 🔁 Real-time text generation

---

## 🧬 AI Architecture

---

## 📚 Dataset

- 📖 *Romeo and Juliet* — William Shakespeare  
- 📦 Source: Project Gutenberg  

### Why this dataset?
- Rich poetic structure
- Strong linguistic patterns
- Classical vocabulary ideal for NLP

---

## 📁 Project Structure

---

## ⚙️ AI Pipeline

---

## 🌐 API Endpoints

### 🔹 Health Check

Response:
```json
{ "status": "healthy" }

POST /api/v1/generate
{
  "text": "love is",
  "temperature": 0.8,
  "words": 40
}
{
  "generated_poem": "love is the golden light that burns within the soul"
}
docker build -t shakespeare-poem-ai .
docker run -p 8000:8000 shakespeare-poem-ai
docker compose up --build
love is
love is the gentle flame that guides the soul through night

---
