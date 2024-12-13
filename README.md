# Arabic Morphology Prediction API

This repository contains an API built with **FastAPI** to predict Arabic word morphology, including:
1. **Jamid** or **Musytaq** classification.
2. Predicted Arabic verb forms: **Madhi**, **Mudhari**, and **Amar**.

The API is designed to support machine learning models trained using **TensorFlow/Keras** and integrates preprocessing tools like tokenizers and label encoders.

## Features
- Predict whether a word is **Jamid** or **Musytaq** using a trained model (`model.h5`).
- Predict Arabic verb forms (**Madhi**, **Mudhari**, and **Amar**) with another trained model (`arabic_verb_model.h5`).
- RESTful API endpoints built with **FastAPI**.
- Dockerized for seamless deployment on platforms like **Google Cloud Run**.

---

## Requirements
- Python 3.8+
- Docker (if running as a container)
- FastAPI
- TensorFlow
- Joblib
- Scikit-learn

---

## Project Structure
├── models/ │ ├── model.h5 # Jamid/Musytaq classification model │ ├── arabic_verb_model.h5 # Arabic verb prediction model ├── utils/ │ ├── tokenizer.pickle # Tokenizer for Arabic verb model │ ├── vectorizer.pkl # Vectorizer for Jamid/Musytaq model │ ├── label_encoders.pickle # Label encoders for verb prediction ├── core/ │ ├── config.py # Configuration settings ├── services/ │ ├── model.py # Model loading and prediction logic ├── endpoints/ │ ├── endpoints.py # API endpoints ├── main.py # Application entry point ├── Dockerfile # Docker setup ├── requirements.txt # Python dependencies └── README.md # Project documentation

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sxzrr/Arabic-Morph-API
cd Arabic-Morph-API

### 1. Clone the Repository
