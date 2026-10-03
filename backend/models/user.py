import enum
import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import DateTime, String, func
from sqlalchemy.dialects.postgresql import ENUM, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models.customer_profile import CustomerProfile

try:
    from core.database import Base
except ImportError:
    from backend.core.database import Base


class UserRole(str, enum.Enum):
    CUSTOMER = "customer"
    BUSINESS = "business"
    ADMIN = "admin"
    customer = "customer"
    business = "business"
    admin = "admin"


user_role_enum = ENUM(
    UserRole,
    name="user_role",
    values_callable=lambda obj: [e.value for e in obj],
    create_type=True,
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )
    role: Mapped[UserRole] = mapped_column(
        user_role_enum,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    customer_profile: Mapped[Optional["CustomerProfile"]] = relationship(
        "CustomerProfile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )
