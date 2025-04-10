from fastapi import FastAPI
from app.database import Base, engine
from app.api import client as client_api
from app.api import appointment as appointment_api
from app.api import risk as risk_api


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Create tables on startup
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(client_api.router)

app.include_router(appointment_api.router)

Base.metadata.create_all(bind=engine)

app.include_router(risk_api.router)


