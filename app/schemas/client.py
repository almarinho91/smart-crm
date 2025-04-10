from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    email: str
    phone: str | None = None

class ClientOut(ClientCreate):
    id: int

    model_config = {
        "from_attributes": True
    }