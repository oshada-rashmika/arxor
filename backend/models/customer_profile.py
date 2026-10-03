import uuid
from datetime import datetime
from typing import Any, Optional

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

try:
    from core.database import Base
except ImportError:
    from backend.core.database import Base

try:
    from models.user import User
except ImportError:
    from backend.models.user import User


class CustomerProfile(Base):
    __tablename__ = "customer_profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    full_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    avatar_url: Mapped[Optional[str]] = mapped_column(
        String,
        nullable=True,
    )
    tier: Mapped[str] = mapped_column(
        String,
        default="free",
        server_default="free",
        nullable=False,
    )
    tier_expires_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    interests: Mapped[Optional[Any]] = mapped_column(
        JSONB,
        nullable=True,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="customer_profile",
    )
