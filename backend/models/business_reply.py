import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.business_profile import BusinessProfile
    from models.review import Review

try:
    from core.database import Base
except ImportError:
    from backend.core.database import Base


class BusinessReply(Base):
    __tablename__ = "business_replies"

    review_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("reviews.id"),
        primary_key=True,
        nullable=False,
    )
    business_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("business_profiles.user_id"),
        nullable=False,
    )
    reply_content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    review: Mapped["Review"] = relationship(
        "Review",
        back_populates="business_reply",
    )
    business_profile: Mapped["BusinessProfile"] = relationship(
        "BusinessProfile",
        back_populates="business_replies",
    )
