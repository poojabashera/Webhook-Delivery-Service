from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.database import SessionLocal
import uuid

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Webhook delivery system is running."}

@app.post("/register", response_model=schemas.WebhookClientOut)
def register_webhook(client: schemas.WebhookClientCreate, db: Session = Depends(get_db)):
    existing = db.query(models.WebhookClient).filter_by(webhook_url=client.webhook_url).first()
    if existing:
        raise HTTPException(status_code=400, detail="Webhook URL already registered.")

    new_client = models.WebhookClient(
        id=str(uuid.uuid4()),
        client_name=client.client_name,
        webhook_url=client.webhook_url
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client
from app.schemas import EventIn
from app import worker

@app.post("/event")
def send_event(event: EventIn, db: Session = Depends(get_db)):
    client = db.query(models.WebhookClient).filter_by(id=event.client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    job = {
        "client_id": event.client_id,
        "webhook_url": client.webhook_url,
        "payload": event.payload,
    }
    worker.enqueue_event(job)
    return {"message": "Event queued"}
