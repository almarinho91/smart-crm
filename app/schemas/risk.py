from pydantic import BaseModel

class ClientProfile(BaseModel):
    age: int
    income: float
    region: str
    has_previous_claims: bool

class RiskPrediction(BaseModel):
    risk: str