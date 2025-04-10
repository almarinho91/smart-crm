from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    client_id: int
    date: datetime
    topic: str
    notes: str | None = None

class AppointmentOut(AppointmentCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
