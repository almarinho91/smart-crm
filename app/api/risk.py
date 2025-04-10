from fastapi import APIRouter
from app.schemas.risk import ClientProfile, RiskPrediction
from app.utils.risk_predictor import predict_risk

router = APIRouter(prefix="/predict-risk", tags=["Risk Prediction"])

@router.post("/", response_model=RiskPrediction)
def predict_risk_api(profile: ClientProfile):
    risk = predict_risk(profile)
    return {"risk": risk}