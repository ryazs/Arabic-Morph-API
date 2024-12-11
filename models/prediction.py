from pydantic import BaseModel
from typing import Dict

class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    text: str
    prediction: str

class ArabicVerbPredictionResponse(BaseModel):
    text: str
    predictions: Dict[str, str]

