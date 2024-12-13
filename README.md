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
```
├── api/
│   ├── endpoints.py           # API endpoints
│   ├── arabic_verb_model.h5   # Arabic verb prediction model
├── core/
│   ├── config.py              # Configuration settings
├── model/
│   ├── model.h5               # Jamid/Musytaq classification model
│   ├── arabic_verb_model.h5   # Arabic verb prediction model
├── models/
│   ├── prediction.py          # Prediction settings
├── utils/
│   ├── tokenizer.pickle       # Tokenizer for Arabic verb model
│   ├── vectorizer.pkl         # Vectorizer for Jamid/Musytaq model
│   ├── label_encoders.pickle  # Label encoders for verb prediction
├── services/
│   ├── model.py               # Model loading and prediction logic
├── main.py                    # Application entry point
├── Dockerfile                 # Docker setup
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sxzrr/Arabic-Morph-API
cd Arabic-Morph-API
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed and create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Locally
Start the FastAPI server locally:
```bash
uvicorn main:app --reload
```
The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 4. Test API
You can test the API using tools like:
- [Swagger UI](http://127.0.0.1:8000/docs)
- [Postman](https://www.postman.com/)

---

## API Endpoints

### 1. `/predict`
Predict whether a word is **Jamid** or **Musytaq**.

#### Request:
```json
POST /predict
Content-Type: application/json
{
  "text": "غمي"
}
```

#### Response:
```json
{
  "text": "غمي",
  "prediction": "jamid"
}
```

---

### 2. `/predict2`
Predict the Arabic verb forms (**Madhi**, **Mudhari**, and **Amar**).

#### Request:
```json
POST /predict2
Content-Type: application/json
{
  "text": "أكل"
}
```

#### Response:
```json
{
  "text": "أكل",
  "predictions": {
    "Madhi": "أكل",
    "Mudhari": "يأكل",
    "Amar": "كل"
  }
}
```

---

## Deployment on Google Cloud

### 1. Build Docker Image
```bash
docker build -t us.gcr.io/capstone-project-arabic-morph/arabic-morph-api .
```

### 2. Push to Artifact Registry
```bash
docker push us.gcr.io/capstone-project-arabic-morph/arabic-morph-api
```

### 3. Deploy to Cloud Run
```bash
gcloud run deploy api-arabic \
    --image us.gcr.io/capstone-project-arabic-morph/arabic-morph-api \
    --region asia-southeast2 \
    --platform managed \
    --allow-unauthenticated
```

---

## Acknowledgments
- **TensorFlow/Keras** for the machine learning framework.
- **FastAPI** for providing a modern and fast API development experience.
- **Google Cloud** for hosting and deployment.

---
