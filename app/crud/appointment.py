from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate

def create_appointment(db: Session, appointment_data: AppointmentCreate):
    new_appt = Appointment(**appointment_data.dict())
    db.add(new_appt)
    db.commit()
    db.refresh(new_appt)
    return new_appt

def get_all_appointments(db: Session):
    return db.query(Appointment).all()

def get_appointments_by_client(db: Session, client_id: int):
    return db.query(Appointment).filter(Appointment.client_id == client_id).all()
