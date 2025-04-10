from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.appointment import AppointmentCreate, AppointmentOut
from app.crud import appointment as appointment_crud

router = APIRouter(prefix="/appointments", tags=["Appointments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AppointmentOut)
def create_appointment(appt_data: AppointmentCreate, db: Session = Depends(get_db)):
    return appointment_crud.create_appointment(db, appt_data)

@router.get("/", response_model=list[AppointmentOut])
def list_appointments(db: Session = Depends(get_db)):
    return appointment_crud.get_all_appointments(db)

@router.get("/by-client/{client_id}", response_model=list[AppointmentOut])
def list_by_client(client_id: int, db: Session = Depends(get_db)):
    return appointment_crud.get_appointments_by_client(db, client_id)
