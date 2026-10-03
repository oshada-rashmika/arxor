import uuid
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Boolean, ForeignKey, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.experience import Experience

try:
    from core.database import Base
except ImportError:
    from backend.core.database import Base

try:
    from models.user import User
except ImportError:
    from backend.models.user import User


class BusinessProfile(Base):
    __tablename__ = "business_profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    business_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    category: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    description: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
    )
    tier: Mapped[str] = mapped_column(
        String,
        default="free",
        server_default="free",
        nullable=False,
    )
    phone: Mapped[Optional[str]] = mapped_column(
        String,
        nullable=True,
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default=text("false"),
        nullable=False,
    )
    lankaqr_code: Mapped[Optional[str]] = mapped_column(
        String,
        unique=True,
        nullable=True,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="business_profile",
    )

    experiences: Mapped[list["Experience"]] = relationship(
        "Experience",
        back_populates="business_profile",
        cascade="all, delete-orphan",
    )
