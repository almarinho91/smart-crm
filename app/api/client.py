from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.client import ClientCreate, ClientOut
from app.crud import client as client_crud

router = APIRouter(prefix="/clients", tags=["Clients"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ClientOut)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return client_crud.create_client(db, client)

@router.get("/", response_model=list[ClientOut])
def list_clients(db: Session = Depends(get_db)):
    return client_crud.get_all_clients(db)

@router.get("/{client_id}", response_model=ClientOut)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = client_crud.get_client_by_id(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{client_id}", response_model=ClientOut)
def update_client(client_id: int, client_data: ClientCreate, db: Session = Depends(get_db)):
    client = client_crud.update_client(db, client_id, client_data)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/{client_id}", status_code=204)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    deleted = client_crud.delete_client(db, client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Client not found")