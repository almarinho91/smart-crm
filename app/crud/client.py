from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate

def create_client(db: Session, client_data: ClientCreate):
    new_client = Client(**client_data.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def get_all_clients(db: Session):
    return db.query(Client).all()

def get_client_by_id(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def update_client(db: Session, client_id: int, updated_data: ClientCreate):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        for field, value in updated_data.dict().items():
            setattr(client, field, value)
        db.commit()
        db.refresh(client)
    return client

def delete_client(db: Session, client_id: int):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        db.delete(client)
        db.commit()
        return True
    return False