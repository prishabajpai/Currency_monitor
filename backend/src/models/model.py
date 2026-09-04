from src.database.database import Base
from typing import List, Optional 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, Boolean, DateTime, ForeignKey
from datetime import datetime, timezone

class RateLogs(Base):
    __tablename__ = "rate_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True, autoincrement=True)
    rate: Mapped[float] = mapped_column(Float, nullable = False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False, index=True)

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)

    alerts: Mapped[List["Alerts"]] = relationship("Alerts", backpopulates="user", cascade="all, delete-orphan")

class Alerts(Base):
    __tablename__ = "user_alerts"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index = True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    last_notified_rate: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    threshold_rate: Mapped[float] = mapped_column(Float, default=0.50)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    user: Mapped["Users"] = relationship(back_populates="alerts")