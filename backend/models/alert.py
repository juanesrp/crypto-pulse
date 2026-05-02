import uuid
from sqlalchemy import Column, String, Float, DateTime, UniqueConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from core.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    coin = Column(String(50), nullable=False)
    threshold = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (UniqueConstraint("user_id", "coin", name="uq_user_coin"),)
