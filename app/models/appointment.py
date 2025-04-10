from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    topic = Column(String(100), nullable=False)
    notes = Column(Text, nullable=True)

    # Optional: Link back to client if needed
    client = relationship("Client", backref="appointments")
