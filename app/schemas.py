from pydantic import BaseModel

class WebhookClientCreate(BaseModel):
    client_name: str
    webhook_url: str

class WebhookClientOut(BaseModel):
    id: str
    client_name: str
    webhook_url: str

    class Config:
        orm_mode = True
    
class EventIn(BaseModel):
    client_id: str
    payload: dict
