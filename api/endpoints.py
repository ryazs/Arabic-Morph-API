from fastapi import APIRouter, HTTPException
from models.prediction import PredictionRequest, PredictionResponse, ArabicVerbPredictionResponse
from services.model import predict_text, predict_arabic_verb
from fastapi.logger import logger

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(data: PredictionRequest):
    try:
        result = predict_text(data.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@router.post("/predict2", response_model=ArabicVerbPredictionResponse)
async def predict_arabic_verb_endpoint(data: PredictionRequest):
    try:
        predictions = predict_arabic_verb(data.text)
        return ArabicVerbPredictionResponse(text=data.text, predictions=predictions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Arabic verb prediction error: {str(e)}")

