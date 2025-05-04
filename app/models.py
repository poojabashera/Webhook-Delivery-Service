from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class WebhookClient(Base):
    __tablename__ = "webhook_clients"

    id = Column(String, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    webhook_url = Column(String, unique=True, nullable=False)
    registered_at = Column(DateTime(timezone=True), server_default=func.now())
