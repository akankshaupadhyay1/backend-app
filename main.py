from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
try:
    model = joblib.load("loan_pricing_model.pkl")
except FileNotFoundError:
    raise RuntimeError("Model file not found")

class LoanFeatures(BaseModel):
    Country: str
    Company: str
    BaseRate: float
    Inflation: float
    GDP: float
    RegulationScore: float
    LoanAmount: float
    LoanTerm: int

@app.post("/predict")
def predict(features: LoanFeatures):
    try:
        input_data = pd.DataFrame([features.dict()])
        prediction = model.predict(input_data)
        return {"loan_rate": round(float(prediction[0]), 4)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))